# Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления
# площади, длины окружности и диаметра.
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return 2 * self.radius

if __name__ == "__main__":
    circle = Circle(5)

    print(f"Радиус круга: {circle.radius}")
    print(f"Площадь круга: {circle.area():.2f}")
    print(f"Длина окружности: {circle.circumference():.2f}")
    print(f"Диаметр круга: {circle.diameter():.2f}")