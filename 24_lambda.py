def multiple(x): return x * 2


print(multiple(5))  # Output: 10


def add(x, y): return x + y


print(add(3, 4))  # Output: 7


def check(i): return i in "python"


print(check("p"))  # Output: True
print(check("a"))  # Output: False

# Using lambda with map()
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16

prices = ["$12.99", "$8.50", "$15.00"]
print(list(map(lambda p: float(p.replace("$", "")), prices)))

# Lambda with filter()
prices = [120, 54, 76, 110, 74]
print(list(filter(lambda p: p >= 100, prices)))

students = [["Maria", 85], ["John", 92], ["Alice", 78], ["Bob", 90]]
print(list(filter(lambda student: student[1] >= 85, students)))

# Challenge: keep only students with names starting with 'A'
print(
    list(filter(lambda student: student[0].lower().startswith("a"), students)))

# Lambda with sorted()
students = [["Maria", 85], ["John", 92], ["Alice", 78], ["Bob", 90]]
sorted_students = sorted(
    students, key=lambda student: student[1], reverse=True)
print(sorted_students)
