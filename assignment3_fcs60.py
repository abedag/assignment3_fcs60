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

class Car(Vehicle):
    def __init__(self, brand, model, year, daily_rental_price, seating_capacity):
        Vehicle.__init__(brand, model, year, daily_rental_price)
        self.seating_capacity = seating_capacity

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity} Daily Rental Price: {self._daily_rental_price}")


