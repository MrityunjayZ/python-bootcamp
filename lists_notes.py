# -------------------------------------------
# 📘 PYTHON LISTS - NOTES & EXAMPLES
# -------------------------------------------

# 1️⃣ Creating a List
fruits = ['apple', 'banana', 'mango']
print(fruits)

# 2️⃣ Accessing List Items (Index starts from 0)
print(fruits[0])   # Output: apple
print(fruits[2])   # Output: mango

# 3️⃣ Negative Indexing (last item = -1)
print(fruits[-1])  # Output: mango

# 4️⃣ Changing Items
fruits[1] = 'orange'
print(fruits)      # Output: ['apple', 'orange', 'mango']

# 5️⃣ Adding Items
fruits.append('grape')        # Adds at end
fruits.insert(1, 'pineapple') # Adds at index 1
print(fruits)

# 6️⃣ Removing Items
fruits.remove('apple')        # Removes by value
popped_item = fruits.pop()    # Removes last and returns it
print(fruits, "Popped:", popped_item)

# 7️⃣ List Length
print(len(fruits))

# 8️⃣ Looping Through a List
for fruit in fruits:
    print(fruit)

# 9️⃣ Checking Item Existence
if 'mango' in fruits:
    print("Mango is there!")

# 🔟 Sorting and Reversing
numbers = [3, 1, 4, 2]
numbers.sort()        # Sorts ascending
print(numbers)
numbers.reverse()     # Reverses list
print(numbers)

# 🔁 Copying a List
copy_fruits = fruits.copy()

# 🧹 Clearing a List
fruits.clear()

# -------------------------------------------
# ✅ PRACTICE IDEA:
# 1. Create a list of your 5 favorite books/movies
# 2. Add 2 more items, remove 1
# 3. Sort it, and print the final list
# -------------------------------------------

fav_books = [
    'Ramayan',
    'Mahabharat',
    'Chandogya Upnishad',
    'A Brief History of Time',
    'You must be joking Mr Feynman'
]
print(fav_books)
# Append before the loop
fav_books.append('Automate the Boring Stuff with Python')
fav_books.append('Python for dummies')
fav_books.remove('A Brief History of Time')
for index, book in enumerate(fav_books):
    print(f"{index + 1}. {book}")

# Add digits of :
user_num = input('Enter a number: ')

# Check if the input is all digits
if user_num.isdigit():
    total = 0
    # Loop through each character in the input string
    for char in user_num:
        total += int(char)  # Convert each character to an integer and add it to the total
    print(f"The sum of the digits is: {total}")
else:
    print("Error: The input is not a valid number.")


# Exercise

def greet_and_age(name, age):
    return f"Hello {name}, you are {age} years old!"

def get_valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Oops! That's not a valid number. Try again.")

# Main Program
name = input('Enter your Name: ')
age = get_valid_number('Enter your age: ')
user_num1 = get_valid_number('Enter the first number: ')
user_num2 = get_valid_number('Enter the second number: ')

user_sum = user_num1 + user_num2
user_mult = user_num1 * user_num2

msg = greet_and_age(name, age)
print(msg, end='! ')
print('Sum is:', user_sum, 'and Multiplication is:', user_mult)


# --- List Analysis Function ---

# List Challenge — Function Practice
#Task: Write a function called analyze_numbers that:
# Takes a list of numbers as input
# Returns a tuple with the: Sum of the numbers, Maximum number and Minimum number
def analyze_numbers(numbers):
    if not numbers:
        return ("List is empty", None, None)
    
    total = sum(numbers)
    max_val = max(numbers)
    min_val = min(numbers)
    return (total, max_val, min_val)

# You can change this list to test
nums = []  # Try: [] or [3, 5, 7, 2]

# Make sure we call the function and store the result
result = analyze_numbers(nums)

# Now check and print the result safely
if isinstance(result[0], str):
    print(result[0])
else:
    print("Sum:", result[0])
    print("Max:", result[1])
    print("Min:", result[2])


# Sorting & Filtering Lists ----------------------------------------------------------------------
#PART 1: Sorting a List- Python’s built-in .sort() and sorted() help you organize list items:

numbers = [5, 2, 9, 1, 7] # creates a list of multiple numbers
numbers.sort() # sorts the numbers in place (ascending order)
print('Numbers in ascending order: ', numbers)
numbers.sort(reverse=True) # sorts the numbers in place, descending order
print('Numbers in descending order: ', numbers)

# Or use sorted() if you don’t want to change the original list:
original = [5, 2, 9, 1, 7]
new_sorted = sorted(original)
recNew_sorted = sorted(original, reverse=True)
print('original lis is: ', original)
print('New sortred list is: ',new_sorted )
print('New list in descending order is: ',recNew_sorted)

# 📦 PART 2: Filtering a List
# Let’s say you want only the even numbers from a list:

nums = [3, 4, 7, 8, 10, 15] # the original list is created
evens = [] # to store even numbers we create a new empty list
for num in nums:
   if num % 2 == 0:
     evens.append(num) # we add each number which is an even number to the list 'evens'
print('Even numbers are: ', evens)
print('original numbers are: ', nums)


# Challenge: process_numbers ---------------------------------------------------------------------------
#Write a function called process_numbers that: Accepts a list of numbers,,Sorts the list in ascending order
#Filters out only the even numbers, Returns the filtered even numbers
def process_numbers(numbers):
    sorted_list = sorted(numbers)
    evens = [num for num in sorted_list if num % 2 == 0]
    return sorted_list, evens  # Return both values as a tuple

# Example usage
nums = [9, 2, 7, 4, 11, 6]
sorted_nums, even_nums = process_numbers(nums)

print("Sorted original list:", sorted_nums)
print("Even numbers (sorted):", even_nums)