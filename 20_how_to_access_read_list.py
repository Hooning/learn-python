# Access & Read List
alpha_list = ["a", "b", "c", "d", "e"]

print(alpha_list)

print(alpha_list[2])
print(alpha_list[-3])

# Print the last item in the list
print(alpha_list[-1])
print(alpha_list[len(alpha_list) - 1])

# Read Matrix (Nested List)
matrix = [["a", "b", "c", "d", "e", "f"], [1, 2, 3, 4, 5, 6, 7, 8]]

print(len(matrix[0]) * len(matrix[1]))

# Print row+column of all matrix items (e.g., a1, a2, a3, ..., f8)
for row_index in range(len(matrix[0])):
    for col_index in range(len(matrix[1])):
        print(f"{matrix[0][row_index]}{matrix[1][col_index]}")

# Get multiple items from a list using slicing
print(alpha_list[0:3])  # Get items from index 0 to 2 (3 is exclusive)
print(alpha_list[2:])  # Get items from index 2 to the end of the list
# Get items from the start of the list to index 2 (3 is exclusive)
print(alpha_list[:3])
print(alpha_list[-3:])  # Get the last 3 items from the list
print(alpha_list[:])  # Get all items from the list
print(alpha_list)  # Get all items from the list (same as above)

matrix = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

print(matrix[:2])  # Get the first 2 rows of the matrix
print(matrix[1:])  # Get all rows from index 1 to the end of
print(matrix[-1][:2])
