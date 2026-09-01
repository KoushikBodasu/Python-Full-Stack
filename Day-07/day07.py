# Day 7 - Tuples

numbers = (10, 20, 30, 40)
print("Tuple:", numbers)
print("First item:", numbers[0])
print("Last item:", numbers[-1])
print("Slice:", numbers[1:3])

print("Length:", len(numbers))
print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))

# Tuple unpacking
a, b, c = (1, 2, 3)
print(a, b, c)
