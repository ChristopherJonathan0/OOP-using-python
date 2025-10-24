class Vehicle:
    def __init__(self, id, speed, battery):
        self.id = id
        self.speed = speed
        self.battery = battery
    def move():
        pass
    def refuel():
        pass
    def status(self):
        print("id:", self.id, 
              "speed:", self.speed, 
              "battery:", self.battery)

class ElectricCar(Vehicle):
    def __init__(self, id, speed, battery, passenger_capacity):
        self.id = id
        self.speed = speed
        self.battery = battery
        self.passenger_capacity = passenger_capacity
    def move(self):
        print(f"Mobil listrik melaju dengan kecepatan {self.speed} km/jam")
    def refuel(self):
        self.battery = 100

class AutonomousBike(Vehicle):
    def __init__(self, id, speed, battery, passenger_capacity, balance_mode):
        self.id = id
        self.speed = speed
        self.battery = battery
        self.passenger_capacity = passenger_capacity
        self.balance_mode = balance_mode
    def move(self):
        print("Motor otonom bergerak dengan stabilitas otomatis.")
    def refuel(self):
        self.battery = min(self.battery + 50, 100)
        print("Motor otonom bergerak dengan stabilitas otomatis.", end=" ")
        if self.balance_mode == True:
            print("Mode keseimbangan aktif")
        elif self.balance_mode == False:
            print("Mode keseimbangan tidak aktif")

class SmartBus(Vehicle):
    def __init__(self, id, speed, battery, passenger_capacity, balance_mode, route):
        self.id = id
        self.speed = speed
        self.battery = battery
        self.passenger_capacity = passenger_capacity
        self.balance_mode = balance_mode
        self.route = route
    def move(self):
        print(f"Bus pintar berjalan di rute {self.route}.")
    def refuel(self):
        self.battery = min(self.battery + 30, 100)
        if self.balance_mode == True:
            print("Mode keseimbangan aktif")
        elif self.balance_mode == False:
            print("Mode keseimbangan tidak aktif")
    def announce_stop(self, stop):
        print(f"Berhenti di {stop}.")

class FleetManager:
    def __init__(self):
        self.vehicles = []  

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def status_report(self):
        print("=== Status Armada ===")
        for v in self.vehicles:
            print(f"ID: {v.id} | Speed: {v.speed} | Battery: {v.battery}%")



car = ElectricCar("VH001", 80, 100, 4)
bike = AutonomousBike("VH002", 60, 90, 2, True)
bus = SmartBus("VH003", 40, 70, 20, False,["Terminal A", "Terminal B", "Terminal C"])


fleet = FleetManager()
fleet.add_vehicle(car)
fleet.add_vehicle(bike)
fleet.add_vehicle(bus)


car.move()
bike.move()
bus.move()
bus.announce_stop("Terminal B")


fleet.status_report()