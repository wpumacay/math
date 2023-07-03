from typing import Union, Tuple, List, overload
from numpy import ndarray

################################################################################
#                           Type hints for Vector2                             #
################################################################################

class Vector2:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, x: float): ...
    @overload
    def __init__(self, x: float, y: float): ...
    @overload
    def __init__(self, np_vec: ndarray): ...
    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, value: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, value: float) -> None: ...
    def __add__(self, rhs: Vector2) -> Vector2: ...
    def __sub__(self, rhs: Vector2) -> Vector2: ...
    def __mul__(self, scale: float) -> Vector2: ...
    def __rmul__(self, scale: float) -> Vector2: ...
    def __eq__(self, other: Vector2) -> bool: ...
    def __getitem__(self, index: int) -> float: ...
    def __setitem__(self, index: int, value: float) -> None: ...
    def __neq__(self, other: Vector2) -> bool: ...
    def __neg__(self) -> Vector2: ...
    def dot(self, rhs: Vector2) -> float: ...
    def norm(self) -> float: ...
    def squareNorm(self) -> float: ...
    def normalize(self) -> Vector2: ...
    def normalize_(self) -> None: ...
    def numpy(self) -> ndarray: ...

# Structure should be the same, except for the internal usage of f32 and f64
Vector2f = Vector2
Vector2d = Vector2

################################################################################
#                           Type hints for Vector3                             #
################################################################################

class Vector3:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, x: float): ...
    @overload
    def __init__(self, x: float, y: float): ...
    @overload
    def __init__(self, x: float, y: float, z: float): ...
    @overload
    def __init__(self, np_vec: ndarray): ...
    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, value: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, value: float) -> None: ...
    @property
    def z(self) -> float: ...
    @z.setter
    def z(self, value: float) -> None: ...
    def __add__(self, rhs: Vector3) -> Vector3: ...
    def __sub__(self, rhs: Vector3) -> Vector3: ...
    def __mul__(self, scale: float) -> Vector3: ...
    def __rmul__(self, scale: float) -> Vector3: ...
    def __eq__(self, other: Vector3) -> bool: ...
    def __getitem__(self, index: int) -> float: ...
    def __setitem__(self, index: int, value: float) -> None: ...
    def __neq__(self, other: Vector3) -> bool: ...
    def __neg__(self) -> Vector3: ...
    def cross(self, rhs: Vector3) -> Vector3: ...
    def dot(self, rhs: Vector3) -> float: ...
    def norm(self) -> float: ...
    def squareNorm(self) -> float: ...
    def normalize(self) -> Vector3: ...
    def normalize_(self) -> None: ...
    def numpy(self) -> ndarray: ...

# Structure should be the same, except for the internal usage of f32 and f64
Vector3f = Vector3
Vector3d = Vector3

################################################################################
#                           Type hints for Vector4                             #
################################################################################

class Vector4:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, x: float): ...
    @overload
    def __init__(self, x: float, y: float): ...
    @overload
    def __init__(self, x: float, y: float, z: float): ...
    @overload
    def __init__(self, x: float, y: float, z: float, w: float): ...
    @overload
    def __init__(self, np_vec: ndarray): ...
    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, value: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, value: float) -> None: ...
    @property
    def z(self) -> float: ...
    @z.setter
    def z(self, value: float) -> None: ...
    @property
    def w(self) -> float: ...
    @w.setter
    def w(self, value: float) -> None: ...
    def __add__(self, rhs: Vector4) -> Vector4: ...
    def __sub__(self, rhs: Vector4) -> Vector4: ...
    def __mul__(self, scale: float) -> Vector4: ...
    def __rmul__(self, scale: float) -> Vector4: ...
    def __eq__(self, other: Vector4) -> bool: ...
    def __getitem__(self, index: int) -> float: ...
    def __setitem__(self, index: int, value: float) -> None: ...
    def __neq__(self, other: Vector4) -> bool: ...
    def __neg__(self) -> Vector4: ...
    def dot(self, rhs: Vector4) -> float: ...
    def norm(self) -> float: ...
    def squareNorm(self) -> float: ...
    def normalize(self) -> Vector4: ...
    def normalize_(self) -> None: ...
    def numpy(self) -> ndarray: ...

