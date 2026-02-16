print(True)
print(False)
print(type(True))

print(bool(123))  # True
print(bool(0))  # False
print(bool(""))  # False
print(bool([]))  # False
print(bool({}))  # False
print(bool())  # False
print(bool(None))  # False

# any function: returns True if any element of the iterable is true. If the iterable is empty, return False.
if (any(["", 0, [], {}, None])):
    print("At least one element is true")
else:
    print("All elements are false")

# all function: returns True if all elements of the iterable are true (or if the iterable is empty).
if (all([" ", [2, 3], 1, not None])):
    print("All elements are true")
else:
    print("At least one element is false")

# isinstance
print(isinstance(123, int))  # True
print(isinstance("Hello", str))  # True
print(isinstance(3.14, float))  # True
print(isinstance(True, bool))  # True
print(isinstance(123, str))  # False

"Hello".isalpha()  # True
"123".isnumeric()  # True
"123".isdigit()  # True
"Hello123".startswith("H")  # True
