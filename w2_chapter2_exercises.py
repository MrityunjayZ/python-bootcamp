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


