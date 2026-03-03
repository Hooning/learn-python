# Dictionaries are a collection of key-value pairs.
# They are ordered (as of Python 3.7) and mutable.
# Keys must be unique and immutable (like strings, numbers, or tuples),
# while values can be of any data type and can be duplicated.
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'a': 20
}

# keys are unique, so the second 'a' will overwrite the first 'a's value
# values can be duplicated, so the value 20 can be assigned to multiple keys
print(my_dict)

# print(my_dict[1])  # Not indexed by position.
print(my_dict['a'])  # Indexed by key.

# Is it mutable? Yes, we can change the value of an existing key.
my_dict['c'] = 60
print(my_dict)

# dict methods
user = {"id": 1, "name": "Alice", "city": "Berlin"}

print(user['city'])  # Accessing value by key
# This will raise a KeyError because 'age' is not a key in the dictionary.
# print(user['age'])
print(user.get('age'))  # This will return None instead of raising an error.
print(user.get('age', 'Not Found'))  # This will return 'Not Found'

# checks
print("age" in user)
print("age" not in user)

# View Objects
print(user.keys())
print(user.values())
print(user.items())

for key, value in user.items():
    print(f"{key}: {value}")

# Add, Remove, and Update
user["age"] = 30  # Add
user["city"] = "Paris"  # Update
print(user)

# Update multiple keys at once
user.update({"name": "Bob", "country": "France"})
print(user)

# Remove a key-value pair
age = user.pop("age")
print(user)
print(f"Removed age: {age}")

# This will not raise an error if 'salary' is not a key in the dictionary.
salary = user.pop("salary", "Not Found")
print(f"Removed salary: {salary}")

# user.pop() # This will raise an error because pop() requires a key argument.
# This will remove and return the last key-value pair added to the dictionary.
user.popitem()
print(user)

# Creation
user = {"id": None, "name": None, "city": None}
print(user)

user2 = dict.fromkeys(["id", "name", "city"], None)
print(user2)

# Challenge
# 1. Create New Dict
# 2. Keep only pairs with String Values
# 3. Convert values to uppercase
original_dict = {
    "id": 123,
    "name": "Alice",
    "age": 30,
    "city": "Berlin",
}

new_dict = {}

for key, value in original_dict.items():
    # if isinstance(value, str):
    if type(value) == str:
        new_dict[key] = value.upper()

print(new_dict)

comprehension_dict = {
    # Expression
    key: value.upper()
    # Loop
    for key, value in original_dict.items()
    # Filter
    if isinstance(value, str)
}

print(comprehension_dict)

test_dict = {1: "one", 2: "two", 3: "three"}
print(test_dict)
