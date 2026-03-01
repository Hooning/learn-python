# Sets - Unordered collection of unique items
my_set = {10, 30, 20}  # it is stored in hash table, so it is unordered
print(my_set)

my_set = {10, 30, 20, 10}  # duplicate elements will be ignored
print(my_set)

# Sets do not support indexing, so the following line will raise an error
# print(my_set[0])  # This will raise an error because sets are unordered and do not support indexing.

# Sets are mutable, so you can add or remove elements from a set after it has been created.
my_set.remove(20)  # Remove an element from the set
print(my_set)
my_set.add(40)
print(my_set)
my_set.add(10)  # won't get added, but no error will be raised

# update() method can be used to add multiple elements to a set at once.
my_set.update([50, 60, 70])
my_set.update('hi')
my_set.update(['hello'])
my_set.update({1, 3, 5})
# This is the union operator, which adds all elements from the right set to the left set.
my_set |= {100, 200}
print(my_set)

# remove()
# my_set.remove(777) # This will raise an error if the element is not found in the set.
print(my_set)
# This will not raise an error if the element is not found in the set.
my_set.discard(777)
print(my_set)

# Mathematical set operations
set_a = {10, 20, 50}
set_b = {20, 30, 40}

# Returns a new set that is the union of set_a and set_b
print(set_a.union(set_b))
# This is the union operator, which adds all elements from the right set to the left set.
print(set_a | set_b)

# Returns a new set that is the intersection of set_a and set_b
print(set_a.intersection(set_b))
print(set_a & set_b)  # This is the intersection operator, which returns a new

# only appears in set_a but not in set_b
print(set_a.difference(set_b))
# This is the difference operator, which returns a new set that contains only the elements that are in the left set but not in the right set.
print(set_a - set_b)

# only non shared elements between set_a and set_b
print(set_a.symmetric_difference(set_b))
# This is the symmetric difference operator, which returns a new set that contains only the elements that are in either set_a or set_b but not in both sets.
print(set_a ^ set_b)

print(set_a.issubset(set_b))  # Returns True if set_a is a subset of set_b
print(set_a.issuperset(set_b))  # Returns True if set_a is a superset of set_b
# Returns True if set_a and set_b have no elements in common
print(set_a.isdisjoint(set_b))