# Structure should be the same, except for the internal usage of f32 and f64
Vector4f = Vector4
Vector4d = Vector4

################################################################################
#                          Type hints for Quaternion                           #
################################################################################

class Quaternion:
    def __init__(
        self, *args: Union[float, ndarray, List[float]], **kwargs: Union[float, ndarray]
    ): ...
    @property
    def w(self) -> float: ...
    @w.setter
    def w(self, value: float) -> None: ...
    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, value: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, value: float) -> None: ...
    @property
    def z(self) -> float: ...
    @z.setter
    def z(self, value: float) -> None: ...
    def __add__(self, rhs: Quaternion) -> Quaternion: ...
    def __sub__(self, rhs: Quaternion) -> Quaternion: ...
    def __mul__(self, rhs: Union[float, Quaternion]) -> Quaternion: ...
    def __rmul__(self, rhs: Union[float, Quaternion]) -> Quaternion: ...
    def __getitem__(self, index: int) -> float: ...
    def __setitem__(self, index: int, value: float) -> None: ...
    def __eq__(self, other: Quaternion) -> bool: ...
    def __neq__(self, other: Quaternion) -> bool: ...
    def length(self) -> float: ...
    def lengthSquare(self) -> float: ...
    def normalize(self) -> Quaternion: ...
    def normalize_(self) -> None: ...
    def conjugate(self) -> Quaternion: ...
    def inverse(self) -> Quaternion: ...
    def rotate(self, vec: Union[Vector3, ndarray]) -> Vector3: ...
    @staticmethod
    def RotationX(angle: float) -> Quaternion: ...
    @staticmethod
    def RotationY(angle: float) -> Quaternion: ...
    @staticmethod
    def RotationZ(angle: float) -> Quaternion: ...

# Structure should be the same, except for the internal usage of f32 and f64
Quaternionf = Quaternion
Quaterniond = Quaternion

################################################################################
#                            Type hints for Matrix2                            #
################################################################################

class Matrix2:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, d0: float, d1: float): ...
    @overload
    def __init__(self, m00: float, m01: float, m10: float, m11: float): ...
    @overload
    def __init__(self, col0: Vector2, col1: Vector2): ...
    @overload
    def __init__(self, np_mat: ndarray): ...
    @overload
    def __getitem__(self, index: int) -> Vector2: ...
    @overload
    def __getitem__(self, accessor: Tuple[int, int]) -> float: ...
    @overload
    def __setitem__(self, index: int, value: ndarray) -> None: ...
    @overload
    def __setitem__(self, accessor: Tuple[int, int], value: float) -> None: ...
    def __add__(self, rhs: Matrix2) -> Matrix2: ...
    def __sub__(self, rhs: Matrix2) -> Matrix2: ...
    @overload
    def __mul__(self, rhs: float) -> Matrix2: ...
    @overload
    def __mul__(self, rhs: Vector2) -> Vector2: ...
    @overload
    def __mul__(self, rhs: Matrix2) -> Matrix2: ...
    @overload
    def __rmul__(self, rhs: float) -> Matrix2: ...
    @overload
    def __rmul__(self, rhs: Matrix2) -> Matrix2: ...
    def __eq__(self, other: Matrix2) -> bool: ...
    def __neq__(self, other: Matrix2) -> bool: ...
    @property
    def T(self) -> Matrix2: ...
    def flatten(self) -> ndarray: ...
    def transpose(self) -> Matrix2: ...
    def inverse(self) -> Matrix2: ...
    def trace(self) -> float: ...
    def determinant(self) -> float: ...
    @staticmethod
    def Rotation(angle: float) -> Matrix2: ...
    @staticmethod
    @overload
    def Scale(scale_x: float, scale_y: float) -> Matrix2: ...
    @staticmethod
    @overload
    def Scale(scales: Vector2) -> Matrix2: ...
    @staticmethod
    def Identity() -> Matrix2: ...
    @staticmethod
    def Zeros() -> Matrix2: ...

