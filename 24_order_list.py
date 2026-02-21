# order number list
numbers = [1, 4, 6, 8, 12, 42, 75, 11, 5, 86, 16]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

matrix = [[6, 5, 4], [2, 3, 1], [9, 7, 8]]
matrix.sort()
print(matrix)

matrix[0].sort()
print(matrix)

numbers = [1, 4, 6, 8, 12, 42, 75, 11, 5, 86, 16]
new_list = sorted(numbers,  reverse=True)
print(numbers)
print(new_list)

numbers = [1, 4, 6, 8, 12, 42, 75, 11, 5, 86, 16]
# numbers.reverse()
new_list = list(reversed(numbers))
print(numbers)
print(new_list)
