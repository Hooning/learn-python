# Ternary statement (conditional expression)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(f"Your grade is {grade}")

# case-match statement (Python 3.10+)
country = "South Korea"

match country:
    case "South Korea":
        print("KO")
    case "United States":
        print("US")
    case "Japan":
        print("JP")
    case "Germany":
        print("DE")
    case _:
        print("Unknown country")
