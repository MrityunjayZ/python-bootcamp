# Q1: BMI Calculator
weight = float(input("Enter your weight in Kgs: "))
height = float(input("Enter your height in Meters: "))
bmi =  weight/(height ** 2)
print("Your Body mass index is: ",bmi)

# Q2: Minutes to Hours & Minutes
minutes = int(input("Enter total minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} minutes is {hours} hour(s) and {remaining_minutes} minute(s).")

# Q3: Swap Two Variables (no third variable) arithmetic method
a = int(input("Enter value a: "))
b = int(input("Enter value b: "))
a = a + b
b = a - b
a = a - b
print("a =", a)
print("b =", b)

# Q3: Swap Two Variables (no third variable) tuple swap method
a = int(input("Enter value a: "))
b = int(input("Enter value b: "))
a, b = b, a
print("a =", a)
print("b =", b)

# Q4: Add Digits of a 3-Digit Number
number = int(input("Enter 3 digit number: "))
a = number // 100
b = number // 10 % 10
c = number % 10
print(a + b + c)
