# Break statement
names = ["John", "Jane", "", "Smith"]

for name in names:
    if name == "":
        print("Empty name found, stopping the loop.")
        break
    print(f"Name: {name}")

# Continue statement
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        print(f"Even number found: {number}, skipping.")
        continue
    print(f"Odd number: {number}")

# Pass statement: It is a placeholder that does nothing, often used when a statement is required syntactically but no action is needed.
nums = (1, 2, 3)

for i in nums:
    if i == 2:
        pass  # This will do nothing, just a placeholder
    print(f"Number: {i}")

# Task1
# Loop through a list of days and print only the working days, skipping the weekends (Saturday and Sunday).
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

weekends = ["Saturday", "Sunday"]

for day in days:
    if day in weekends:
        continue
    print(f"Working day: {day}")

# Task2
# Scan emails to block unsafe data from entering your system
emails = ["example@example.com", "unsafe@example.com",
          "DROP TABLE USERS;", "test@example.com"]

for email in emails:
    if ";" in email:
        print("Unsafe email detected, blocking it.")
        break
    print(f"Safe email: {email}")
