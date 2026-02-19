# Loop through tuples
for i in (1, 2, 3, 4, 5):
    print(f"Round {i}")

# Loop through lists
items = [1, 2, 3, 4, 5, "Hi"]
for item in items:
    print(f"Item: {item}")

# Loop through string
typed_string = "Hello World!"
for char in typed_string:
    print(f"Character: {char}")

# Loop through range
# range(start, stop, step)
# default start is 0, default step is 1
range_numbers = range(1, 6)
for i in range_numbers:
    print(f"Number: {i}")

# Loop through dictionary
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(f"Key: {key}, Value: {person[key]}")

# Real-world example: Calculate the average score of a list of scores
scores = [85, 90, 78, 92, 88]
total = 0

for score in scores:
    total += score
print(f"total score: {total}")
print(f"average score: {total / len(scores)}")

files = ["file1.csv ", "File2.csv", " file3.TXT"]

for file in files:
    file = file.strip().lower().replace(".txt", ".csv")
    print(f"Processed file name: {file}")

# Challenge: Use for loops to print 7 times table from 1 to 10
times_table = 7

for i in range(1, 11):
    print(f"{times_table} x {i} = {times_table * i}")

for i in range(7):
    print("*" * i)
