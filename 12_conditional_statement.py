# # score calulator A -> F
# score = int(input("Enter your score: "))

# if score >= 90:
#     print("Your grade is A")
# elif score >= 80:
#     print("Your grade is B")
# elif score >= 70:
#     print("Your grade is C")
# elif score >= 60:
#     print("Your grade is D")
# else:
#     print("Your grade is F")

# # Independent if statements
# # score = int(input("Enter your score: "))
# if score >= 90:
#     print("Your grade is A")
# if score >= 80:
#     print("Your grade is B")
# if score >= 70:
#     print("Your grade is C")
# if score >= 60:
#     print("Your grade is D")
# if score < 60:
#     print("Your grade is F")

# Challenge
# 1. Validate the email address
# It must be filled in and not empty
# Must contain "." and "@"
# Must contain exactly one "@"
# Must end with '.com', '.org', '.net'
# Must not be longer than 254 characters
email = "hi@test.com"

if email == "":
    print("Error: Email cannot be empty")
elif "@" not in email:
    print("Error: Email must contain '@'")
elif email.count("@") != 1:
    print("Error: Email must contain exactly one '@'")
elif "." not in email:
    print("Error: Email must contain '.'")
elif not (email.endswith(".com") or email.endswith(".org") or email.endswith(".net")):
    print("Error: Email must end with '.com', '.org', or '.net'")
elif len(email) > 254:
    print("Error: Email must not be longer than 254 characters")
elif not (email[0].isalnum() and email[-1].isalnum()):
    print("Error: Email must start and end with alphanumeric characters")
else:
    print("Valid email address")
