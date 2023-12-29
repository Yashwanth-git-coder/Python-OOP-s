class Car:

    def __init__(self, make, model, year):
        # Initialize attributes to describe a car
        self.make = make
        self.model = model
        self.year = year
        # Set a default value for the odometer reading
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # Return a neatly formatted descriptive name
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        # Print a statement showing the car's mileage
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        # Set the odometer reading to a given value
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        # Add the given amount to the odometer reading
        self.odometer_reading += miles


# Create an instance of Car
my_car = Car('Lambo', 'a4', '2024')
print(my_car.get_descriptive_name())  # Print the car's descriptive name

# Update the odometer reading for my_car
my_car.update_odometer(24)
my_car.read_odometer()  # Print my_car's mileage


# Create another instance of Car
my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())  # Print the used car's descriptive name

# Update the odometer reading for my_used_car
my_used_car.update_odometer(23500)
my_used_car.read_odometer()  # Print my_used_car's mileage

# Increment the odometer reading for my_used_car
my_used_car.increment_odometer(100)
my_used_car.read_odometer()  # Print my_used_car's updated mileage
