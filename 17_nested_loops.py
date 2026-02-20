for x in range(3):
    for y in range(2):
        print(f"({x}, {y})")

# Why we need nested loops?
# Crossing Data
colors = ["Red", "Green", "Blue"]
sizes = ["Small", "Medium", "Large"]

for color in colors:
    for size in sizes:
        print(f"{color} - Size: {size}")

years = [2025, 2026]
months = ["Jan", "Feb", "Mar"]
days = range(1, 29)

for year in years:
    for month in months:
        for day in days:
            print(f"report_{year}-{month}-{day}.csv")

# Meta Data driven Loops
