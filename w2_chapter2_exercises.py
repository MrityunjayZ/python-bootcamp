# Q1. What will this print?
print(4 < 5 and 5 < 6)
 # answer: True
# Q2. What about this one?
print(4 < 5 or 10 < 6)
 # answer: True
print(not (5 == 5))
 # answer: False

# Mixing Boolean and Comparison Operators
(4 < 5) and (5 != 6)  # answer: True
(3 == 3) or (not (2 < 1)) # answer: True

# Challenge:
  #What will the following print? Think and respond before running it.
x = 10
y = 5
print((x > 5 and y < 10) or not (x == 10))
     # answer: True

x = 7
y = 12
print((x < 10 and y > 10) or (x == y))
# answer :True

x = 5  
y = 10  
z = 5  

print((x == z) and not (y < 5))
 # answer: (x == z) means (5 == 5) is True, (y < 5) which is False and with 'not' we are changing it True. so the True and Treu will give us True

x = 7  
y = 3  
z = 7

result = (x != y and z >= x) or (y == 3 and not (z < y))
print(result)
# answer: (7 != 3 and 7>=7) or (3 == 3 and not (7<3))
 # (True and True) or (True and True)
 # True or True , final answer is True 

x = 4
y = 9
z = 4

print((x == z or y < 5) and not (y == 10))
# answer: (4==4 or 9<5) and not(9==10)
# (True or False) and True
# True and True is finally True

#1. Modify the example so that if the name is 'Bob', it prints 'Hello, Bob!' 
 # instead of 'Hi, Alice.'.
name = 'Bob'
if name == 'Bob':
    print('Hi ', name)

# 2. Write an if statement that checks if a number is greater than 10. If true,
 #  print 'Number is greater than 10'.
user_num = int(input('Enter a number: '))
if user_num > 10:
    print('Number is greater than 10')
else:
    print('number not greater than 10')

# Variation 1: Check if a name is not Bob
#Write a program that:

user_name = input('Enter your Name: ')
if user_name != 'Bob':
    print("You're not Bob!")
else:
    print('Hello again, Bob!')


# Variation 2: Check if a number is negative, zero, or positive
 #Write a program that:

user_num = int(input('Enter any Number: '))
if user_num < 0:
    print('Negative number')
elif user_num == 0:
    print('Zero')
else:
    print('Positive number')
    
# Write a program that:
 #Asks the user to enter their age
user_age = int(input(('Enter your age: ')))
if user_age < 13:
    print('Child')
elif  13>= user_age <=17:  # more pythonic way: elif 13 <= user_age <= 17:
    print('Teen')
else:
    print('Adult')

# Quick Task 2: Divisibility Checker
user_number = int(input('Enter a number: ')) 
if user_number % 3 == 0 and user_number % 5 == 0:
     print('Fizzbuzz')
elif user_number % 3 == 0 and user_number % 5 != 0:
     print('Fizz')
elif user_number % 3 != 0 and user_number % 5 == 0:
     print('Buzz')
else:
    print('Not Divisible by 3 and 5')

# Challenge: Odd, Even, or Zero
user_num = int(input('Enter a number: '))
if user_num == 0:
    print('Zero is neither odd nor even.')
else:
    print('The number is even.' if user_num % 2 == 0 else 'The number is odd.')


# Challenge 1: Grade Checker
# Write a Python script that:
user_score = int(input('Enter a score between 0 and 100: '))  # Prompts the user to enter a score between 0 and 100.
if user_score >= 90:
    print('Grade A.')
elif user_score >= 80:
    print('Grade B.')
elif user_score >= 70:
    print('Grade C.')

else:
    print('Fail.')


# Area of a rectangle
u_width = int(input('Enter the width of the rectangle in meters: '))
u_length = int(input('Enter the length of the rectangle in meters: '))
area = u_width * u_length
print(f'{area} Sq.M')

# Challenge: Leap Year Checker

u_year = int(input('Enter the year you wish to check for a leap year: ')) #Asks the user to enter a year.

if u_year % 400 == 0: # unless it is also divisible by 400.
    print(f'{u_year} is a Leap year')
elif u_year % 100 == 0: # But not if it is divisible by 100
    print(f'{u_year} is Not a leap year')
elif u_year % 4 == 0:  # A year is a leap year if it is divisible by 4.
    print(f'{u_year} is a Leap year')
else:
    print(f'{u_year} is Not a leap year')


# Challenge: The Secret Club Password Checker
username = input('Enter user name: ')  #Ask the user for their username.
if username == 'Mrityunjay':  #If the username is "Mrityunjay", ask for a password.
    user_pass = input('Enter your password: ')
    print('Access granted. Welcome to the secret club!' if user_pass == 'openSesame' else 'Wrong password. Access denied!')
