# Function to add two numbers
def add(a, b):
    return a + b

# Function to check if a number is even
def is_even(num):
    return num % 2 == 0

# Function to get valid integer input
def get_valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a valid number. Please try again.")

# Main loop
while True:
    print("\nChoose an operation:")
    print("1. Add two numbers")
    print("2. Check if a number is even")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        num1 = get_valid_number('Enter first number: ')
        num2 = get_valid_number('Enter second number: ')
        sum_result = add(num1, num2)
        print(f"✅ Sum of {num1} and {num2} is: {sum_result}")
    elif choice == '2':
        num = get_valid_number('Enter a number to check if it is even: ')
        if is_even(num):
            print(f"🔍 {num} is even.")
        else:
            print(f"🔍 {num} is odd.")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


# Practice Set 1: Basics
 # 1. Write a function multiply(x, y) that returns the product of two numbers.
def multiply(x, y):
    return x * y

factor_1 = float(input("Enter the first number: "))
factor_2 = float(input("Enter the second number: "))

print("The product of the two numbers is", multiply(factor_1, factor_2))


 # 2. Write a function is_odd(num) that returns True if the number is odd, False otherwise.Paired with is_even
def is_odd(a):
    return a % 2 != 0

def is_even(a):
    return a % 2 == 0

u_num = int(input('Enter a number to check if it is even or odd: '))
if is_odd(u_num):
    print('The number is odd.')
else:
    print('The number is not odd.')

if is_even(u_num):
    print('The number is even.')
else:
    print('The number is not even.')

# 3. Write a function print_greeting(name) that prints: "Hello, <name>! Welcome to Python."
def print_greeting(name):
    return f"Hello, {name}! Welcome to Python."

# Get user input
a = input('Enter your name: ')
print(print_greeting(a))

# Practice 2: Functions with Conditions
# 1. Write a function check_sign(num) that prints:
#    - "Positive" if the number is greater than 0
#    - "Negative" if it's less than 0
#    - "Zero" if it's exactly 0

def check_sign(num):
   
    if num > 0:
        print('Positive)')  # Replace with your code
    elif num < 0:
        print('Negative')
    else:
        print('Zero')

num = int(input('Enter a number of your choice: '))
check_sign(num)



# 2. Write a function max_of_two(a, b) that returns the greater of the two numbers

def max_of_two(a, b):
    if a > b:
        return f"{a} is greater"
    elif b > a:
        return f"{b} is greater"
    else:
        return "Both numbers are equal"

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

print(max_of_two(a, b))


# 3. Write a function check_age(age) that prints:
#    - "Child" if age < 13
#    - "Teen" if 13 <= age < 20
#    - "Adult" if 20 <= age < 60
#    - "Senior" if age >= 60

def check_age(age):
    if age < 13:
        return f"{age} yrs old, you are a Child"
    elif 13 <= age < 20:
        return f"{age} yrs old, you are a Teen"
    elif 20 <= age < 60:
        return f"{age} yrs old, you are an Adult"
    else:
        return f"You are a Senior"
    
u_age = int(input('Enter your age: '))
print(check_age(u_age))

# Practice Drill 4: Grading System
# Write a function grade(score) that takes a numeric score (0 to 100) and returns a grade based on the following:
#90 to 100 → "A"
#80 to 89 → "B"
#70 to 79 → "C"
#60 to 69 → "D"
#Below 60 → "F"
def grade(score):
    if 90 <= score <= 100:
        return f'{score} : You have secured A grade'
    elif 80 <= score < 90:
        return f'{score} : You have secured B grade'
    elif 70 <= score < 80:
        return f'{score} : You have secured C grade'
    elif 60 <= score < 70:
        return f'{score} : You have secured D grade'
    else:
        return f'{score} : You have secured F grade'

user_score = int(input("Enter the score (0 to 100): "))  # user input
print("Your grade is:", grade(user_score))  # calling function to print result


# Drill: Check Leap Year
# Write a function called is_leap_year(year) that:
# Returns True if the year is a leap year.
# Returns False otherwise.
# Rules for Leap Year:
# A year is a leap year if it is divisible by 4,
# but not by 100, unless it is also divisible by 400.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Ask user to input a year
year_input = int(input("Enter a year: "))
result = is_leap_year(year_input)

# Print result
if result:
    print(f"{year_input} is a leap year.")
else:
    print(f"{year_input} is not a leap year.")


 # Practice Drill Set 3: Nested Conditions & Combined Logic
#Challenge 1: Movie Ticket Price Checker
# Write a function ticket_price(age, is_student) that returns the price of a 
      # movie ticket based on the following rules:
# If under 12 years old → $5
# If a student (any age) → $8
# If 60 or older → $6
# All others → $10
# Use is_student as a boolean (True/False).
# Then ask the user for input and call your function.
def ticket_price(age, is_student=False):  # default to False
    if age < 12:
        return 5
    elif is_student:
        return 8
    elif age >= 60:
        return 6
    else:
        return 10

# Ask user for age
age_input = int(input("Enter your age: "))

# Only ask for student status if age is 12 or above
if age_input >= 12:
    student_input = input("Are you a student? (yes/no): ").strip().lower()
    is_student = student_input == "yes"
else:
    is_student = False  # Irrelevant for under 12

# Call the function and print result
price = ticket_price(age_input, is_student)
print(f"Your ticket price is: ${price}")

