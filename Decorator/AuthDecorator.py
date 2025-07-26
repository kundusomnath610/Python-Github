def auth_decorator(fun):
    """
    Auth HardCode function username = "Admin" and Password = "password"
    """
    username = input("Enter User name: ") # input
    password = input("Enter Password: ") # input

    def wrapper():
        correct_username = "Admin"
        correct_password = "Admin"

        if (username, password) == (correct_username, correct_password):
            print("Access Authentication")
        else:
            print("Access denied")
    return wrapper

@auth_decorator
def say_hello():
    print("Hello Authentication is secure")
say_hello()