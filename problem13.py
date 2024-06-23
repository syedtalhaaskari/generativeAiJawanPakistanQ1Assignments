# Write a function called km_to_miles that takes kilometers as a parameter, converts it into miles and returns the result.

def km_to_miles(kilometers):
    return round(kilometers * 0.621371, 2)

km = 100

miles = km_to_miles(km)

print(f"Kilometers: {km}")
print(f"Miles: {miles}")
