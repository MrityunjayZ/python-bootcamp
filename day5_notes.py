# 1. Defining & Calling Functions

def greet():
    print("Hello, Mrityunjay!")

greet()

# Note: once defined greet() will always recall the fuction and print Hello Mrityunjay

# 2. Function with Parameters

def greet_user(name):
    print(f"Welcome, {name}!")

greet_user("Mrityunjay")

# Note: this code defines greet_user and prints with f strings the user name in {....}

# 3. Return Values

def add(x, y):
    return x + y

result = add(10, 5)
print("Sum is:", result)

# Note: this code defines add(x, y) and adds x and y values

# 4. Default & Keyword Arguments

def power(base, exponent=2):
    return base ** exponent

print(power(3))        # uses default exponent = 2
print(power(2, 5))     # overrides default

# Note: defined parameter here is set to 2, so first it multiplies 3 by to as 2 is default exponent. then it multiplies 2 five times as both the values are given

# 5. Working with Lists

fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits)

for fruit in fruits:
    print(fruit)

# Note: first it defines what is included in the fruits, then appends or adds mango to it. result is list of fruits including apended mango
 