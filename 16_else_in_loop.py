items = [1, 4, 6, 9, 12]

for item in items:
    print(f"Processing item: {item}")
else:
    print("All items have been processed successfully.")


# Else + Break: Else to check whether the loop is fully executed.
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        print("Number 3 found, breaking the loop.")
        break
    print(f"Number: {number}")
else:
    print("Loop completed without finding number 3.")

# check for even numbers
nums = [1, 3, 5, 8, 11]

for num in nums:
    if num % 2 == 0:
        print(f"Even number found: {num}")
        break
    print(f"Number: {num}")
else:
    print("No even numbers found in the list.")

# Why we need Else in Loop?
names = ["Alice", "Bob", None, "Charlie"]
# names = ["Alice", "Bob", "Max", "Charlie"]

for name in names:
    if name is None:
        print("None value found, stopping the loop.")
        break
else:
    print("All names are valid, loop completed successfully.")

# Task: Check if All Files are CSV files
files = ["data1.csv", "data2.csv", "report.pdf", "data3.csv"]

for file in files:
    if not file.endswith(".csv"):
        print(f"Non-CSV file found: {file}, stopping the check.")
        break
else:
    print("All files are CSV files.")

# Challenge
# Check whether any filename appears more than once
file_list = ["data1.csv", "data2.csv", "report.pdf", "data01.csv"]

for file in file_list:
    if file_list.count(file) > 1:
        print(f"Duplicate file found: {file}, stopping the check.")
        break
else:
    print("All files are unique, no duplicates found.")
