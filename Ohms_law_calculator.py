
# Ohm's Law and Power Calculator
# Author: Segun
# ND1 Mechatronics Engineering, YabaTech

# Function to collect valid positive numbers
def get_value(name, unit):
    while True:
        try:
            value = float(input(f"Enter {name} ({unit}): "))

            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value

        except ValueError:
            print("Invalid input! Please enter a number.")


# Function to perform calculations
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

        elif choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Try again.")
            continue

        # Display valid input combinations
        pairs = {
            "1": [
                ("Current", "Resistance"),
                ("Power", "Current"),
                ("Power", "Resistance")
            ],
            "2": [
                ("Voltage", "Resistance"),
                ("Power", "Voltage"),
                ("Power", "Resistance")
            ],
            "3": [
                ("Voltage", "Current"),
                ("Voltage", "Power"),
                ("Power", "Current")
            ],
            "4": [
                ("Voltage", "Current"),
                ("Voltage", "Resistance"),
                ("Current", "Resistance")
            ]
        }

        targets = {
            "1": "Voltage",
            "2": "Current",
            "3": "Resistance",
            "4": "Power"
        }

        target = targets[choice]

        print("\nChoose the two known values:")

        for i, pair in enumerate(pairs[choice], 1):
            print(f"{i}. {pair[0]} and {pair[1]}")

        option = input("Choose a combination: ")

        if option not in ["1", "2", "3"]:
            print("Invalid combination!")
            continue

        first, second = pairs[choice][int(option) - 1]

        # Collect the two known values
        units = {
            "Voltage": "V",
            "Current": "A",
            "Resistance": "ohms",
            "Power": "W"
        }

        a = get_value(first, units[first])
        b = get_value(second, units[second])

        # Perform the correct calculation
        if target == "Voltage":
            if first == "Current":
                result = a * b
            elif second == "Current":
                result = a / b
            else:
                result = (a * b) ** 0.5

        elif target == "Current":
            if first == "Voltage":
                result = a / b
            elif second == "Voltage":
                result = a / b
            else:
                result = (a / b) ** 0.5

        elif target == "Resistance":
            if first == "Voltage" and second == "Current":
                result = a / b
            elif first == "Voltage":
                result = (a ** 2) / b
            else:
                result = a / (b ** 2)

        else:
            if first == "Voltage" and second == "Current":
                result = a * b
            elif first == "Voltage":
                result = (a ** 2) / b
            else:
                result = (a ** 2) * b

        # Display result
        print("\n===== CALCULATION RESULT =====")
        print(f"Formula: {target}")
        print(f"{target} = {result:.2f} {units[target]}")

        # Extra feature: Repeat calculation
        print("\n1. Calculate again")
        print("2. Exit")

        again = input("Choose an option: ")

        if again == "2":
            print("Thank you for using the calculator!")
            break


# Run the program
if __name__ == "__main__":
    calculator()

