# Decorator function
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

# Applying the decorator
@my_decorator
def greet():
    print("Hello!")

# Calling the function
greet()
