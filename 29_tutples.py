# List is ordered, allows duplicate elements, indexed, mutable.
my_list = [10, 20, 30, 10]
print(my_list)

# Tuple is ordered, allows duplicate elements, indexed, immutable.
my_tuple = (10, 30, 20, 10)
print(my_tuple)
print(my_tuple[1])
# my_tuple[3] = 40  # This will raise an error because tuples are immutable.

# This will return a sorted list, but my_tuple itself remains unchanged.
print(sorted(my_tuple))  # it will convert the tuple to a list

# Use tuples when you want to ensure that the data cannot be modified after creation,
# which can help prevent bugs and improve code readability.
