# Day 9 - ELIF and Nested Conditions

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")

# Nested condition
age = int(input("Enter your age: "))
if age >= 18:
    has_id = input("Do you have ID? yes/no: ")
    if has_id.lower() == "yes":
        print("Entry allowed")
    else:
        print("Please bring an ID")
else:
    print("Entry not allowed")
