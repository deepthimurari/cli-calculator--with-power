# Calculator using dictionary mapping

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "Error! Division by zero." if b == 0 else a / b
def power(a,b):
    return a ** b


# Mapping operations to functions
operations = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
    "5": ("power", power)
}


def calculator():
    while True:
        print("\n===== CLI Calculator =====")

        # Display menu dynamically
        for key, value in operations.items():
            print(f"{key}. {value[0]}")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "6":
            print("Exiting...")
            break

        if choice in operations:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                operation_name, function = operations[choice]
                result = function(num1, num2)

                print(f"{operation_name} Result: {result}")

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        else:
            print("Invalid choice! Try again.")


# Run the calculator
calculator()