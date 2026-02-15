import random
import math as Math

# Types
x = 5
y = 3.14
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))

# Converting numeric types
x = "24"
print(type(x))
x = int(x)
print(type(x))
print(x * 3)

y = 3.14
print(int(y))
y = 3
print(float(y))
y = "3.14"
print(float(y))

x = 3
y = 4
print(complex(x, y))

# Math Operators
print(2 + 3)  # Addition
print(5 - 2)  # Subtraction
print(4 * 3)  # Multiplication
print(10 / 2)  # Division
print(10 / 3)  # Division with remainder
print(10 // 3)  # Floor Division
print(10 % 3)  # Modulus
print(2 ** 3)  # Exponentiation

x = 2
x = x + 3
print(x)

x = 2
x += 3
print(x)

x = 2
x -= 3
print(x)

x = 2
x *= 3
print(x)

x = 2
x /= 3
print(x)

# Rounding
print(2 - 10)
print(abs(2 - 10))  # Absolute value

# Rounding Numbers
price = 35.5463734324
print(round(price))  # Round to nearest integer
print(round(price, 2))  # Round to 2 decimal places
print(Math.ceil(price))  # Round up
print(Math.floor(price))  # Round down
print(Math.trunc(price))  # Truncate decimal part
print(int(price))  # Convert to integer (truncates decimal part)

# Advanced Math Functions
print(Math.sqrt(16))  # Square root

# Random Numbers
print(random.random())  # Random float between 0.0 and 1.0
# Random integer between 1 and 6 - usecase for creating dummy data
print(random.randint(1, 6))

# Validation
x = 7.0  # There are no decimal values, it is considered an integer
print(x.is_integer())
y = 3.14
print(y.is_integer())

x = 70
print(isinstance(x, int))
x = 70.01
print(isinstance(x, int))
print(isinstance(x, float))

# Challenge: Generate a random integer between 1 and 100, and check if the result is an even number.
random_number = random.randint(1, 100)
print(f"Generated random number: {random_number}")
print(f"Is the number even? {random_number % 2 == 0}")
