# Add new data to the list
numbers = ["a", "b", "c"]
numbers.append("d")  # Add 'd' to the end of the list
numbers.append("e")  # Add 'e' to the end of the list
print(numbers)

numbers.insert(1, "x")  # Insert 'x' at index 1
print(numbers)
numbers.insert(0, "y")
print(numbers)

matrix = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
matrix.append(["j", "k", "l"])  # Add a new row to the matrix
# Insert a new row at the beginning of the matrix
matrix.insert(0, ["m", "n", "o"])
matrix[2].append("x")
matrix[0].insert(0, "z")
print(matrix)

# Remove data from the list
numbers = ["a", "b", "c", "d", "c", "e"]
# Remove 'c' from the list, it will remove the first occurrence of 'c'
numbers.remove("c")
print(numbers)

numbers.pop(1)  # Remove the item at index 1 (which is 'b')
print(numbers)

print(numbers.pop())  # Remove the last item and print it
print(numbers)

numbers.clear()
print(numbers)

matrix = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
matrix.remove(["d", "e", "f"])  # Remove the second row from the matrix
matrix.pop()
print(matrix)

# Update data in the list
letters = ["a", "b", "c", "d", "e"]
letters[2] = "z"  # Update the item at index 2 to 'z'
print(letters)


matrix = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
matrix[2] = ["x", "y", "z"]  # Update the third row of the matrix
matrix[0][0] = "-"
matrix[1][1] = "*"
matrix[2][2] = "!"
print(matrix)
