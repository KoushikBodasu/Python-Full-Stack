# Day 14 - Patterns and Nested Loops

# Star triangle
for i in range(1, 6):
    print("*" * i)

print()

# Number pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()

# Pyramid
for i in range(1, 6):
    spaces = " " * (5 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
