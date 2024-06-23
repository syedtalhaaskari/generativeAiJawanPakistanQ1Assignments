# Write a function called fuel_cost that takes 2 numbers as parameter "distance" as required arg 
# and "fuel_per_liter" as optional arg that has default value to 280. 
# The function should return the cost in Rs.

def fuel_cost(distance, fuel_per_liter = 200):
    return distance * fuel_per_liter

distance = 3400
fuel_per_liter = 540
print(f"Distance: {distance}")
print(f"Fuel per liter: {fuel_per_liter}")
print(f"Fuel Cost: {fuel_cost(distance, fuel_per_liter)}")

distance = 34
print(f"\nDistance: {distance}")
print(f"Fuel Cost: {fuel_cost(distance)}")