# Structure should be the same, except for the internal usage of f32 and f64
Matrix2f = Matrix2
Matrix2d = Matrix2

################################################################################
#                            Type hints for Matrix3                            #
################################################################################

class Matrix3:
    def __init__(
        self,
        *args: Union[float, ndarray, Vector3],
        **kwargs: Union[float, ndarray, Vector3]
    ): ...
    @overload
    def __getitem__(self, index: int) -> Vector3: ...
    @overload
    def __getitem__(self, accessor: Tuple[int, int]) -> float: ...
    @overload
    def __setitem__(self, index: int, value: ndarray) -> None: ...
    @overload
    def __setitem__(self, accessor: Tuple[int, int], value: float) -> None: ...
    def __add__(self, rhs: Matrix3) -> Matrix3: ...
    def __sub__(self, rhs: Matrix3) -> Matrix3: ...
    @overload
    def __mul__(self, rhs: float) -> Matrix3: ...
    @overload
    def __mul__(self, rhs: Vector3) -> Vector3: ...
    @overload
    def __mul__(self, rhs: Matrix3) -> Matrix3: ...
    @overload
    def __rmul__(self, rhs: float) -> Matrix3: ...
    @overload
    def __rmul__(self, rhs: Matrix3) -> Matrix3: ...
    def __eq__(self, other: Matrix3) -> bool: ...
    def __neq__(self, other: Matrix3) -> bool: ...
    @property
    def T(self) -> Matrix3: ...
    def flatten(self) -> ndarray: ...
    def transpose(self) -> Matrix3: ...
    def inverse(self) -> Matrix3: ...
    def trace(self) -> float: ...
    def determinant(self) -> float: ...
    @staticmethod
    def RotationX(angle: float) -> Matrix3: ...
    @staticmethod
    def RotationY(angle: float) -> Matrix3: ...
    @staticmethod
    def RotationZ(angle: float) -> Matrix3: ...
    @staticmethod
    @overload
    def Scale(scale_x: float, scale_y: float, scale_z: float) -> Matrix3: ...
    @staticmethod
    @overload
    def Scale(scales: ndarray) -> Matrix3: ...
    @staticmethod
    def Identity() -> Matrix3: ...
    @staticmethod
    def Zeros() -> Matrix3: ...

# Structure should be the same, except for the internal usage of f32 and f64
Matrix3f = Matrix3
Matrix3d = Matrix3

################################################################################
#                            Type hints for Matrix4                            #
################################################################################

class Matrix4:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, d0: float, d1: float, d2: float, d3: float): ...
    @overload
    def __init__(
        self,
        m00: float,
        m01: float,
        m02: float,
        m03: float,
        m10: float,
        m11: float,
        m12: float,
        m13: float,
        m20: float,
        m21: float,
        m22: float,
        m23: float,
        m30: float,
        m31: float,
        m32: float,
        m33: float,
    ): ...
    @overload
    def __init__(self, col0: Vector4, col1: Vector4, col2: Vector4, col3: Vector4): ...
    @overload
    def __init__(self, np_mat: ndarray): ...
    @overload
    def __getitem__(self, index: int) -> Vector4: ...
    @overload
    def __getitem__(self, accessor: Tuple[int, int]) -> float: ...
    @overload
    def __setitem__(self, index: int, value: ndarray) -> None: ...
    @overload
    def __setitem__(self, accessor: Tuple[int, int], value: float) -> None: ...
    def __add__(self, rhs: Matrix4) -> Matrix4: ...
    def __sub__(self, rhs: Matrix4) -> Matrix4: ...
    @overload
    def __mul__(self, rhs: float) -> Matrix4: ...
    @overload
    def __mul__(self, rhs: Vector4) -> Vector4: ...
    @overload
    def __mul__(self, rhs: Matrix4) -> Matrix4: ...
    @overload
    def __rmul__(self, rhs: float) -> Matrix4: ...
    @overload
    def __rmul__(self, rhs: Matrix4) -> Matrix4: ...
    def __eq__(self, other: Matrix4) -> bool: ...
    def __neq__(self, other: Matrix4) -> bool: ...
    @property
    def T(self) -> Matrix4: ...
    def flatten(self) -> ndarray: ...
    def transpose(self) -> Matrix4: ...
    def inverse(self) -> Matrix4: ...
    def trace(self) -> float: ...
    def determinant(self) -> float: ...
    @staticmethod
    def RotationX(angle: float) -> Matrix4: ...
    @staticmethod
    def RotationY(angle: float) -> Matrix4: ...
    @staticmethod
    def RotationZ(angle: float) -> Matrix4: ...
    @staticmethod
    @overload
    def Scale(scale_x: float, scale_y: float, scale_z: float) -> Matrix4: ...
    @staticmethod
    @overload
    def Scale(scales: ndarray) -> Matrix4: ...
    @staticmethod
    def Identity() -> Matrix4: ...
    @staticmethod
    def Zeros() -> Matrix4: ...

