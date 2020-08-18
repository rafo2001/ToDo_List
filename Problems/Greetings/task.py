def morning(func):
    def wrapper(arg1):
        func(arg1)
        print("Good morning,", arg1)
    return wrapper
