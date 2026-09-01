# Day 13 - Iteration Practice and Logical Problems

# Sum of numbers
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

# Count vowels
word = input("Enter a word: ")
count = 0

for ch in word.lower():
    if ch in "aeiou":
        count += 1

print("Vowels:", count)

# Reverse a string using a loop
reverse = ""
for ch in word:
    reverse = ch + reverse

print("Reverse:", reverse)
