# Day 5 - Lists

numbers = [10, 20, 30, 40]
print("List:", numbers)

numbers.append(50)
numbers.insert(1, 15)
numbers.remove(30)

print("Updated list:", numbers)
print("First item:", numbers[0])
print("Slice:", numbers[1:4])

numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