# Multi-Ticket + Summary Tracker Version:
def ticket_price(age, is_student=False):
    if age < 12:
        return 5, "Child"
    elif is_student:
        return 8, "Student"
    elif age >= 60:
        return 6, "Senior"
    else:
        return 10, "Adult"

# Track totals
total_price = 0
categories = {
    "Child": 0,
    "Student": 0,
    "Senior": 0,
    "Adult": 0
}

while True:
    # Get valid age
    while True:
        age_input = input("Enter age (or type 'done' to finish): ").strip()
        if age_input.lower() == "done":
            break
        elif age_input.isdigit():
            age = int(age_input)
            if age >= 0:
                break
            else:
                print("Age cannot be negative.")
        else:
            print("Please enter a valid number or 'done'.")

    if age_input.lower() == "done":
        break

    # Ask for student status if needed
    is_student = False
    if age >= 12:
        while True:
            student_input = input("Are you a student? (yes/no): ").strip().lower()
            if student_input in ["yes", "no"]:
                is_student = student_input == "yes"
                break
            else:
                print("Please answer with 'yes' or 'no'.")

    # Calculate ticket price
    price, category = ticket_price(age, is_student)
    print(f"→ Category: {category}, Price: ${price}\n")
    total_price += price
    categories[category] += 1

# Final summary
print("\n🧾 Summary:")
for cat, count in categories.items():
    print(f"{cat}: {count} ticket(s)")
print(f"Total Price: ${total_price}")


# Drill 1: BMI Checker
# Write a function bmi_category(weight, height) that:
# Accepts weight (in kg) and height (in meters)
# Calculates BMI: BMI = weight / (height ** 2)
# Returns:
# "Underweight" if BMI < 18.5
# "Normal" if 18.5 ≤ BMI < 25
# "Overweight" if 25 ≤ BMI < 30
# "Obese" if BMI ≥ 30

def bmi_category(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

weight = float(input('To check BMI, enter your weight in Kgs: '))
height = float(input('To check BMI, enter your height in Meters: '))
print("Your BMI category is:", bmi_category(weight, height))

# Drill 2: Password Strength Checker
# Write a function check_password(password) that:
# Returns "Weak" if length < 6
# Returns "Medium" if 6 ≤ length < 10
# Returns "Strong" if length ≥ 10
def check_password(password):
    if len(password) < 6:
        return 'Weak'
    elif 6 <= len(password) < 10:
        return 'Medium'
    else:
        return 'Strong'

password = input('Enter your password: ')
print("Password strength:", check_password(password))


# Drill 3: Discount Eligibility Checker
# Task: Write a function is_eligible_for_discount(age, is_student) 
# that returns True if the person is under 18 or a student, otherwise returns False.
def is_eligible_for_discount(age, is_student):
    # Normalize input to lowercase and strip whitespace
    if is_student.lower().strip() == 'yes' or age < 18:
        return True
    else:
        return False

age = int(input('Enter your age: '))
is_student = input('Are you a student? (yes/no): ')
print("Eligible for discount:", is_eligible_for_discount(age, is_student))

# From the book # From the book # From the book # From the book # From the book
# Section 1
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')
hello()

# Parameters (aka Inputs)
def hello(name):
    print('Hello, ' + name + '!')

hello('Alice')
hello('Bob')
hello('Zebra')

# #Micro-Challenge:
# Write a function called greet_and_age that:
# Takes two parameters: name and age
# Prints: "Hello [name], you are [age] years old!"
# Example output if you call greet_and_age('Tom', 30):

def greet_and_age(name, age):
    return f"Hello {name}, you are {age} years old!"

age = int(input('Enter your age: '))
name = input('Enter your Name: ')
msg = greet_and_age(name, age)
print(msg)

# Print v/s Return:
def add(a, b):
    print(a + b)

def add_and_return(a, b):
    return a + b

x = add(5, 3)
print("x is:", x)

y = add_and_return(5, 3)
print("y is:", y)

# Local and Global Scope: Local variable: Defined inside a function — only usable inside that function.
                          #Global variable: Defined outside all functions — usable anywhere in the script.

def my_func():
    spam = 'I am local'
    print(spam)

my_func()
print(spam)  #spam only exists inside my_func() — once the function ends, 
              #the variable disappears. That’s called local scope.

spam = 'I am global'

def my_func():
    print(spam)

my_func()
print(spam) #spam exists outside my_func() — its always available 

spam = 'I am global'

def my_func():
    spam = 'I am local now' # creates a new locaal value for spam, it doesnt affect the out side value
    print('Inside function:', spam)

my_func()
print('Outside function:', spam)
#Note : you can change the global spam value by using 'global spam' inside the local...eg.
spam = 'I am global'

def my_func():
    global spam
    spam = 'Now I’ve changed!'
    print('Inside:', spam)

my_func()
print('Outside:', spam)

# Takes a global variable
#Modifies it using global
#Returns the updated value (even though it's already changed globally)
number = 4

def addval():
    global number
    number = number + 1
    print(number, 'Inside')
    return number

new_val = addval()
print(new_val, 'returned')
print(number, 'outside')




print('Hello', end = '! ') # continues printing in the same line
print('world')
print('Hello', end = '! ')
print('Mrityunjay') 
print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep = ', ') # separates with a desired separator or sign