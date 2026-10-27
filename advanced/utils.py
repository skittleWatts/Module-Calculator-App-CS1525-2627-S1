def get_user_number() -> int:
    """
    Retrieves an integer from the user for operations.
    :return: The user's input as an integer.
    """
    while True:
        try:
            user_number = int(input("Please enter your chosen integer: "))
            break
        except ValueError:
            print("Please enter a valid integer input!")
    return user_number

def get_operation() -> str:
    """
    Gets an operation (+, -, *, or /) from the user.
    :return: The operation as a string.
    """
    valid_inputs = ["/", "*", "-", "+"]
    while True:
        user_operation = input("Please choose your operation (+, -, *, or /): ")
        if user_operation in valid_inputs:
            break
        else:
            print("Please choose +, -, *, or /.")
    return user_operation