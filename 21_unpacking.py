person = ["Jose", 39, "Full Stack Developer", "Madrid"]
# name = person[0]
# age = person[1]
# profession = person[2]
# city = person[3]

name, age, profession, city = person

print(f"Name: {name}\nAge: {age}\nProfession: {profession}\nCity: {city}")

# Asterisk (*) can be used to unpack the remaining items in a list into a new list.
# allowed to use only one asterisk (*) in the unpacking assignment, and it must be used to unpack the remaining items into a new list.
name, *details, city = person

print(details)

name, *details = person

print(details)

numbers = [1, 2, 3, 4]

fisrt, second, third, fourth = numbers
# Below will fail because there are more items in the list than variables to unpack into.
# first, second, third = numbers
first, second, third, *last = numbers

nums = [1]
first, *rest = nums
print(first)
print(rest)

string = "Hi"
first, *rest = string
print(first)
print(rest)

# Skipping items with underscore (_)
person = ["David", 30, "Data Scientist", "New York"]
name, _, profession, _ = person
print(f"Name: {name}\nProfession: {profession}")
print(_)  # set to the last skipped value, which is "New York" in this case

name, *_, city = person
print(f"Name: {name}\nCity: {city}")
print(_)
