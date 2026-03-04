def clean_name(name):
    if not name:
        return None
    else:
        cleaned_name = name.strip().title()
        # print(cleaned_name)
        return cleaned_name


name = clean_name("  jOhn  ")
print(name)

name = clean_name("")
print(name)  # Output: None

# if it don't return anything, it will return None by default


def clean_name(name):
    lower_cleaned = name.strip().lower()
    upper_cleaned = name.strip().upper()
    return lower_cleaned, upper_cleaned


# If you return multiple values, it will return a tuple
# containing those values.
print(clean_name("  jOhn  "))

lo_name, up_name = clean_name("  jOhn  ")
print(lo_name)  # Output: "john"
print(up_name)  # Output: "JOHN"
