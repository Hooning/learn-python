# While Loop
# Repeats a block of code - over and over as long as a condition is True!

# For vs While Loop
# For Loop: Used when you know in advance how many times you want to execute a block of code.
# While Loop: Used when you want to repeat a block of code an unknown number of times, until a certain condition is met.

# Example of While Loop
# While condition
i = 1  # initialization

while i <= 5:
    print(f"Number: {i}")
    i += 1  # increment
print("While loop completed.")

# Task: Count numbers from 1 to 5
Count = 1

while Count <= 5:
    print(f"{Count}")
    Count += 1

# Task: Ask the user for input until they type "yes"
answer = ""

while answer != "yes":
    answer = input("Do you agree? (yes/no): ").lower()
print("Thank you for agreeing!")

# While True: Infinite Loop
while True:
    user_input = input("Type 'exit' to stop the loop: ").lower()
    if user_input == "exit":
        print("Exiting the loop. Goodbye!")
        break
    print(f"You typed: {user_input}")

chance = 3
attempts = 0

while attempts < chance:
    answer = input("Do you agree? (yes/no): ").lower()
    if answer == "yes":
        print("Glad we're on the same page!")
        break
    attempts += 1
    print("Please reconsider your answer.")
else:
    print("Too many attempts, exiting the loop.")
