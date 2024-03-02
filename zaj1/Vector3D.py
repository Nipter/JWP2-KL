import math

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    def __str__(self) -> str:
        return f"Vector3D({self.__x}, {self.__y}, {self.__z})"

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, z):
        self.__z = z

    def norm(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2 + self.__z ** 2)

    def __add__(self, other):
        return Vector3D(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    def __sub__(self, other):
        return Vector3D(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)

    def __mul__(self, scalar):
        return Vector3D(self.__x * scalar, self.__y * scalar, self.__z * scalar)

    def dot(self, other):
        return Vector3D(self.__x * other.__x, self.__y * other.__y, self.__z * other.__z)

    def cross(self, other):
        c_x = self.__y * other.__z - self.__z * other.__y
        c_y = self.__z * other.__x - self.__z * other.__z
        c_z = self.__x * other.__y - self.__z * other.__x
        return Vector3D(c_x, c_y, c_z)

    def are_orthogonal(self, other):
        return self.dot(other) == 0


def main():
    vector = Vector3D(1, 2, 3)
    print("Vector: ", vector)
    print("Norm: ", vector.norm())
    print("Add: ", vector + Vector3D(1, 2, 3))
    print("Sub: ", vector - Vector3D(1, 2, 3))
    print("Mul: ", vector.__mul__(3))
    print("Dot: ", vector.dot(Vector3D(2, 2, 2)))
    print("Cross: ", vector.cross(Vector3D(1, 2, 3)))
    print("Are orthogonal: ", vector.are_orthogonal(Vector3D(1, 2, 3)))


if __name__ == "__main__":
    main()
