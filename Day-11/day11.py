# Day 11 - FOR ELSE, break, continue, pass and assert

for number in range(1, 6):
    print(number)
else:
    print("Loop completed")

for number in range(1, 10):
    if number == 5:
        break
    print(number)

for number in range(1, 6):
    if number == 3:
        continue
    print("Continue example:", number)

def future_function():
    pass

age = 20
assert age >= 18
print("Assertion passed")