else:
    print('Sorry, you are not on the guest list!')


# Challenge: Simple ATM Simulator
stored_pin = '3344'
user_bal = 1000
menu_options = ['1. Check Balance', '2. Deposit Money', '3. Withdraw Money', '4. Exit']

u_pin = input('Enter your 4-digit PIN: ')  # Keep as string for easy comparison
if u_pin == stored_pin:
    print('Access Granted!\n')

    while True:
        print("\nATM Menu:")
        for item in menu_options:
            print(item)
        
        u_choice = input('Enter your choice (1-4): ')
        
        if u_choice == '1':
            print('Your current balance is ₹', user_bal)

        elif u_choice == '2':
            u_deposit = int(input('Enter the amount you wish to deposit: ₹'))
            user_bal += u_deposit
            print(f'₹{u_deposit} deposited successfully. New balance is ₹{user_bal}')

        elif u_choice == '3':
            u_withdraw = int(input('Enter the amount you wish to withdraw: ₹'))
            if u_withdraw <= user_bal:
                user_bal -= u_withdraw
                print(f'₹{u_withdraw} withdrawn successfully. New balance is ₹{user_bal}')
            else:
                print('Insufficient funds!')

        elif u_choice == '4':
            print('Thank you for using our ATM. Goodbye!')
            break

        else:
            print('Invalid option. Please try again.')

else:
    print('Incorrect PIN. Access denied!')

# Round 2: Loop Practice

#Round 2: Light Practice
for i in range(0, 21, +1): #Print all even numbers from 0 to 20 using a for loop.
    if i % 2 == 0:
        print(i)


#print the sum of all numbers between 1 and 100 using a while loop.
# Initialize variables 
sum = 0 
number = 1 
 
while number <= 100: # Use a while loop to sum numbers from 1 to 100 
    sum += number  # Add the current number to the sum 
    number += 1    # Increment the number 
 
# Print the result 
print("The total of all numbers from 1 to 100 is:", sum) 

#Prompt a user to enter a password until they type 'python123', then print 'Access Granted'.
while True:
    password = input('Enter the password: ')
    if password == 'python123':
        break  # Exit the loop if the password is correct
    else:
        print('Wrong password, try again.')
        continue  # Go back to the beginning of the loop

print('Access granted.')

# Loop Drill 1: Count and Skip
#Write a for loop to print all numbers from 1 to 20, but skip multiples of 4.
for i in range(0, 21, 1):
    if i % 4 != 0:
        print(i)

for i in range(0, 21): # Prints only the multiples of 4
    if i % 4 == 0:
        print(i)

# Loop Drill 2: Countdown with While
count = 10
while count >= 1:
  print(count)
  count -= 1
# Use a while loop to count down from 10 to 1, but print only the odd numbers.

count = 10
while count >= 1:
  if count %2 != 0:
   print(count)
  count -= 1

# Mini Drill 1: Reverse & Filter
# Task: Print all numbers from 30 down to 0 that are divisible by 5 but not by 10.
for i in range(30, -1, -1):
    if i % 5 == 0 and i % 10 != 0:
        print(i)

# Mini Drill 2: Sum of Multiples
# Task: Use a for loop to calculate the sum of all numbers between 1 and 50 that are divisible by 3.

total = 0
for i in range(1, 51):
    if i % 3 == 0:
        total += i
print("Sum of numbers divisible by 3 between 1 and 50:", total)

# Loop Drill 3: Custom Range Filter
# Task: Print all numbers between 10 and 100 (inclusive) that are divisible by 7 and end with the digit 1.
for i in range(10, 101):
    if i % 7 == 0: 
        if i % 10 == 1:
          print(i)

# Loop Drill 4: Running Average
# Task: Ask the user to enter 5 numbers using a loop, and after all inputs, print the average of those numbers.
# 🧠 Hint: You'll need a counter and a sum variable.
number_list = []  # Create list outside the loop

  # Loop exactly 5 times
for i in range(5):
    number = int(input('Enter a number: '))
    number_list.append(number)

  # Define a function to calculate average
def average(mylist):
    return sum(mylist) / len(mylist)

  # Call the function and print the result
print('The average is:', average(number_list))

# Loop from 1 to 10. Print only odd numbers using continue.
for num in range(1, 10):
    if num % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print(num)

# Print all numbers between 1 and 15 using a for loop, but skip numbers divisible by 4 using continue.
for num in range(1, 15):
    if num % 4 == 0:
        continue  # Skip numbers divisible by 4
    print(num)

# Break Drill 1: Find the First Multiple of 7
 #Task: Use a loop to find and print the first number between 1 and 100 
 # that is divisible by 7 and greater than 50. Stop the loop once it's found.

