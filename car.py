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
        self.gasmileage = gasMileage
        self.carmileage = carMileage

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
        self.gasLevel -= distance / self.gasmileage
        self.carmileage += distance
        print(f"Remaining gas level: {self.gasLevel:.2f}")

    def fillgas(self, gas):
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
        if self.gasmileage <= 20:
            self.gasmileage *= 2
            print(f"Upgraded gas mileage to {self.gasmileage} miles per gallon.")
        else:
            print("No upgrade needed. Mileage is already better than or equal to 20 mpg.")


# Create an instance of the Car class
car1 = Car("Toyota", "CHR", 1968, "Black", 20000, 0.75, 15, 25, 2000)

# Simple menu for interacting with the car
inn = input("Please select what you would like to do:\n1) Drive\n2) Fill Gas\n3) Upgrade\n")

if inn == "1":
    # Drive the car
    distance = float(input("How many miles would you like to drive? "))
    car1.drive(distance)

elif inn == "2":
    # Fill gas
    gas_amount = float(input("How many gallons of gas would you like to add? "))
    car1.fillgas(gas_amount)

elif inn == "3":
    # Upgrade the car
    car1.upgrade()

else:
    print("Invalid option. Please choose 1, 2, or 3.")
