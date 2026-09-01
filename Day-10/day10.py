# Day 10 - FOR Loop and Problem Solving

numbers = [10, 20, 30, 40, 50]

total = 0
for number in numbers:
    print(number)
    total += number

print("Total:", total)

# Find even numbers
for number in range(1, 11):
    if number % 2 == 0:
        print("Even:", number)
