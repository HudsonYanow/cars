from car import Car
import BL

# Create an instance of the Car class
car1 = Car("Toyota", "CHR", 1968, "Black", 20000, 0.75, 15, 25, 2000)
active=True
while active:
    # Simple menu for interacting with the car
    userInput = input("""Please select what you would like to do:
                    1)Drive
                    2) Fill Gas
                    3)Upgrade car
                    4)exit""")

    if userInput == "1":
        # Drive the car
        distance=BL.floatInputValidator("How many miles would you like to drive? ","please only use numbers.\nHow many miles would you like to drive? ")
        car1.drive(distance)

    elif userInput == "2":
        # Fill gas
        gas_amount=BL.floatInputValidator("How many gallons of gas would you like to add? ", "please only use numbers.\nHow many gallons of gas would you like to add? ")
        car1.fillGas(gas_amount)

    elif userInput == "3":
        # Upgrade the car
        car1.upgrade()
    elif userInput == "4":
        #exits the program
        active=False
    else:
        print("Invalid option. Please choose 1, 2, or 3.")

