class Vehicle:
    def __init__(self, brand, year, capacity):
        self.brand = brand
        self.year = year
        self.capacity = capacity

    def info(self):
        print(self.brand, self.year, self.capacity)


class Car(Vehicle):
    def __init__(self, brand, year, capacity, doors):   
        super().__init__(brand, year, capacity)       
        self.doors = doors

    def info(self):
        print(self.brand, self.year, self.capacity, self.doors)


class Motorcycle(Vehicle):
    def __init__(self, brand, year, capacity, type_motor):  
        super().__init__(brand, year, capacity)
        self.type_motor = type_motor

    def info(self):
        print("Motorcycle:", self.brand, "year:", self.year, 
              "capacity:", self.capacity, "type:", self.type_motor)


# Pemanggilan object
x = Car("GTR", "2020", "2 seats", "2")
x.info()

y = Motorcycle("Yamaha", "2022", "2 seats", "Sport")
y.info()
