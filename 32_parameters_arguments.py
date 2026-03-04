# Parameters are the variables that are defined in a function's definition.
# Arguments are the values passed to a function when it is called.

# name is a parameter.
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")  # "Alice" is the argument passed to the function.

name = " ThOMas   "


def clean_name(name):
    print(name.strip().title())


clean_name(name)  # " ThOMas   " is the argument passed to the function.

# Global variable
f = 2

# x is a parameter


def multiply_by_f(x):
    # y is a Local variable
    y = x * f  # f is a global variable used inside the function
    print(y)


# 3 is the argument passed to the function, and f is accessed as a global variable
multiply_by_f(3)
