print("Bob's Car Rental Service")

class Vehicle:
    def __init__(self, brand, model, year, daily_rental_price):
        self.brand = brand
        self.model = model
        self.year = year
        self._daily_rental_price = daily_rental_price

    
