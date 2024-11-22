class Car:
    def __init__(self, brand, model, year, color, price, gasLevel, gasTankSize, gasMileage, carMileage):
        """
        Initializes a new car instance.

        Args:
            brand (str): The brand of the car.
            model (str): The model of the car.
            year (int): The manufacturing year of the car.
            color (str): The color of the car.
            price (float): The price of the car.
            gasLevel (float): The current level of gas in the car's tank.
            gasTankSize (float): The total size of the car's gas tank.
            gasMileage (float): The fuel efficiency of the car.
            carMileage (float): The total mileage of the car.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.gasLevel = gasLevel
        self.gasTankSize = gasTankSize
        self.gasMileage = gasMileage
        self.carMileage = carMileage


    def drive(self, distance):
        """
        Simulates driving the car a certain distance, decreasing the gas level based on mileage.

        Args:
            distance (float): The distance to drive in miles.

        Updates:
            The gas level is decreased based on the car's mileage.
            The car's total mileage is updated.
        """
        print(f"Driving {self.brand} {self.model} ({self.year}) for {distance} miles.")
        self.gasLevel -= distance / self.gasMileage
        self.carMileage += distance
        print(f"Remaining gas level: {self.gasLevel:.2f}")


    def fillGas(self, gas):
        """
        Fills the car's gas tank by a specified amount.

        Args:
            gas (float): The amount of gas to add to the tank.
        """
        self.gasLevel = min(self.gasLevel + gas, self.gasTankSize)  # Ensure gas level doesn't exceed tank size
        print(f"Gas level after filling: {self.gasLevel:.2f}")


    def upgrade(self):
        """
        Upgrades the car's gas mileage if it's less than or equal to 20 miles per gallon.
        Doubles the gas mileage if the condition is met.
        """
        if self.gasMileage <= 20:
            self.gasMileage *= 2
            print(f"Upgraded gas mileage to {self.gasMileage} miles per gallon.")
        else:
            print("No upgrade needed. Mileage is already better than or equal to 20 mpg.")


