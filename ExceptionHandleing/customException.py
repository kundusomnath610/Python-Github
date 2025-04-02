class InvalidAge(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAge("Age must be grater 18")
    
try:
    check_age(12)
except InvalidAge as e:
    print("Exception occure detailed are: ", e)