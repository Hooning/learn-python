# *args and **kwargs are used in function definitions
#  to allow for variable numbers of arguments.

# def total(a=0, b=0, c=0):
def total(*args):  # arguments
    print(sum(args))


total(3, 5)  # Output: 8
# This will raise a TypeError because total() expects exactly 2 arguments.
total(3, 5, 7)
total(3, 5, 7, 2)

# When to use *args:
# When the parameter has same type of data and
# you want to pass a variable number of arguments to the function.
# positional arguments are passed as a tuple to the function.


def create_user(**kwargs):  # keyword arguments
    print(type(kwargs))
    print(kwargs)


create_user(first_name="Mo", last_name="Salah", age=33, country="Egypt")

create_user(name="Ronaldo", country="Portugal")

# When to use **kwargs:
# When the parameter has different types of data and
# you want to pass a variable number of keyword arguments to the function.
# keyword arguments are passed as a dictionary to the function.
