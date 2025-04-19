# Warm-Up Challenge: Define and Call Functions
# # Function to add two numbers
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

# Get inputs for addition
num1 = get_valid_number('Enter first number: ')
num2 = get_valid_number('Enter second number: ')
sum_result = add(num1, num2)
print(f"✅ Sum of {num1} and {num2} is: {sum_result}")

# Get inputs for is_even checks
u_num1 = get_valid_number('Enter a number to check if it is even: ')
u_num2 = get_valid_number('Enter another number to check if it is even: ')
print(f"🔍🔍 Is {u_num1} even? → {is_even(u_num1)}")
print(f"🔍🔍 Is {u_num2} even? → {is_even(u_num2)}")
