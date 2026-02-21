numbers = [1, 5, 2, 7, 9, 4]
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Length: {len(numbers)}")

# All or Any
print(f"All: {all(numbers)}")
print(f"All with zero: {all([1, 0, 7])}")
print(f"All with empty string: {all(['a', 'b', ''])}")

print(f"Any: {any(numbers)}")
print(f"Any with zero: {any([1, 0, 7])}")
print(f"Any with empty string: {any(['a', 'b', ''])}")

# Counting Occurrences
letters = ["a", "b", "c", "a", "d", "b", "a"]
print(f"Count of 'a': {letters.count('a')}")

# Finding Index
print(f"Index of 'c': {letters.index('b')}")

# in and not it operators
print(f"'a' in letters: {'a' in letters}")
print(f"'z' in letters: {'z' in letters}")

# Analysis & Checks
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(f"list1 == list2: {list1 == list2}")
# checking if both variables point to the same object in memory, which is False because they are two different list objects with the same content.
print(f"list1 is list2: {list1 is list2}")

list2 = [5, 2, 3]
# Comparison is done element-wise, so it compares 1 with 5, which is False, and thus the whole comparison returns False.
print(f"list1 == list2: {list1 > list2}")
