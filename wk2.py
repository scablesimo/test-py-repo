# Create a tuple of 5 city names
cities = ("New York", "London", "Tokyo", "Paris", "Sydney")

# Attempt to change one of the cities
try:
    cities[0] = "Los Angeles"
except TypeError as e:
    print("Error:", e)

# Explanation
print("\nExplanation: Tuples are immutable in Python, meaning their elements cannot be changed once assigned.")
