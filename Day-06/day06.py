# Day 6 - Sets and Dictionaries

numbers = {1, 2, 3, 3, 4}
print("Set:", numbers)

numbers.add(5)
numbers.remove(2)
print("Updated set:", numbers)

a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)

student = {
    "name": "Koushik",
    "age": 22,
    "course": "Python"
}

print(student)
print("Name:", student["name"])

student["age"] = 23
student["city"] = "Hyderabad"
print(student)

print("Keys:", student.keys())
print("Values:", student.values())
