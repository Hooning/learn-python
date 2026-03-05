# Task
# Checks whether the password meets the minimum requirement
# of 8 characters

def is_valid_password(password):
    return len(password) >= 8


# Example usage
# Output: Password must be at least 8 characters long. None
print(is_valid_password("short"))
print(is_valid_password("longenough"))  # Output: True

# Task
# Checks whether an email has a basic valid format


def is_valid_email(email):
    return "@" in email and "." in email


# Example usage
print(is_valid_email("example@example.com"))  # Output: True
print(is_valid_email("invalid-email@test"))  # Output: False
