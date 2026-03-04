# Building Full name clean
def clean_full_name(first_name, last_name, country):
    cleaned_first_name = first_name.strip().title()
    cleaned_last_name = last_name.strip().title()
    full_name = f"{cleaned_first_name} {cleaned_last_name}"
    print(full_name, "from", country.strip().upper())


clean_full_name("  jOhn  ", "  doE  ", "Germany")  # Positional arguments
clean_full_name(country="South Korea", first_name="  hoon  ",
                last_name="  chO  ")  # Keyword arguments

# Mixed arguments (not recommended)
# Rule1: Positional arguments must come before keyword arguments.
# Rule2: Once you use a keyword argument, all subsequent arguments must also be keyword arguments.
clean_full_name("  jOhn  ",  country="Germany", last_name="  doE  ")

# Default parameters
# Rule1: Default parameters must come after non-default parameters
#        in the function definition.


def bonus_calculation(salary, bonus_percentage=10):
    bonus = salary * (bonus_percentage / 100)
    print(f"Bonus: {bonus}")


bonus_calculation(70000)  # Uses default bonus_percentage of 10%
bonus_calculation(70000, 15)  # Overrides default bonus_percentage with 15%
