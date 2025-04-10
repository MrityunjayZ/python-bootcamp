# Write a function greet(name="Guest")
  #Print: Hello, <name>!

def greet_user(name):   #
    print(f"Hello, {name}!")

greet_user("Guest")

# Write a function add_numbers(a, b)
  #Returns the sum
  #Ask user for inputs and call this function

def addnum():
    user_num1 = int(input("Enter first number: "))
    user_num2 = int(input("Enter second number: "))
    sum = user_num1 + user_num2
    print("The sum of ",user_num1,"and ",user_num2,"is: ",sum)
addnum()

# Create a list of numbers [10, 20, 30, 40]
  #Append a number from user input
  #Print the updated list
  #Print the maximum number in the list using a custom function

admin_list = [10, 20, 30, 40]
print(admin_list)
user_add = int(input("Enter number to add to above list: "))
admin_list.append(user_add)
print(admin_list)
max(admin_list)
print("highest number in the updated list is: ",max(admin_list))
