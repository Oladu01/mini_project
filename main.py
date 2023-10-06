import sys

if len(sys.argv) != 3:
    print("Usage: python main.py <number1> <number2>")
else:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        result = a + b
        print(f"The sum of {a} and {b} is: {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
