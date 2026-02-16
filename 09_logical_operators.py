# and / or / not
# and - both sides must be true
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or - at least one side must be true
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not - negates the value
print(not True)  # False
print(not False)  # True
print(not 3 > 1)  # False, because 3 > 1 is True
print(not not True)

# Examples
print(3 > 1 and 5 < 1)  # False, because 5 < 1 is False
print(3 > 1 or 5 < 1)  # True, because 3 > 1 is True
print(3 > 1 and 5 > 1)  # True, because both 3 > 1 and 5 > 1 are True
print(3 > 1 or 5 < 1)  # True, because 3 > 1 is True
print(3 < 1 or 5 < 1)   # False, because both 3 < 1 and 5 < 1 are False

# Example: Login system
email = True
password = True
print(email and password)

# Parentheses can be used to group expressions and control the order of evaluation

# True, because the second part is True
print((3 > 1 and 5 < 1) or (2 > 1 and 4 < 5))

# have "or" and "and" in the same expression, "and" will be evaluated first
# True, because the second part is True
# True, because the second part is True
print(3 > 1 and 5 < 1 or 2 > 1 and 4 < 5)
# True, because the second part is True
print(3 > 1 and (5 < 1 or 2 > 1) and 4 < 5)

# Tasks:
# Allow access only if the user is logged in or
# they are guest
# but they must not banned
is_logged_in = True
is_guest = False
is_banned = False
if ((is_logged_in or is_guest) and not is_banned):
    print("Access granted")
else:
    print("Access denied")

# Challenge
# 1. Check if a user's name is not empty and
#    the age is greater than or equal to 18
name = "David"
age = 17

if name and age >= 18:
    print("User is valid")
else:
    print("User is invalid")

# 2. Check if the password is at least 8 characters long and
#    does not contain spaces
password = "1234567d"

if (len(password) >= 8 and " " not in password):
    print("Password is valid")
else:
    print("Password is invalid")
