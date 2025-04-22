# -------------------------------------------
# 🔧 FUNCTIONS & PARAMETERS - PYTHON NOTES
# -------------------------------------------

# 1️⃣ Basic Function with a Parameter
def greet(name):
    print("Hello", name)

greet("Alice")  # Output: Hello Alice
greet("Bob")    # Output: Hello Bob


# 2️⃣ Function with Multiple Parameters
def greet_with_city(name, city):
    print("Hello", name, "from", city)

greet_with_city("Alice", "Mumbai")  # Output: Hello Alice from Mumbai
greet_with_city("Bob", "Delhi")     # Output: Hello Bob from Delhi


# 3️⃣ Positional vs Keyword Arguments
# Positional (order matters)
greet_with_city("Charlie", "Kolkata")

# Keyword (order doesn't matter)
greet_with_city(city="Chennai", name="Daisy")


# 4️⃣ Default Parameter Values
def greet_default(name, city="Bangalore"):
    print("Hello", name, "from", city)

greet_default("Eva")                # Output: Hello Eva from Bangalore
greet_default("Frank", "Hyderabad")# Output: Hello Frank from Hyderabad


# 5️⃣ Returning Values Instead of Printing
def get_greeting(name, city):
    return f"Hello {name} from {city}"

msg = get_greeting("George", "Pune")
print(msg)  # Output: Hello George from Pune


# 6️⃣ Practice Challenge (Try This Yourself!)
# Create a function called 'add_numbers' that takes two parameters: a and b
# # It should return the sum of a and b
def add_numbers(a, b):
    return ( a + b )
print(add_numbers(5, 6))

# Example:
# add_numbers(5, 7) => 12

# Bonus: Add a default value to b = 10
# So if user only gives one value, it still works:
# add_numbers(5) => 15
def add_numbers(a, b=10):
    return a + b

print(add_numbers(5))      # Expected: 15
print(add_numbers(5, 3))   # Expected: 8

# -------------------------------------------
# Function Challenge Set
# 1. calculate_discount(price, discount_percent)
#Write a function that:
#Takes the original price and discount percent (e.g., 20 for 20%)
#Returns the discounted price
def calculate_discount(price, discount_percent):
    return price - (price * (discount_percent)/100) 
print(calculate_discount(500, 50))

# 2. full_name(first, last, middle="")
#Write a function that:
# Accepts first name, last name, and an optional middle name
# Returns a properly formatted full name
def full_name(first, last, middle=""):
    # Capitalize each part of the name
    first = first.title()
    last = last.title()
    middle = middle.title()

    if middle:
        return f"Welcome {first} {middle} {last}!"
    else:
        return f"Welcome {first} {last}!"

print(full_name('ram', 'prasad'))             # Output: Welcome Ram Prasad!
print(full_name('ram', 'prasad', 'mishra'))   # Output: Welcome Ram Mishra Prasad!

# 3. convert_temperature(temp_celsius)
#Converts Celsius to Fahrenheit using this formula: F = C * 9/5 + 32
def convert_temperature(temp_celsius):
    return temp_celsius*(9/5) + 32
print(convert_temperature(45))