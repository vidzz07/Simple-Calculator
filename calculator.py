def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

def main():
    print("Welcome to the Simple Calculator!")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter the number of the operation (1/2/3/4): ")
    
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        return

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if choice == '1':
        result = add(num1, num2)
        op = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        op = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        op = '*'
    elif choice == '4':
        result = divide(num1, num2)
        op = '/'

    print(f"Result: {num1} {op} {num2} = {result}")

if __name__ == "__main__":
    main()
