age = 39
print(type(age))
# convert age to string
print("Your age is " + str(age) + " years old")

# Math
password = "1234567a"
print(len(password))
if len(password) < 8:
    print("Password must be at least 8 characters")
else:
    print("Password is strong")

text = """Python is easy to learn.
It is a great language for beginners.
It is also powerful for professionals.
"""
print(text.count("It"))

# Transformations
dateStr = "2026/02/15"
print(dateStr.replace("/", "."))

phone = "123-456-7890"
print(phone.replace("-", " "))

price = "$1,288.68"
print(price.replace("$", "").replace(",", ""))

# challenge
phoneNumber = "+49 (176) 123-4567"
print(phoneNumber.replace(" ", "").replace(
    "+", "00").replace("(", "").replace(")", "").replace("-", ""))

# Join Strings
# Transformations
first_name = "Hoon"
last_name = "Cho"

full_name = first_name + " " + last_name
print(full_name)

folder = "C:\\Users\\Hoon\\Documents\\"
file_name = "report.pdf"
file_path = folder + file_name
print(file_path)

name = "Hoon"
age = 39
is_student = False
print(f"My name is {name}. I am {age} years old. Student: {is_student}")

print(f"{{This is just me!}}")

stamp = "2026-02-15 14:30:00"
print(stamp.split(" "))

csv_file = "John,Doe,30,Engineer"
print(csv_file.split(","))

# String Repeatintion
print("Ha" * 3)

greeting = "Hello"
print(greeting[0])
print(greeting[-1])
print(greeting[2])
print(greeting[-3])

print(greeting[0:3])
print(greeting[-5:-2])

print(greeting[1:])

# [start:end:step]
print(greeting[0:4:2])

# Indexing and Slicing
text = "Python"
print(text[len(text) - 1])

date = "2026-02-15"
print(date[0:4])  # Extract year
print(date[:4])  # Extract year
print(date[5:7])  # Extract month
print(date[8:10])  # Extract day
print(date[8:])  # Extract day
print(date[-2:])  # Extract day

# Cleaning Strings
raw_input = "   Hello, World!   "
cleaned_input = raw_input.strip()
print(cleaned_input)
print(len(cleaned_input))

raw_input = "   Hello, World!"
cleaned_input = raw_input.lstrip()
print(cleaned_input)
print(len(cleaned_input))

raw_input = "Hello, World!   "
cleaned_input = raw_input.rstrip()
print(cleaned_input)
print(len(cleaned_input))
