# String data type in Python
print("hello".upper())
print("WORLD".lower())
print("python programming".title())

# Integer data type in Python
print("Addition: ", 10 + 5)  # Addition
print("Subtraction: ", 10 - 5)  # Subtraction
print("Multiplication: ", 10 * 5)  # Multiplication
print("Division: ", 10 / 5)  # Division
print("Floor Division: ", 10 // 3)  # Floor division
print("Modulus: ", 10 % 3)  # Modulus

# Float data type in Python
print("Addition: ", 10.5 + 5.5)  # Addition
print("Subtraction: ", 10.5 - 5.5)  # Subtraction
print("Multiplication: ", 10.5 * 5.5)  # Multiplication
print("Division: ", 10.5 / 5.5)  # Division

# complex data type in Python
complex_number = 2 + 3j
print("Real part:", complex_number.real)
print("Imaginary part:", complex_number.imag)

# Set data type in Python
my_set = {4, 2, 1, 5, 3}
my_set.add(6)
# find value 3 in the set
print("Is 6 in my set?", 6 in my_set)
print("Is 7 in my set?", 7 not in my_set)
my_set.remove(6)
print("My set:", my_set)


# tuple data type in Python
my_tuple = (1, 2, 3, 4, 5, 5, "6")
# Finding the index of an element in the tuple
print("Index of '6' in my tuple:", my_tuple.index("6"))
print("My tuple:", my_tuple)

# dictionary data type in Python
my_dict = {"name": "David", "age": 30, "city": "New York"}
print("My dictionary:", my_dict)

# list data type in Python
my_list = [1, 2, 3, 4, 5, "6"]
my_list.append(7)  # Adding an element to the list
print("My list:", my_list)

# Challenge
age = 39
height = 1.77
name = "Hoon"
amIStudent = False
somthing = None

print(f"Name: {name}, Age: {age}, Height: {height}, Am I a student? {amIStudent}, Something: {somthing}")
print(f"Data types - Name: {type(name)}, Age: {type(age)}, Height: {type(height)}, Am I a student? {type(amIStudent)}, Something: {type(somthing)}")
print(f"Length of name: {len(name)}")
