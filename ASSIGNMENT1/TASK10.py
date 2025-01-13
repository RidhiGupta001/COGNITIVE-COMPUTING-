import sys
if len(sys.argv) != 3:
    print("Usage: python program_name.py <number1> <number2>")
    sys.exit(1)
try:
    number1 = float(sys.argv[1])
    number2 = float(sys.argv[2])
    result = number1 + number2
    print(f"The sum of {number1} and {number2} is {result}")

except ValueError:
    print("Please enter valid numbers.")
    sys.exit(1)
