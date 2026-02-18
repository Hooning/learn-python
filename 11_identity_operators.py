# Identity operators are used to compare the memory location of two objects.
# They are "is" and "is not".
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True, because the values are the same
print(a is b)  # False, because a and b are different objects in memory

a = 5
b = 5

print(a == b)  # True, because the values are the same
print(a is b)  # True, because a and b are the same object in memory

x = ["a", "b", "c"]
y = x

print(x == y)
print(x is y)

# Tasks
# Validate the email address
# It must be filled in and not empty
email = None
# Use is instead of == when checking for None, because None is a singleton in Python
print(email is not None and email != "")
