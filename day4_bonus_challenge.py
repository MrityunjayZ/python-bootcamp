# Day 4 Bonus Challenge: FizzBuzz with a Twist
# Problem Statement:

# Print numbers from 1 to 50 with the following rules:
# If the number is divisible by 3, print "Fizz"
# If it’s divisible by 5, print "Buzz"
# If divisible by both 3 and 5, print "FizzBuzz"
# Else, just print the number

# Example Output:

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# ...
# 14
# FizzBuzz
# ...

for num in range(51):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
        continue
    elif num % 3 ==0:
        print("fizz")
    elif num % 5 ==0:
        print("buzz")   
    else:
        print(num)