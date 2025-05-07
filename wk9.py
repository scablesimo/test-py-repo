# utils.py


def greet_user(name):
    print(f"Hello,{name}!")
def square_number(n):
    return n**2

greetuser:("Stefano") # type: ignore
result = square_number(5)
print("Square of 5 is:",result)