for num in range(1, 101): # define the range.
    if num > 50 and num % 7 == 0: # check if number is greater than 50 and divisible by 7
        print('First number greater than 50 and divisible by 7 is ',num)
        break
     
# Break Drill 2: Password Prompt with Break
 # Task: Keep asking the user to enter the correct password "python123" and 
 #exit the loop only when the correct password is entered.
while True:    # runs till the following is True
    u_pass = input('Enter password: ')
    if u_pass == 'python123': 
        print('Access granted')
        break  # if the password is correct, the loop is broken
    else:     # if the 'if' statement is not satisfied executes 'else:'
        print('Wrong password, enter password again')   

#Practice 1: Guess the Secret Number
#Task:
#Set a secret number (e.g. 17).
#Use a while loop to keep asking the user to guess the number.
#When the guess is correct, print "Correct!" and break the loop.
#Otherwise, print "Try again!".

secret_num = '17' # assignes the value 17 to variable secret_num
counter = 0 #sets counter to 0
while True: # runs till the folllowing condition is True
    if counter < 3: #checks if the counter is less than 3
        u_entry = input('Guess the secret number: ')
        counter = counter + 1 #counter value is increased by 1
        if u_entry == secret_num:
                print(f'Correct! You guessed it on attempt #{counter}')
                break # if the user enters the number 17, the loop is broken
        else:    # if the 'if' statement is not satisfied executes 'else:'
            print('Try again')
            
    else: #checks if the counter value is 3, if True then executes the following
         print('Maximum attempts, bye')
         break


# Practice 2: Find the First Number Divisible by Both 6 and 8
#Task:
#Use a for loop to go from 10 to 100.
#Find and print the first number that is divisible by both 6 and 8.
#Use break to stop once it's found.
for num in range(10, 101): # range is defined
    if num % 6 == 0 and num % 8 == 0: # if conditions checks if both the conditions are met
        print(num)
        break # loop breaks at the instance when 'if' condition is met

# Mini Drill
# Drill 1: Skip Multiples
 #Task:Use a for loop to print numbers from 1 to 30, but skip numbers that are divisible by 3 using continue.
for num in range(1, 31): # defines the range 
    if num % 3 == 0: #defines the if condition
        continue #if the number is divisible by 3 the loop continues to look for other numbers 
        print(num) #prints numbers which satisfy the condition 

# Drill 2: Secret Word
 #Task:Use a while loop to keep asking the user to type a secret word: "banana".
 #If the user types the wrong word 5 times, stop the loop with a message "Too many wrong tries!".
counter = 0 #sets counter to 0
while True: # code will run until the 'if' condition is met
    u_input = input('Enter the secret word: ')
    counter = counter + 1 # counter is increased by 1 to calculate the max allowed attempts of 5
    if u_input == 'banana':
        print('Welcome member')
        break # if user enters the correct word the loop breaks with a message
    elif counter == 5: # elif condition to check if the user has attempted for the maximum allowed times.
        print('Too many wrong tries')
        break # if user maxed out the attempts allowed, loop breaks with a message

#Drill 3: Find the First Perfect Square
 #Task:Use a for loop to go from 10 to 100. Print the first number in that range
  #  which is a perfect square (i.e., whose square root is a whole number). Use break to stop once found.
import math #imports math module which contains mathematical functions
for num in range(10, 101): # specifies the range within which the the task has to be performed
    if math.sqrt(num) == int(math.sqrt(num)): #square root is a float so we compare the float 
                                                #and the integer value of it.
        print(num) # if the very first num with perfect square root is found in the range specified, its printed
        break # loop breaks since the condition is satisfied


# This is a guess the number game.
import random # imports the randomt module 
secret_num = random.randint(1, 20) #generates a random number between 1 and 20 and assignes it to secret_num

for guess_attempt in range(1, 7): #defines the no of attempts , which is 6
    user_num = int(input('I am thinking of a number between 1 and 20!, guess the number: '))
    if user_num > secret_num:
        print('Your Guess is too high, guess again: ')
    elif user_num < secret_num:
        print('Your guess is too low, guess again: ')
    else:
        break # this is the corrrect guess
if user_num == secret_num:
    print(' Good job! You guessed my number in ', str(guess_attempt), 'guesses!')
else:
   print('Nope. The number I was thinking of was ', str(secret_num ))


import random, sys
print('ROCK, PAPERS, SISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:     # this is the main game loop
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))

    while True:  # The player input loop
        player_move = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ')
        if player_move == 'q':
            sys.exit() # Quit the program.
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')
    
    # Display what the player chose:
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_number == 3:
        computer_move = 's'
        print('SCISSORS')

# Display and record the win/loss/tie:
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1


