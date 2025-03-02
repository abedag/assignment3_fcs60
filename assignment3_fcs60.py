print("Bob's Car Rental Service")

# lass for vehicle which is a parent class

class Vehicle:
    # Function for instance attributes and provided parameters 
    def __init__(self, brand, model, year, daily_rental_price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__daily_rental_price = daily_rental_price

    # Function for displaying vehicle's info
    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}, Year: {self.year}, Daily Rental Price: {self.__daily_rental_price}$")

    # Function for calculating rental cost per day 
    def calculate_rental_cost(self, days):
        return self.__daily_rental_price * days
    
    # Function for getting vehicle rental price
    def get_rental_price(self):
        return self.__daily_rental_price
    
    # Function for setting vehicle rental price
    def set_rental_price(self, final_price):
        self.__daily_rental_price = final_price


# Class for car which inherits from vehicle class

class Car(Vehicle):
    # Function for instance attributes (inherited from vehicle attributes)
    def __init__(self, brand, model, year, seating_capacity, daily_rental_price):
        super().__init__(brand, model, year, daily_rental_price)
        self.seating_capacity = seating_capacity

    # Function for displaying car's info
    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity} Daily Rental Price: {self.get_rental_price()}$")


# Class for bike which inherits from vehicle class

class Bike(Vehicle):
    # Function for instance attributes (inherited from vehicle attributes)
    def __init__(self, brand, model, year, engine_capacity, daily_rental_price):
        super().__init__(brand, model, year, daily_rental_price)
        self.engine_capacity = engine_capacity

    # Function for displaying bike's info
    def display_info(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine Capacity: {self.engine_capacity}, Daily Rental Price: {self.get_rental_price()}$")

# Function for showing vehicle's info
def show_vehicle_info(vehicle):
    vehicle.display_info()


c = Car("BMW", "M5 CS", 2024, 5, 100)
b = Bike("BMW", "S1000RR", 2022, "999cc", 50)

show_vehicle_info(c)
show_vehicle_info(b)

c_rental_cost = c.calculate_rental_cost(15)
b_rental_cost = b.calculate_rental_cost(30)

print(f"Rental cost for {c.brand} {c.model} for 15 days: {c_rental_cost}$")  
print(f"Rental cost for {b.brand} {b.model} for 30 days: {b_rental_cost}$")

c.set_rental_price(120)
c_new_rent = c.get_rental_price()

print(f"The updated daily rental cost is {c_new_rent}$")