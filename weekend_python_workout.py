# WARM-UP SECTION ----------------------------------------------------------------------------
# 1. Ask for user's name and age, then greet them properly
def greet_user(name, age):  # defines a function 
        if age.isdigit(): # checks if the age entered is digit
            return f'Hello!! {name}, you are:{age} yrs old !'
        else:
            return 'Age is invalid, please enter a number'
       
name = input('Enter your name: ')
age = input('Enter your age: ')
greeting = greet_user(name, age)
print(greeting)      

# 🔁 CORE DRILL: Functions + Loops + Lists -----------------------------------------------------------
# 2. Function to take two numbers and return their sum and product
def two_nums(num1, num2):
     sum_num = num1 + num2
     num_multi = num1 * num2
     return f'The total of the two numbers is: {sum_num} and the product of two numbers is : {num_multi}'
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
print(two_nums(num1, num2))

#  Optional Refactor (Just to Learn)
def two_nums(num1, num2):
    return num1 + num2, num1 * num2

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
total, product = two_nums(num1, num2)

print(f'The total of the two numbers is: {total} and the product is: {product}')

# 3. Sort a list and filter only even numbers --------------------------------------------------------
def process_nums(numbers):
    sorted_list = sorted(numbers)  # Doesn't touch original
    new_list = []
    for num in sorted_list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

nums = [5, 3, 10, 2, 8, 11]
new_nums = process_nums(nums)
print("Filtered even numbers:", new_nums)
print("Original list remains:", nums)


#--------------------------------------------------------------------------
# 4. Ask the user for numbers, store them in a list, sort the list, and show only the odd numbers

# Function to process the list: sorts it and filters odd numbers
def process_nums(numbers):
    sorted_list = sorted(numbers)  # Step 1: Create a sorted copy of the original list
    new_list = []                  # Step 2: Initialize an empty list to store odd numbers
    for num in sorted_list:       # Step 3: Loop through the sorted list
        if num % 2 != 0:          # Step 4: Check if the number is odd
            new_list.append(num)  # Step 5: Add odd numbers to the new list
    return new_list               # Step 6: Return the filtered list of odd numbers

# Initialize an empty list to hold user inputs
user_list = []

# Loop to collect input from the user
while True:
    user_input = input("Enter a number (or type 'done' to finish): ")  # Ask for input
    if user_input.lower() == 'done':  # Step 1: Break the loop if user types 'done'
        break
    try:
        num = int(user_input)         # Step 2: Try converting input to integer
        user_list.append(num)         # Step 3: Add valid number to the user list
    except ValueError:                # Step 4: Handle non-numeric input gracefully
        print("Please enter a valid number.")  # Notify the user of invalid input

# Display the original list entered by the user
print("The list you entered is:", user_list)

# Call the function to process the list and get only odd numbers
new_nums = process_nums(user_list)

# Display the sorted list of odd numbers
print('Odd numbers in your list are:', new_nums)

#-----------------------------------------------------------------------------------------------
# Bonus Drill #5: Combo Filter + Math
# Task: Ask the user to enter a list of numbers (same input method).
# From that list: Filter only even numbers, Calculate and display their sum and average
# Function to filter and return even numbers from a sorted list

# Step 1: Function to get even numbers from a sorted list
def get_evens(numbers):
    # We sort the list and return only numbers divisible by 2
    return [num for num in sorted(numbers) if num % 2 == 0]

# Step 2: Function to get odd numbers from a sorted list
def get_odds(numbers):
    # We sort the list and return only numbers NOT divisible by 2
    return [num for num in sorted(numbers) if num % 2 != 0]

# Step 3: Function to compute sum, average, max, and min safely
def compute_stats(nums):
    # Check if list is not empty to avoid division by zero or max/min errors
    if nums:
        total = sum(nums)                     # Get sum of numbers
        avg = total / len(nums)               # Calculate average
        return {
            "sum": total,
            "avg": avg,
            "max": max(nums),
            "min": min(nums)
        }
    else:
        # If list is empty, return safe default values
        return {
            "sum": 0,
            "avg": 0,
            "max": None,
            "min": None
        }

