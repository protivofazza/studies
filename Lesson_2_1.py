class Vehicle:
    country_of_registration = 'Ukraine'

    def __init__(self, model, vin, maximum_mass):
        self.model = model
        self.vin = vin
        self.maximum_mass = maximum_mass

    def set_model(self, type_vehicle):
        self.model = type_vehicle

    def set_vin(self, id_number):
        self.vin = id_number

    def set_maximum_mass(self, mass):
        self.maximum_mass = mass


class Truck(Vehicle):
    def __init__(self, model, vin, maximum_mass, lift_capacity):
        self.model = model
        self.vin = vin
        self.maximum_mass = maximum_mass
        self.lift_capacity = lift_capacity


class Car(Vehicle):
    def set_seats(self, value):
        self.number_of_seats = value
