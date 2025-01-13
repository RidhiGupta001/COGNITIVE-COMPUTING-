# Exception Handling with division
def divide_numbers(a, b):
    try:
        result = a / b
        print("Division result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Executing the finally block.")


divide_numbers(10, 2)
divide_numbers(10, 0)

try:
    integer = int(input("Kindly enter the input: "))
    print("You entered:", integer)
except ValueError:
    print("ERROR")
    print("Input should be an integer.")

 
