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
