
# Ohm's Law and Power Calculator

import math

# Function to collect valid positive numbers
def get_value(name):
    while True:
        try:
            value = float(input("Enter " + name + ": "))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input! Enter a number.")

# Main calculator function
def calculator():
    while True:
        print("\n=== OHM'S LAW AND POWER CALCULATOR ===")
        print("1. Calculate Voltage")
        print("2. Calculate Current")
        print("3. Calculate Resistance")
        print("4. Calculate Power")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Try again.")
            continue

        targets = {
            "1": "Voltage",
            "2": "Current",
            "3": "Resistance",
            "4": "Power"
        }

        target = targets[choice]

        print("\nChoose the two known values:")
        print("1. Voltage and Current")
        print("2. Voltage and Resistance")
        print("3. Current and Resistance")

        pair = input("Choose a combination: ")

        if pair == "1":
            a = get_value("Voltage (V)")
            b = get_value("Current (A)")

            if choice == "1":
                result = a
            elif choice == "2":
                result = b
            elif choice == "3":
                result = a / b
            else:
                result = a * b

        elif pair == "2":
            a = get_value("Voltage (V)")
            b = get_value("Resistance (Ohms)")

            if choice == "1":
                result = a
            elif choice == "2":
                result = a / b
            elif choice == "3":
                result = b
            else:
                result = (a ** 2) / b

        elif pair == "3":
            a = get_value("Current (A)")
            b = get_value("Resistance (Ohms)")

            if choice == "1":
                result = a * b
            elif choice == "2":
                result = a
            elif choice == "3":
                result = b
            else:
                result = (a ** 2) * b

        else:
            print("Invalid combination!")
            continue

        units = {
            "1": "Volts (V)",
            "2": "Amperes (A)",
            "3": "Ohms",
            "4": "Watts (W)"
        }

        print("\nFormula used: Ohm's Law")
        print(target, "=", round(result, 2), units[choice])

        print("\n1. Calculate again")
        print("2. Exit")

        again = input("Choose: ")

        if again == "2":
            print("Goodbye!")
            break

# Run the calculator
calculator()
