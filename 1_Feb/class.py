class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def show(self):
        print(self.make.__str__()+self.model.__str__()+self.year.__str__())
        

    def __add__(self, other):
        if isinstance(other, Vehicle):
            combined_make_model = f"{self.make} {self.model} + {other.make} {other.model}"
            return combined_make_model
        else:
            raise ValueError("Error")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, fuel_type):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def show(self):
        super().show()
        print(f"Doors: {self.num_doors}, Fuel Type: {self.fuel_type}")



vehicle1 = Vehicle("Mahindra", "Scorpio", 2022)
vehicle2 = Vehicle("Ford", "Endeavour", 2024)

print("Information for Vehicle 1:")
vehicle1.show()
repr(vehicle1)

print("\nInformation for Vehicle 2:")
vehicle2.show()
print(repr(vehicle2))

combined_make_model = vehicle1 + vehicle2
print("\nCombined Make and Model:", combined_make_model)

car1 = Car("Ford", "Mustang", 2024, 2, "Gasoline")
car2 = Car("Tesla", "Model S", 2025, 4, "Electric")

print("\nInformation for Car 1:")
car1.show()
repr(car1)

print("\nInformation for Car 2:")
car2.show()
print(repr(car2))
