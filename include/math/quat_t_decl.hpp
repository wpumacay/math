#pragma once

#include <ios>
#include <array>
#include <cmath>
#include <cassert>
#include <cstdint>
#include <initializer_list>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <type_traits>

#include <math/mat4_t_decl.hpp>
#include <math/mat3_t_decl.hpp>
#include <math/vec3_t_decl.hpp>
#include <math/euler_t_decl.hpp>

namespace math {

template <typename Scalar_T>
class Matrix3;

template <typename Scalar_T>
class Matrix4;

template <typename Scalar_T>
class Euler;

}  // namespace math

namespace math {

template <typename Scalar_T>
class Quaternion {
 public:
    /// Number of scalar dimensions of the quaternion
    constexpr static uint32_t QUAT_SIZE = 4;
    /// Number of scalars used in the storage of the vector
    constexpr static uint32_t BUFFER_COUNT = 4;
    /// Number of bytes allocated for the buffer of this quaternion
    constexpr static uint32_t BUFFER_SIZE = sizeof(Scalar_T) * BUFFER_COUNT;

    /// Typename of the vector
    using Type = Quaternion<Scalar_T>;
    /// Typename of the scalar used for the vector (float32, float64, etc.)
    using ElementType = Scalar_T;
    /// Typename of the internal storage used for the vector
    using BufferType = std::array<Scalar_T, BUFFER_COUNT>;

    // Some related types
    using Vec3 = Vector3<Scalar_T>;
    using Mat3 = Matrix3<Scalar_T>;
    using Mat4 = Matrix4<Scalar_T>;

    /// Constructs a zero-initialized vector
    Quaternion() = default;

    /// Constructs a real-valued quaternion
    /// \param real Real-value part of the quaternion
    explicit Quaternion(Scalar_T real) {
        m_Elements[0] = real;
        m_Elements[1] = static_cast<Scalar_T>(0.0F);
        m_Elements[2] = static_cast<Scalar_T>(0.0F);
        m_Elements[3] = static_cast<Scalar_T>(0.0F);
    }

    /// Constructs a quaternion given its 4 components
    /// \param x_val Value of the first imaginary component
    /// \param y_val Value of the second imaginary component
    /// \param z_val Value of the third imaginary component
    /// \param w_val Value of the real-valued component
    explicit Quaternion(Scalar_T w_val, Scalar_T x_val, Scalar_T y_val,
                        Scalar_T z_val) {
        m_Elements[0] = w_val;
        m_Elements[1] = x_val;
        m_Elements[2] = y_val;
        m_Elements[3] = z_val;
    }

    /// Constructs a quaternion given a 3x3 rotation matrix
    /// \param[in] matrix A 3x3 rotation matrix given by the user
    explicit Quaternion(const Mat3& matrix) { setFromRotationMatrix(matrix); }

    /// Constructs a quaternion given a 4x4 transformation matrix
    /// \param[in] matrix A 4x4 transformation matrix given by the user
    explicit Quaternion(const Mat4& transform) { setFromTransform(transform); }

    /// Constructs a quaternion given a set of Euler angles
    /// \param[in] euler A set of euler angles describing the same rotation
    explicit Quaternion(const Euler<Scalar_T>& euler) { setFromEuler(euler); }

    /// Constructs a quaternion given an axis-angle pair
    /// \param[in] axis A vector representing the rotation axis
    /// \param[in] angle The angle by which to rotate around the given axis
    explicit Quaternion(const Vec3& axis, Scalar_T angle) {
        setFromAxisAngle(axis, angle);
    }

    // cppcheck-suppress noExplicitConstructor
    /// Constructs a quaternion from a given list of the form {x, y, z, w}
    Quaternion(const std::initializer_list<Scalar_T>& values) {
        // Complain in case we don't receive exactly 4 values
        assert(values.size() == Quaternion<Scalar_T>::QUAT_SIZE);
        // Just copy the whole data from the initializer list
        std::copy(values.begin(), values.end(), m_Elements.data());
    }

    /// \brief Updates this quaternion with a given 3x3 rotation matrix
    auto setFromRotationMatrix(const Mat3& matrix) -> void;

    /// \brief Updates this quaternion with a given 4x4 transformation matrix
    auto setFromTransform(const Mat4& transform) -> void;

    /// \brief Updates this quaternion with a given set of Euler angles
    auto setFromEuler(const Euler<Scalar_T>& euler) -> void;

    /// \brief Updates this quaternion with a given axes-angle pair
    auto setFromAxisAngle(const Vec3& axis, Scalar_T angle) -> void;

    /// Returns a mutable reference to the real w-component
    auto w() -> Scalar_T& { return m_Elements[0]; }

    /// Returns a mutable reference to the imaginary x-component
    auto x() -> Scalar_T& { return m_Elements[1]; }

    /// Returns a mutable reference to the imaginary y-component
    auto y() -> Scalar_T& { return m_Elements[2]; }

    /// Returns a mutable reference to the imaginary z-component
    auto z() -> Scalar_T& { return m_Elements[3]; }

    /// Returns an unmutable reference to the real w-component
    auto w() const -> const Scalar_T& { return m_Elements[0]; }

    /// Returns an unmutable reference to the imaginary x-component
    auto x() const -> const Scalar_T& { return m_Elements[1]; }

    /// Returns an unmutable reference to the imaginary y-component
    auto y() const -> const Scalar_T& { return m_Elements[2]; }

    /// Returns an unmutable reference to the imaginary z-component
    auto z() const -> const Scalar_T& { return m_Elements[3]; }

    /// Returns a mutable reference to the storage of the quaternion
    auto elements() -> BufferType& { return m_Elements; }

    /// Returns an unmutable reference to the storage of the quaternion
    auto elements() const -> const BufferType& { return m_Elements; }

    /// Returns a pointer to the data of the underlying storage in use
    auto data() -> Scalar_T* { return m_Elements.data(); }

    /// Reeturns a const-pointer to the data of the underlying storage in use
    auto data() const -> const Scalar_T* { return m_Elements.data(); }

    /// Returns a mutable reference to the requested entry of the quaternion
    auto operator[](uint32_t index) -> Scalar_T& { return m_Elements[index]; }

    /// Returns an unmutable reference to the requested entry of the quaternion
    auto operator[](uint32_t index) const -> const Scalar_T& {
        return m_Elements[index];
    }

    /// Returns a printable string-representation of the vector
    auto toString() const -> std::string {
        std::stringstream str_result;
        if (std::is_same<ElementType, float>()) {
            str_result << "Quaternionf(" << w() << ", " << x() << ", " << y()
                       << ", " << z() << ")";
        } else if (std::is_same<ElementType, double>()) {
            str_result << "Quaterniond(" << w() << ", " << x() << ", " << y()
                       << ", " << z() << ")";
        } else {
            str_result << "QuaternionX(" << w() << ", " << x() << ", " << y()
                       << ", " << z() << ")";
        }
        return str_result.str();
    }

    /// Returns the quaternion associated with the given rotation around x-axis
    static auto RotationX(Scalar_T angle) -> Quaternion<Scalar_T>;

    /// Returns the quaternion associated with the given rotation around y-axis
    static auto RotationY(Scalar_T angle) -> Quaternion<Scalar_T>;

    /// Returns the quaternion associated with the given rotation around z-axis
    static auto RotationZ(Scalar_T angle) -> Quaternion<Scalar_T>;

 private:
    /// Storage of the quaternion's entries in   (w, x, y, z) order
    BufferType m_Elements = {1, 0, 0, 0};
};

}  // namespace math
