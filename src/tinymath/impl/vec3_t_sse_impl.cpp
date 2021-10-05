#if defined(TINYMATH_SSE_ENABLED)

#include <xmmintrin.h>

#include <tinymath/impl/vec3_t_sse_impl.hpp>

namespace tiny {
namespace math {
namespace sse {

// ***************************************************************************//
//   Implementations for single-precision floating point numbers (float32_t)  //
// ***************************************************************************//
using Vec3f = Vector3<float32_t>;
using Array3f = Vec3f::BufferType;

// NOLINTNEXTLINE(runtime/references)
auto kernel_add_v3f(Array3f& dst, const Array3f& lhs, const Array3f& rhs)
    -> void {
    auto xmm_lhs = _mm_loadu_ps(lhs.data());
    auto xmm_rhs = _mm_loadu_ps(rhs.data());
    auto xmm_result = _mm_add_ps(xmm_lhs, xmm_rhs);
    _mm_storeu_ps(dst.data(), xmm_result);
}

// NOLINTNEXTLINE(runtime/references)
auto kernel_sub_v3f(Array3f& dst, const Array3f& lhs, const Array3f& rhs)
    -> void {
    auto xmm_lhs = _mm_loadu_ps(lhs.data());
    auto xmm_rhs = _mm_loadu_ps(rhs.data());
    auto xmm_result = _mm_sub_ps(xmm_lhs, xmm_rhs);
    _mm_storeu_ps(dst.data(), xmm_result);
}

// NOLINTNEXTLINE(runtime/references)
auto kernel_scale_v3f(Array3f& dst, float32_t scale, const Array3f& vec)
    -> void {
    auto xmm_scale = _mm_set1_ps(scale);
    auto xmm_vector = _mm_loadu_ps(vec.data());
    auto xmm_result = _mm_mul_ps(xmm_scale, xmm_vector);
    _mm_storeu_ps(dst.data(), xmm_result);
}

}  // namespace sse
}  // namespace math
}  // namespace tiny

#endif  // TINYMATH_SSE_ENABLED
