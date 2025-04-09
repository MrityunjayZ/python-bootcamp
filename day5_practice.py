# Functions
# Q1: Add Two Numbers
# Write a function add_numbers(a, b) that returns their sum.
# Ask the user for two numbers and print the result using the function.

x = int(input(f"enter number one: "))
y = int(input(f"enter number two: "))
def add(x, y):
    return x + y

result = add(x, y)
print("Sum is:", result)

# Q2: Check Even or Odd
# Write a function is_even(n) that returns True if a number is even, otherwise False.

n = int(input("Enter a number: "))
if n % 2 == 0:
 print("True")
else:  
   print("False")

# Q3: Greet User with Default
# Write a function greet(name="Guest") that prints "Welcome, <name>".
# Call it once with a name and once without.  

def greet_user(name):
    print(f"Welcome, {name}!")

greet_user("Guest")

# Lists
# Q4: Search in List
# Create a list of fruits.
# Ask the user to enter a fruit name.
#Check if it exists in the list and print an appropriate message.

user_entry = str(input("Enter a fruit: "))
fruits = ["apple", "banana", "cherry", "mango"]
if user_entry in fruits:
    print("its available",user_entry)
else:
    print("Not found")

# alternate code 
fruits = ["apple", "banana", "cherry", "mango"]

# Convert all fruits in the list to lowercase
fruits_lower = [fruit.lower() for fruit in fruits]

# Get user input in lowercase
user_input = input("Enter a fruit name: ").strip().lower()

if user_input in fruits_lower:
    print(f"{user_input} is available.")
else:
    print(f"{user_input} is not in the list.")
    
# Q5: Find the Max
# Write a function that takes a list of numbers and returns the maximum value.

numbers_str = input("Enter a list of numbers separated by spaces: ")
user_list = [int(num) for num in numbers_str.split()]
print("Your list is: ",user_list)
max_num = 0
for i in user_list:
    if i > max_num:
        max_num = i
print("highest number in list provided is: ",max_num)

# alternate code
numbers_str = input("Enter a list of numbers separated by spaces: ")
user_list = [int(num) for num in numbers_str.split()]
print("Your list is: ",user_list)
max(user_list)
print("highest number in list provided is: ",max(user_list))