# Structure should be the same, except for the internal usage of f32 and f64
Matrix4f = Matrix4
Matrix4d = Matrix4

################################################################################
#                             Type hints for Pose3d                            #
################################################################################

class Pose3d:
    position: Vector3
    orientation: Quaternion

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, position: Vector3, orientation: Quaternion): ...
    @overload
    def __init__(self, position: Vector3, orientation: Matrix3): ...
    @overload
    def apply(self, vec: Vector3) -> Vector3: ...
    @overload
    def apply(self, vec_np: ndarray) -> ndarray: ...
    def inverse(self) -> Pose3d: ...
    def toMatrix(self) -> Matrix4: ...
    @overload
    def __mul__(self, vec: Vector3) -> Vector3: ...
    @overload
    def __mul__(self, vec_np: ndarray) -> ndarray: ...
    @overload
    def __mul__(self, rhs: Pose3d) -> Pose3d: ...

# Structure should be the same, except for the internal usage of f32 and f64
Pose3d_f = Pose3d
Pose3d_d = Pose3d

################################################################################
#                       Type hints for conversions helpers                     #
################################################################################

def vec2_to_nparray_f32(vec: Vector2f) -> ndarray: ...
def vec2_to_nparray_f64(vec: Vector2d) -> ndarray: ...
def vec3_to_nparray_f32(vec: Vector3f) -> ndarray: ...
def vec3_to_nparray_f64(vec: Vector3d) -> ndarray: ...
def vec4_to_nparray_f32(vec: Vector4f) -> ndarray: ...
def vec4_to_nparray_f64(vec: Vector4d) -> ndarray: ...
def mat2_to_nparray_f32(mat: Matrix2f) -> ndarray: ...
def mat2_to_nparray_f64(mat: Matrix2d) -> ndarray: ...
def mat3_to_nparray_f32(mat: Matrix3f) -> ndarray: ...
def mat3_to_nparray_f64(mat: Matrix3d) -> ndarray: ...
def mat4_to_nparray_f32(mat: Matrix4f) -> ndarray: ...
def mat4_to_nparray_f64(mat: Matrix4d) -> ndarray: ...
def nparray_to_vec2_f32(array_np: ndarray) -> Vector2f: ...
def nparray_to_vec2_f64(array_np: ndarray) -> Vector2d: ...
def nparray_to_vec3_f32(array_np: ndarray) -> Vector3f: ...
def nparray_to_vec3_f64(array_np: ndarray) -> Vector3d: ...
def nparray_to_vec4_f32(array_np: ndarray) -> Vector4f: ...
def nparray_to_vec4_f64(array_np: ndarray) -> Vector4d: ...
def nparray_to_mat2_f32(array_np: ndarray) -> Matrix2f: ...
def nparray_to_mat2_f64(array_np: ndarray) -> Matrix2d: ...
def nparray_to_mat3_f32(array_np: ndarray) -> Matrix3f: ...
def nparray_to_mat3_f64(array_np: ndarray) -> Matrix3d: ...
def nparray_to_mat4_f32(array_np: ndarray) -> Matrix4f: ...
def nparray_to_mat4_f64(array_np: ndarray) -> Matrix4d: ...
