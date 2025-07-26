import time

def time(func):
    def wrapper(*args , **kargs):
        func()