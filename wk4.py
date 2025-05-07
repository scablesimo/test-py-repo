# Create a dictionary with a person's details
person = {
    "name": "John Newton",
    "age": 30,
    "email": "john.newton@gmail.com"
}

# Update the email address
person["email"] = "john.newton@gmail.com"

# Print all keys and values
print("Person details:")
for key, value in person.items():
    print(f"{key}: {value}")
