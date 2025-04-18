# 1. Number Checker
Ask the user to enter a number. Check if the number is:
Positive
Negative
Zero
Also print whether it’s even or odd.

num = float(input("Enter any number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

if (num % 2) == 0:

              print("The number is even")

else:

              print("The provided number is odd")

# 2. Simple Login System
Ask the user to input a username and password.
If username is "admin" and password is "12345", print "Access granted"
Otherwise print "Access denied"

username = str(input("Enter user name: "))
password = int(input("enter password: "))
if username == "admin" and password == 12345:
    print("acess granted")
else:
       print("acess denied")

# 3. Grade Evaluator
Take a student’s marks as input (0–100). Print the grade:

90–100: A
75–89: B
60–74: C
50–59: D
Below 50: F
If the marks are not within 0–100, show an error.

student_marks = int(input("Enter your marks out of hundred: "))

if student_marks < 0 or student_marks > 100:
    print("Error, not valid marks")
elif student_marks >= 90:
    print("Grade: A")
elif student_marks >= 75:
    print("Grade: B")
elif student_marks >= 60:
    print("Grade: C")
elif student_marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")

# 4. Ride Eligibility Checker
Ask for:
Age
Height in cm
Rules:
Must be 12 years or older
Must be at least 140 cm tall
Print eligibility status accordingly.

height = int(input("Enter your height in cm: "))
age = int(input("Enter your age : "))

if age >= 12 and height >= 140:
    print("You are eligible to apply.")
else:
    print("You are not eligible.")

# 5. Magic Number Guessing Game
Set a variable magic_number = 7
Ask the user to guess a number
Tell them if they guessed:
Correct
Too high
Too low

x = 7
user_guess = int(input("Guess the magic number: "))
if user_guess == x:
    print("Correct")
elif user_guess > x:
    print("Too High")
else:
    print("Too Low")

# Day 3 Practice Paper
Q1. Even or Odd Checker with Range
Ask the user for two numbers (start and end).
Print all even numbers in that range using a loop.

user_num1 = int(input("Enter the starting number: "))
user_num2 = int(input("Enter the end number: "))
for number in range(user_num1, user_num2 + 1):
  if number % 2 == 0:
    print(number)

Q2. Simple Calculator
Ask user to enter two numbers and the operation (+, -, *, /).
Perform and display the result.
Handle division by zero with a proper message.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    print("result is : ", num1 + num2)
elif operator == "-":
    print("result is : ", num1 - num2)
elif operator == "*":
    print("result is : ", num1 * num2)
elif operator == "/":
    if num2 == 0:
      print("Cannot divide by zero.")
    else:
      print("result is : ", num1 / num2)

Q3. Login System (Basic)
Store a predefined username and password.
Ask user to enter both.
Print success message if correct, else allow up to 3 attempts.

counter = 0

while counter < 3:
    username = input("Enter user name: ")
    password = input("Enter password: ")

    if username == "admin" and password == "12345":
        print("Access granted")
        break  # Stop the loop if login is successful
    else:
        print("Access denied")
        counter += 1  # Increment attempts

if counter == 3:
    print("Too many attempts, system locked")

