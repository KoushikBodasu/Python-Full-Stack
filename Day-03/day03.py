# Day 3 - Operators and Formatting

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

print("a > b:", a > b)
print("a == b:", a == b)

x = 10
x += 5
print("Assignment operator:", x)

print("Logical:", a > 5 and b < 5)
print("Membership:", 3 in [1, 2, 3])
print("Identity:", a is x)

# Bitwise example
print("Bitwise AND:", 5 & 3)

name = input("Enter your name: ")
print("Hello", name)

print(f"Welcome {name}!")
print("My name is {} and I am learning Python.".format(name))
