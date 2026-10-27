from zipfile import sizeEndCentDir

from operations import add, subtract, multiply, divide
from utils import get_user_number, get_operation


while True:
    print("""
    -------------------------------------------------------
    
            Welcome to the Calculator!!!!!!!!!
            
    You will be asked to enter a number, an operation, then
    another number. The result of your operation will then 
    be displayed.
    
    -------------------------------------------------------
    """)
    first_num = get_user_number()
    operation = get_operation()
    second_num = get_user_number()

    if operation == "+":
        result = add(first_num, second_num)
        print(f"Your result is {result}.")
    elif operation == "-":
        result = subtract(first_num, second_num)
        print(f"Your result is {result}.")
    elif operation == "*":
        result = multiply(first_num, second_num)
        print(f"Your result is {result}.")
    else:
        while second_num == 0:
            print("You cannot divide by zero. Retry entering your second number.")
            second_num = get_user_number()
        result = divide(first_num, second_num)
        print(f"Your result is {result}.")