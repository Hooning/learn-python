# How to Copy?
# 1. Assignment
import copy
original_list = [1, 2, 3, 4, 5]
# This creates a reference to the same list, not a copy
assigned_list = original_list
assigned_list.append(6)
original_list.pop()
# True, both variables point to the same list
print(assigned_list == original_list)
print(assigned_list is original_list)

# 2. Shallow Copy
shallow_copied_list = original_list.copy()
shallow_copied_list.append(7)
original_list.pop()
print(f"shallow_copied_list: {shallow_copied_list}")
print(f"original_list: {original_list}")

matrix = [["a", "b"], ["c", "d"]]
matrix_copy = matrix.copy()
matrix.pop()
# This will affect both matrix and matrix_copy because they share the same inner lists
matrix_copy[0].append("x")
print(f"matrix: {matrix}")
print(f"matrix_copy: {matrix_copy}")
print("==" * 20)

# 3. Deep Copy
matrix = [["a", "b"], ["c", "d"]]
deep_copied_list = copy.deepcopy(matrix)
matrix.pop()
deep_copied_list[0].append("y")
print(f"matrix: {matrix}")
print(f"deep_copied_list: {deep_copied_list}")

# IS Operator
original = [[1, 2, 3], [4, 5, 6]]

# Assignment
list2 = original
print(f"original is list2: {original is list2}")

# Shallow Copy
list3 = original.copy()
print(f"original is list3: {original is list3}")
print(f"original[0] is list3[0]: {original[0] is list3[0]}")

# Deep Copy
list4 = copy.deepcopy(original)
print(f"original is list4: {original is list4}")
print(f"original[0] is list4[0]: {original[0] is list4[0]}")
