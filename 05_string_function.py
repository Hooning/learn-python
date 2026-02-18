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

# Whitespace clean up
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

text = "Engineering"
print(len(text))
print(len(text.strip()))

num_of_spaces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())
print(f"Number of leading and trailing spaces: {num_of_spaces}")
print(f"Is the text clean? {is_clean}")

# Clean Cases
text = "python PROGRAMING"
print(text.lower())
print(text.upper())
print(text.title())

# Case Conversions
search = "   Email"
data = "emAil  "

print(search == data)
print(search.lower() == data.lower())
print(search.strip().lower() == data.strip().lower())

# Challenge
text = "968-Maria, ( D@t@ Engineer );; 27y  "
cleaned_text = text.strip().replace("968-", "name: ").replace(",", " |").replace("(",
                                                                                 "role: ").replace("D@t@", "data").replace(" );;", " | age: ").replace("y", "").lower()
print(cleaned_text)

# Search in strings
date = "2026-Feb-10"
print(date.startswith("2026"))
print(date.endswith("10"))

# Using "in" operator (what you have)
print("Feb" in date)  # Returns True/False

# Using find() - returns index or -1 if not found
print(date.find("Feb"))      # Returns 5
print(date.find("Feb") != -1)  # Returns True/False

# Using index() - returns index or raises ValueError if not found
print(date.index("Feb"))     # Returns 5

# Using count() - returns number of occurrences
print(date.count("Feb") > 0)  # Returns True/False

# Validating string
country = "USA"
print(country.isalpha())

# isdigit() vs isnumeric()
# ---------------------------------------------------------------
# Method       | Accepts                                | Examples
# ---------------------------------------------------------------
# isdigit()    | 0-9 digits, superscripts, subscripts   | "123", "²", "₃"
# isnumeric()  | All of isdigit() + fractions,          | "½", "Ⅳ", "三"
#              | Roman numerals, etc.                   | (Chinese 3)
# ---------------------------------------------------------------
phone = "0123456789"
print(phone.isdigit())
print(phone.isnumeric())
print("Ⅳ".isnumeric())
