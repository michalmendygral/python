#ozdabianie
def decorator(func):
    # opakowanie
    def wrapper():
        print("__begin__")
        func()
        print("__end__")
    return wrapper


def hello():
    print("hello world!")

hello = decorator(hello)
hello()

print()

@decorator
def witaj():
    print("witaj świecie!")

witaj()