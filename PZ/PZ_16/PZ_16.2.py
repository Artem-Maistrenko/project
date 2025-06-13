# Создание базового класса "Транспортное средство" и его наследование для создания
# классов "Автомобиль" и "Мотоцикл". В классе "Транспортное средство" будут
# общие свойства, такие как максимальная скорость и количество колес, а классы
# наследники будут иметь свои уникальные свойства и методы.

class Vehicle:
    def __init__(self, max_speed, wheels):
        self.max_speed = max_speed
        self.wheels = wheels

    def info(self):
        return f"Макс. скорость: {self.max_speed} км/ч, колес: {self.wheels}"


class Car(Vehicle):
    def __init__(self, max_speed, brand, model, fuel_type, wheels=4):
        super().__init__(max_speed, wheels)
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def info(self):
        return f"Автомобиль {self.brand} {self.model}. Топливо: {self.fuel_type}, {super().info()}"


class Motorcycle(Vehicle):
    def __init__(self, max_speed, brand, has_sidecar, wheels=2):
        super().__init__(max_speed, wheels + has_sidecar)
        self.brand = brand
        self.has_sidecar = has_sidecar

    def info(self):
        sidecar = " с коляской" if self.has_sidecar else ""
        return f"Мотоцикл {self.brand}{sidecar}, {super().info()}"


if __name__ == "__main__":
    vehicles = [
        Vehicle(190, 4),
        Car(220, "Hyundai", "Accent", "бензин"),
        Motorcycle(180, "Harley-Davidson", False),
        Motorcycle(150, "Урал", True)
    ]

    for v in vehicles:
        print(v.info())