# Step 4: Ask user for numbers until they type 'done'
user_list = []  # Start with an empty list

while True:
    user_input = input("Enter a number (or type 'done' to finish): ")

    if user_input.lower() == 'done':
        break  # Exit the loop if the user is done

    try:
        num = int(user_input)      # Try converting to an integer
        user_list.append(num)      # Add to the list if valid
    except ValueError:
        print("Please enter a valid number.")  # Handle non-numeric inputs

# Step 5: Show the full list user entered
print("\n✅ Your list is:", user_list)

# Step 6: Separate even and odd numbers using the earlier functions
evens = get_evens(user_list)
odds = get_odds(user_list)

# Step 7: Calculate statistics for both even and odd numbers
even_stats = compute_stats(evens)
odd_stats = compute_stats(odds)

# Step 8: Display results for even numbers
print("\n--- Even Numbers Stats ---")
print("Even numbers:", evens)
print("Sum:", even_stats["sum"])
print("Average:", even_stats["avg"])
print("Max:", even_stats["max"])
print("Min:", even_stats["min"])

# Step 9: Display results for odd numbers
print("\n--- Odd Numbers Stats ---")
print("Odd numbers:", odds)
print("Sum:", odd_stats["sum"])
print("Average:", odd_stats["avg"])
print("Max:", odd_stats["max"])
print("Min:", odd_stats["min"])

# Step 10: Compare even and odd stats and print summary
print("\n📊 Final Comparison:")

# Compare total sum
if even_stats["sum"] > odd_stats["sum"]:
    print("✅ Evens have a higher sum.")
elif odd_stats["sum"] > even_stats["sum"]:
    print("✅ Odds have a higher sum.")
else:
    print("⚖️ Both have equal sums.")

# Compare average
if even_stats["avg"] > odd_stats["avg"]:
    print("✅ Evens have a higher average.")
elif odd_stats["avg"] > even_stats["avg"]:
    print("✅ Odds have a higher average.")
else:
    print("⚖️ Both have equal averages.")


#-----------------------------------------------------------------------------------
# Goal: Ask the user to enter marks for 5 subjects. Store the marks in a list.
  #Calculate and display: The total marks. The average marks. The highest and lowest mark.
  #Also, tell the user: Whether their average is above 75 (then print "Distinction ✨")
     #Between 50-75 ("Passed ✅"),Below 50 ("Failed ❌")

# Store in .CVS file
import csv

# Step 1: Define the list of Subjects for which we want marks
subjects = ["Physics", "Mathematics", "Biology", "Chemistry", "Statistics"]

# Step 2: Create an empty dictionary to store student names and their corresponding marks
marks = {}

# Step 3: Define a function to collect marks for each student
def user_entry(marks):
    num_students = int(input("How many students' marks do you want to enter? "))
    for _ in range(num_students):
        student_name = input("Enter student's name: ")
        student_marks = {}
        for subject in subjects:
            while True:  # Keeps asking until user enters a valid input
                user_marks = input(f"Enter marks for {subject} (0-100) for {student_name}: ")
                try:
                    user_marks = int(user_marks)  # Try converting input to integer
                    if 0 <= user_marks <= 100:
                        student_marks[subject] = user_marks  # Store valid marks
                        break  # Exit the loop if input is valid
                    else:
                        print("Marks should be between 0 and 100, try again.")
                except ValueError:
                    print("Please enter a valid number.")
        marks[student_name] = student_marks

# Step 4: Save student data to a CSV file
def save_to_csv(marks):
    with open("student_marks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Writing the header row
        writer.writerow(["Student Name"] + subjects)
        for student_name, student_marks in marks.items():
            row = [student_name] + [student_marks.get(subject, "") for subject in subjects]
            writer.writerow(row)
    print("\nData saved to student_marks.csv")

# Step 5: Display the summary of all students' marks
def display_summary(marks):
    print("\nSummary of Student Marks:")
    for student_name, student_marks in marks.items():
        print(f"\n{student_name}:")
        for subject, mark in student_marks.items():
            print(f"  {subject}: {mark}")

# Step 6: Main program execution
user_entry(marks)
save_to_csv(marks)
display_summary(marks)
