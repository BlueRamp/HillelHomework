def split_string(func):
    def wrapper(*args, **kwargs):
        print(func().split())
    return wrapper()


@split_string
def return_string():
    some_string = input("Input string: ")
    return some_string
