#if defined(TINYMATH_SSE_ENABLED)

#include <smmintrin.h>
#include <xmmintrin.h>

#include <tinymath/impl/vec3_t_sse_impl.hpp>

/**
 * SSE instruction sets required for each kernel:
 *
 * - kernel_add_v3f                 : SSE
 * - kernel_sub_v3f                 : SSE
 * - kernel_scale_v3f               : SSE
 * - kernel_hadamard_v3f            : SSE
 * - kernel_length_square_v3f       : SSE4.1 (_mm_dp_ps)
 * - kernel_length_v3f              : SSE4.1 (_mm_dp_ps)
 * - kernel_normalize_in_place_v3f  : SSE4.1 (_mm_dp_ps)
 * - kernel_dot_v3f                 : SSE4.1 (_mm_dp_ps)
 * - kernel_cross_v3f               : SSE
 */

namespace tiny {
namespace math {
namespace sse {

// ***************************************************************************//
//   Implementations for single-precision floating point numbers (float32_t)  //
// ***************************************************************************//
using Vec3f = Vector3<float32_t>;
using Array3f = Vec3f::BufferType;

auto kernel_add_v3f(Array3f& dst, const Array3f& lhs, const Array3f& rhs)
    -> void {
    auto xmm_lhs = _mm_load_ps(lhs.data());
    auto xmm_rhs = _mm_load_ps(rhs.data());
    auto xmm_result = _mm_add_ps(xmm_lhs, xmm_rhs);
    _mm_store_ps(dst.data(), xmm_result);
}

auto kernel_sub_v3f(Array3f& dst, const Array3f& lhs, const Array3f& rhs)
    -> void {
    auto xmm_lhs = _mm_load_ps(lhs.data());
    auto xmm_rhs = _mm_load_ps(rhs.data());
    auto xmm_result = _mm_sub_ps(xmm_lhs, xmm_rhs);
    _mm_store_ps(dst.data(), xmm_result);
}

auto kernel_scale_v3f(Array3f& dst, float32_t scale, const Array3f& vec)
    -> void {
    auto xmm_scale = _mm_set1_ps(scale);
    auto xmm_vector = _mm_load_ps(vec.data());
    auto xmm_result = _mm_mul_ps(xmm_scale, xmm_vector);
    _mm_store_ps(dst.data(), xmm_result);
}

auto kernel_hadamard_v3f(Array3f& dst, const Array3f& lhs, const Array3f& rhs)
    -> void {
    auto xmm_lhs = _mm_load_ps(lhs.data());
    auto xmm_rhs = _mm_load_ps(rhs.data());
    _mm_store_ps(dst.data(), _mm_mul_ps(xmm_lhs, xmm_rhs));
}

auto kernel_length_square_v3f(const Array3f& vec) -> float32_t {
    // Implementation based on this post: https://bit.ly/3FyZF0n
    constexpr int32_t COND_PROD_MASK = 0x71;
    auto xmm_v = _mm_load_ps(vec.data());
    return _mm_cvtss_f32(_mm_dp_ps(xmm_v, xmm_v, COND_PROD_MASK));
}

auto kernel_length_v3f(const Array3f& vec) -> float32_t {
    // Implementation based on this post: https://bit.ly/3FyZF0n
    constexpr int32_t COND_PROD_MASK = 0x71;
    auto xmm_v = _mm_load_ps(vec.data());
    return _mm_cvtss_f32(_mm_sqrt_ss(_mm_dp_ps(xmm_v, xmm_v, COND_PROD_MASK)));
}

auto kernel_normalize_in_place_v3f(Array3f& vec) -> void {
    // Implementation based on this post: https://bit.ly/3FyZF0n
    constexpr int32_t COND_PROD_MASK = 0x7f;
    auto xmm_v = _mm_load_ps(vec.data());
    auto xmm_sums = _mm_dp_ps(xmm_v, xmm_v, COND_PROD_MASK);
    auto xmm_r_sqrt_sums = _mm_sqrt_ps(xmm_sums);
    auto xmm_v_norm = _mm_div_ps(xmm_v, xmm_r_sqrt_sums);
    _mm_store_ps(vec.data(), xmm_v_norm);
}

auto kernel_dot_v3f(const Array3f& lhs, const Array3f& rhs) -> float32_t {
    constexpr int32_t COND_PROD_MASK = 0x71;
    auto xmm_lhs = _mm_load_ps(lhs.data());
    auto xmm_rhs = _mm_load_ps(rhs.data());
    auto xmm_cond_prod = _mm_dp_ps(xmm_lhs, xmm_rhs, COND_PROD_MASK);
    return _mm_cvtss_f32(xmm_cond_prod);
};

auto kernel_cross_v3f(Array3f& dst, const Array3f& lhs, const Array3f& rhs)
    -> void {
    // Implementation adapted from @ian_mallett (https://bit.ly/3lu6pVe)
    constexpr auto MASK_A = tiny::math::ShuffleMask<3, 0, 2, 1>::value;
    constexpr auto MASK_B = tiny::math::ShuffleMask<3, 1, 0, 2>::value;
    // Recall that the dot product of two 3d-vectors a and b given by:
    // a = {a[0], a[1], a[2], a[3]=0}, b = {b[0], b[1], b[2], b[3]=0}
    // has as resulting expression:
    // a (x) b = [a[1] * b[2] - a[2] * b[1],
    //            a[2] * b[0] - a[0] * b[2],
    //            a[0] * b[1] - a[1] * b[0],
    //                        0            ]
    auto vec_0 = _mm_load_ps(lhs.data());  // a = {a[0], a[1], a[2], a[3]=0}
    auto vec_1 = _mm_load_ps(rhs.data());  // b = {b[0], b[1], b[2], b[3]=0}
    // tmp_0 = {a[1], a[2], a[0], 0}
    auto tmp_0 = _mm_shuffle_ps(vec_0, vec_0, MASK_A);
    // tmp_1 = {b[2], b[0], b[1], 0}
    auto tmp_1 = _mm_shuffle_ps(vec_1, vec_1, MASK_B);
    // tmp_2 = {a[2], a[0], a[1], 0}
    auto tmp_2 = _mm_shuffle_ps(vec_0, vec_0, MASK_B);
    // tmp_3 = {b[1], b[2], b[0], 0}
    auto tmp_3 = _mm_shuffle_ps(vec_1, vec_1, MASK_A);
    _mm_store_ps(dst.data(), _mm_sub_ps(_mm_mul_ps(tmp_0, tmp_1),
                                        _mm_mul_ps(tmp_2, tmp_3)));
}

}  // namespace sse
}  // namespace math
}  // namespace tiny

#endif  // TINYMATH_SSE_ENABLED
