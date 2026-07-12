import sys

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def get_number(prompt):
    """Safely gets a float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def main():
    print("=" * 35)
    print("      CLI CALCULATOR v1.0")
    print("=" * 35)

    operations = {
        '1': ('Addition', add, '+'),
        '2': ('Subtraction', subtract, '-'),
        '3': ('Multiplication', multiply, '*'),
        '4': ('Division', divide, '/')
    }

    while True:
        print("\nAvailable Operations:")
        for key, (name, _, _) in operations.items():
            print(f"  {key}. {name}")
        print("  5. Exit")

        choice = input("\nSelect an option (1-5): ").strip()

        if choice == '5':
            print("\nGoodbye!")
            sys.exit()

        if choice not in operations:
            print("❌ Invalid choice. Please select a number between 1 and 5.")
            continue

        name, func, symbol = operations[choice]
        print(f"\n--- {name} ---")

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result = func(num1, num2)
            # Formatting: drops the .0 if the result is a whole number
            formatted_res = int(result) if result.is_integer() else result
            formatted_num1 = int(num1) if num1.is_integer() else num1
            formatted_num2 = int(num2) if num2.is_integer() else num2

            print("-" * 35)
            print(f"Result: {formatted_num1} {symbol} {formatted_num2} = {formatted_res}")
            print("-" * 35)
        except ZeroDivisionError as e:
            print(f"\n❌ Error: {e}")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
