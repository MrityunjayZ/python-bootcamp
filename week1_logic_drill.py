# 1. Challenge 1: Palindrome Checker
check = input("Enter a word to check if it is a Palindrome: ")
check = check.lower()  # properly call lower()

reversed_check = ''.join(reversed(check))  # convert reversed object to string

if check == reversed_check:
    print('The word entered is a palindrome.')
else:
    print('The word entered is not a palindrome.')

# 2. Prime Number Checker

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

    # User input handled outside the function
number = int(input("Enter a number to check if it's a prime: "))
if is_prime(number):
    print("It is a prime number.")
else:
    print("It is not a prime number.")

# Q3: Password Strength Checker
def check_password_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if len(password) < 8:
        return "Very Weak"
    elif has_upper and has_lower and has_digit and has_special:
        return "Strong"
    else:
        return "Weak"

# Get input from user
user_password = input("Enter your password: ")

# Call function and store the result
strength = check_password_strength(user_password)

# Print the result
print(f"Password is {strength}")

# Challenge 4: To-Do List Manager

def todo_list_manager():
    tasks = []

    while True:
        print("\n--- TO-DO MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            task = input("Enter new task: ")
            tasks.append(task)
            print(f"New task: {task} added.")
        elif choice == '2':
            print("Your list of tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '3':
            if tasks:
                delete_index = int(input("Enter task number to delete: ")) - 1
                if 0 <= delete_index < len(tasks):
                    removed = tasks.pop(delete_index)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks to delete.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

# Call the function
todo_list_manager()
