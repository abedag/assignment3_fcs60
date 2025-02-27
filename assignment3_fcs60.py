print("Bob's Car Rental Service")

class Vehicle:
    def __init__(self, brand, model, year, daily_rental_price):
        self.brand = brand
        self.model = model
        self.year = year
        self._daily_rental_price = daily_rental_price

    
    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}, Year: {self.year}, Daily Rental Price: {self._daily_rental_price}")

    def calculate_rental_cost(self, days):
        return self._daily_rental_price * days
    
    def get_rental_price(self):
        return self._daily_rental_price
    
    def set_rental_price(self, final_price):
        self._daily_rental_price = final_price


class Car(Vehicle):
    def __init__(self, brand, model, year, seating_capacity, daily_rental_price):
        Vehicle.__init__(self ,brand, model, year, daily_rental_price)
        self.seating_capacity = seating_capacity

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity} Daily Rental Price: {self._daily_rental_price}")


class Bike(Vehicle):
    def __init__(self, brand, model, year, engine_capacity, daily_rental_price):
        Vehicle.__init__(self, brand, model, year, daily_rental_price)
        self.engine_capacity = engine_capacity

    def display_info(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Seats: {self.engine_capacity} Daily Rental Price: {self._daily_rental_price}")

def show_vehicle_info(vehicle):
    vehicle.display_info()


c = Car("BMW", "M5 CS", 2024, 5, 100)
b = Bike("BMW", "S1000RR", 2022, "999cc", 50)

show_vehicle_info(c)
show_vehicle_info(b)

c_rental_cost = c.calculate_rental_cost(15)
b_rental_cost = b.calculate_rental_cost(30)

print(f"Rental cost for {c.brand} {c.model} for 15 days: ${c_rental_cost}")  
print(f"Rental cost for {b.brand} {b.model} for 30 days: ${b_rental_cost}")

