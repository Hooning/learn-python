# Combining
letters = ["a", "b", "c"]
numbers = [1, 2, 3]

comb = letters + numbers
print(comb)
print(letters * 2)

combined_list = [letters, numbers]
print(combined_list)

numbers.extend(letters)
print(letters)
print(numbers)

# Zip
list1 = [1, 2, 3]
list2 = ["a", "b", "c", "d"]
zipped = list(zip(list1, list2))
print(zipped)

ids = [101, 102, 103]
names = ["Alice", "Bob", "Charlie"]

users = list(zip(ids, names))
print(users)
