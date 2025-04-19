
# -----------------------------------------
# Chapter 3: Functions - Notes & Examples
# -----------------------------------------

# 📌 What is a function?
# A function is a named block of code designed to do one specific job.
# It helps break down complex problems into smaller parts (modular code).

# -----------------------------------------
# 1. Defining and Calling Functions
# -----------------------------------------

# Syntax:
# def function_name(parameters):
#     # code block
#     return result (optional)

def greet_user():
    print("Hello, welcome to Python!")

greet_user()  # Calling the function


# -----------------------------------------
# 2. Function with Parameters
# -----------------------------------------

def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8


# -----------------------------------------
# 3. The return Statement
# -----------------------------------------

def square(num):
    return num * num

result = square(4)
print("Square is:", result)


# -----------------------------------------
# 4. Arguments and Parameters
# -----------------------------------------

# Positional Arguments
def full_name(first, last):
    return f"{first} {last}"

print(full_name("Ada", "Lovelace"))

# Keyword Arguments
print(full_name(last="Einstein", first="Albert"))

# Default Values
def greet(name="Guest"):
    print("Hello,", name)

greet()            # Hello, Guest
greet("Mrityunjay") # Hello, Mrityunjay


# -----------------------------------------
# 5. Variable Scope: Local vs Global
# -----------------------------------------

# Local Scope: Defined inside the function
def local_example():
    x = 10  # Local variable
    print("Inside function:", x)

local_example()
# print(x)  # ❌ Error: x is not defined globally

# Global Scope
y = 100

def show_global():
    print("Global y is:", y)

show_global()


# -----------------------------------------
# 6. The None Return
# -----------------------------------------

def do_nothing():
    pass

print(do_nothing())  # Output: None


# -----------------------------------------
# 7. Practical Examples
# -----------------------------------------

def is_even(num):
    return num % 2 == 0

print("Is 7 even?", is_even(7))
print("Is 10 even?", is_even(10))


# -----------------------------------------
# End of Notes for Chapter 3
# -----------------------------------------


# -----------------------------------------
# 🧠 Practice Challenges
# -----------------------------------------

# 🔁 Challenge 1: Calculator Function
# Define a function `calculator(a, b, operation)` that can add, subtract, multiply, or divide based on the operation passed.
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Invalid operation"

# Try calling this function with all 4 operations
print(calculator(10, 5, "add"))        # 15
print(calculator(10, 5, "subtract"))   # 5
print(calculator(10, 5, "multiply"))   # 50
print(calculator(10, 5, "divide"))     # 2.0


# 🔁 Challenge 2: Greeting Generator
# Write a function greet_user(name, lang="en") that returns a greeting in English if lang is "en", or Hindi if "hi".

def greet_user(name, lang="en"):
    if lang == "en":
        return f"Hello, {name}!"
    elif lang == "hi":
        return f"Namaste, {name}!"
    else:
        return f"Hi, {name}!"

print(greet_user("Mrityunjay"))         # Hello, Mrityunjay!
print(greet_user("Amit", lang="hi"))    # Namaste, Amit!


# 🔁 Challenge 3: Number Type Checker
# Write a function number_type(num) that returns:
# - "Even" if num is even
# - "Odd" if num is odd
# - "Zero" if num is 0

def number_type(num):
    if num == 0:
        return "Zero"
    elif num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(number_type(0))   # Zero
print(number_type(7))   # Odd
print(number_type(8))   # Even


# 🔁 Challenge 4: Find Maximum of Three
# Write a function max_of_three(a, b, c) that returns the maximum of the three numbers.

def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(5, 12, 8))  # 12

# -----------------------------------------
# ✅ Try modifying and testing these challenges with different inputs!
# -----------------------------------------
