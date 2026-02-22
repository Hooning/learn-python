# Iterator object:
# An iterator is an object that implements the iterator protocol,
# which consists of the methods __iter__() and __next__().
# An iterator allows you to traverse through all the elements of a collection,
# such as a list or a tuple, without needing to know the underlying structure of the collection.
#
# Why do we need iterators?
# Iterators provide a way to access elements of a collection one at a time,
# which can be more memory efficient than loading the entire collection into memory at once.

# Iterable object:
# An iterable is any Python object capable of returning its members one at a time,
# allowing it to be iterated over in a for-loop or with other iteration tools.
# Examples of iterables include lists, tuples, strings, dictionaries, and sets.
# An iterable must implement the __iter__() method, which returns an iterator object.
letters = ["a", "b", "c", "d"]
new_letters = []
for letter in letters:
    new_letters.append(letter.upper())
    print(new_letters)

# enumerate() function: is iterator
# The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
# This is useful when you need to access both the index and the value of items in a collection during iteration.
# The syntax is: enumerate(iterable, start=0)
# where iterable is the collection you want to iterate over, and start is the index from which the counter should start (default is 0).
print(list(enumerate(letters)))

for index, letter in enumerate(letters):
    print(f"Index: {index}, Letter: {letter}")

# reversed() function: is iterator
# The reversed() function returns a reverse iterator over the values of the given sequence.
letters = ["a", "b", "c", "d"]
numbers = [1, 2, 3, 4]
print(list(reversed(letters)))
print(list(zip(letters, numbers)))
for letter, number in zip(letters, numbers):
    print(f"Letter: {letter}, Number: {number}")

# map() function: is iterator
# The map() function applies a given function to each item of an iterable (like a list) and returns a map object (which is an iterator).
letters = ["a", "b", "c", "d"]
upper_letters = map(str.upper, letters)
print(list(upper_letters))

print(list(map(lambda x: x + "1", letters)))

numbers = ["1", "2", "3", "4"]
print(list(map(int, numbers)))

names = [" Alice", " Bob ", "Charlie "]
stripped_names = map(str.strip, names)
print(list(stripped_names))

for name in map(str.strip, names):
    print(f"'{name}'")

# filter() function: is iterator
# The filter() function constructs an iterator from elements of an iterable for which a function returns true
list1 = ["sql", "2", "6", None, "a", "b", False, 0]
# filter falsy values
filtered_list = filter(None, list1)
filtered_list = filter(bool, filtered_list)

filtered_list = filter(str.isalpha, filtered_list)
print(list(filtered_list))
