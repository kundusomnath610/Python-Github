def auth_decorator(fun):
    def wrapper():
        correct_useename = "Admin"
        correct_password = "password"

        username = "Admin"
        password = "password"

        if (username, password) == (correct_useename, correct_password):
            print("Access Authentication")
            func()
        else:
            print("Access denied")
    return wrapper

@auth_decorator
def say_hello():
    print("Hello Authentication is secure")
say_hello()