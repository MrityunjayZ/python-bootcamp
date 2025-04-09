# Loop Challenges
# Q1: Sum of N Numbers
# Ask the user for a number n.
# Print the sum of numbers from 1 to n.

num = int(input("Enter a number: "))
sum_numbers = sum(range(1, num + 1))
print("Sum of numbers from 1 to", num, "is", sum_numbers)

# Q2: Multiplication Table Generator
# Ask the user for a number and print its multiplication table up to 10.

number = int(input("Enter a number: "))

print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

sum_of_numbers = sum(range(1, number + 1))
print(f"The sum of numbers from 1 to {number} is: {sum_of_numbers}")

# Q3: Reverse Countdown
# Ask for a number n, then print a countdown from n to 1 using a while loop.

n = int(input("Enter a number: "))
print("Countdown:")
current = n
while current >= 1:
    print(current)
    current -= 1

# Pattern Challenges
# Q4: Right-Aligned Triangle
# Ask the user for rows, and print:
#   *
#  **
# ***
#****
# (Hint: Use nested for loops and end="" to control spacing)

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("*" * i)

# Q5: Number Pyramid
# For n = 5, print:
# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end='')
    print()

