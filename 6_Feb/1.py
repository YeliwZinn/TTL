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

