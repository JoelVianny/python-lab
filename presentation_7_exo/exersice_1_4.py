"""Перепишите иерархию классов транспортных
средств выделив протокол, так чтобы каждый класс
конкретного транспортного средства реализовывал
его.
3. Для класса дробей реализуйте перегруженные
операции + и *.
4. Реализуйте операцию деления длины в английской
системе мер на части. Выбрасывайте исключение,
при попытке деления на ноль."""

from typing import Protocol

class TransportProtocol(Protocol):
    def display_info(self) -> str:
        ...

class PassengerCar:
    def __init__(self, mass, power, wheels, seats):
        self.mass = mass
        self.power = power
        self.wheels = wheels
        self.seats = seats

    def display_info(self) -> str:
        return f"Масса: {self.mass} кг, Мощность: {self.power} л.с., Количество колес: {self.wheels}, Мест для сидения: {self.seats}"

class Bus:
    def __init__(self, mass, power, wheels, seats, standing_places, route):
        self.mass = mass
        self.power = power
        self.wheels = wheels
        self.seats = seats
        self.standing_places = standing_places
        self.route = route

    def display_info(self) -> str:
        return f"Масса: {self.mass} кг, Мощность: {self.power} л.с., Количество колес: {self.wheels}, Сидячих мест: {self.seats}, Стоячих мест: {self.standing_places}, Маршрут: {self.route}"

class CargoTruck:
    def __init__(self, mass, power, wheels, cargo_mass):
        self.mass = mass
        self.power = power
        self.wheels = wheels
        self.cargo_mass = cargo_mass

    def display_info(self) -> str:
        return f"Масса: {self.mass} кг, Мощность: {self.power} л.с., Количество колес: {self.wheels}, Масса груза: {self.cargo_mass} кг"

vehicles: list[TransportProtocol] = [
    PassengerCar(1500, 120, 4, 5),
    Bus(10000, 300, 6, 40, 50, "Маршрут №101"),
    CargoTruck(8000, 400, 6, 5000)
]

for vehicle in vehicles:
    print(vehicle.display_info())


# --- 3. Класс дробей с перегруженными операциями ---
class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю.")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def _simplify(self) -> None:
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __add__(self, other: "Fraction") -> "Fraction":
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other: "Fraction") -> "Fraction":
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"
    # --- 4. Класс Length для английской системы мер ---
class Length:
    def __init__(self, feet: int, inches: int) -> None:
        if inches >= 12:
            raise ValueError("Дюймы должны быть меньше 12.")
        self.feet = feet
        self.inches = inches

    def __truediv__(self, parts: int) -> "Length":
        if parts == 0:
            raise ZeroDivisionError("Нельзя делить на ноль!")
        total_inches = self.feet * 12 + self.inches
        new_inches = total_inches // parts
        return Length(new_inches // 12, new_inches % 12)

    def __str__(self) -> str:
        return f"{self.feet} футов {self.inches} дюймов"