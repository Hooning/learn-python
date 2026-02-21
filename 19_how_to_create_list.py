# Create Lists by initializing them with square brackets and separating the items with commas.
empty = []
letters = ["a", "b", "c", "d"]
numbers = [1, 2, 3, 4]
mixed = [1, "a", True, None]
print(mixed)
print(type(mixed))

# Create Lists by using the list() constructor and passing an iterable as an argument.
empty = list()
print(empty)

letters = list("Python")
print(letters)

numbers = list(range(5))
print(numbers)

# Nested Lists (Matrix)
matrix = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
print(matrix)
print(type(matrix))

mixed_matrix = [[1, "a", True], [None, 3.14, "hello"]]
print(mixed_matrix)
print(type(mixed_matrix))
