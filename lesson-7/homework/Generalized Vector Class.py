import math

class Vector:
    def __init__(self, *components):
        self.components = components

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, Vector):  # Dot product
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimension")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):  # Scalar multiplication
            return Vector(*(a * other for a in self.components))

    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*(x / mag for x in self.components))

# Example usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)
print(v1 + v2)
print(v2 - v1)
print(v1 * v2)
print(v1 * 3)
print(v1.magnitude())
print(v1.normalize())
