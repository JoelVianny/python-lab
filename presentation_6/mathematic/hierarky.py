class TransportVehicle:
    def __init__(self, mass, power, wheels):
        self.mass = mass
        self.power = power
        self.wheels = wheels

    def display_info(self):
        return f"Масса: {self.mass} кг, Мощность: {self.power} л.с., Количество колес: {self.wheels}"

class PassengerCar(TransportVehicle):
    def __init__(self, mass, power, wheels, seats):
        super().__init__(mass, power, wheels)
        self.seats = seats

    def display_info(self):
        return super().display_info() + f", Мест для сидения: {self.seats}"

class Bus(TransportVehicle):
    def __init__(self, mass, power, wheels, seats, standing_places, route):
        super().__init__(mass, power, wheels)
        self.seats = seats
        self.standing_places = standing_places
        self.route = route

    def display_info(self):
        base = super().display_info()
        return f"{base}, Сидячих мест: {self.seats}, Стоячих мест: {self.standing_places}, Маршрут: {self.route}"

class CargoTruck(TransportVehicle):
    def __init__(self, mass, power, wheels, cargo_mass):
        super().__init__(mass, power, wheels)
        self.cargo_mass = cargo_mass

    def display_info(self):
        return super().display_info() + f", Масса груза: {self.cargo_mass} кг"

# Создание списка транспортных средств
vehicles = [
    PassengerCar(1500, 120, 4, 5),
    Bus(10000, 300, 6, 40, 50, "Маршрут №101"),
    CargoTruck(8000, 400, 6, 5000)
]

# Вывод информации о каждом транспортном средстве
for vehicle in vehicles:
    print(vehicle.display_info())