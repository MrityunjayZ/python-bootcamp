# Concept Notes
# 1. If / Elif / Else Basics

age = int(input("Enter your age: "))
if age < 18 :
    print("You are a minor ")
elif age == 18 :
    print("You just became and adult")
else :
    print("You are an adult")
Notes: the above code defines if the user is an adult, just turned adult or a minor by comparing the entered age variable with socially established adult hood parameter of 18 years

# 2. Comparison Operators

print(10 > 5) #True
print(10 < 5) #False
print(10 == 10) #True
print(10 != 5) #True
Notes: the above code gives true or false value for the numbers compared, in this case 10 and 5, the last one is different as it checks if the numbers are unequal so True

#  3a. Logical Operators

user_age = int(input("Enter your age: "))
age = user_age
has_licence = True
if age >= 18 and has_licence:
    print("You can drive")
else:
    print("You cannot drive")
Notes: above code asks for the user to enter their age and checks parameters if the person is 18 years or above with driving licence then the he\she can drive else if the age is below 18 thenthey cannot drive

#  3b. Logical Operators

user_age = int(input("Enter your age: "))
user_licence = input("Do you have a licence? (Y/N): ").strip().upper()

if user_age >= 18 and user_licence == "Y":
    print("You're of age and have a license. You can drive!")
elif user_age >= 18 and user_licence == "N":
    print("You're of age but need to get a license.")
else:
    print("You're not old enough to drive yet.")


Notes:more refined way with accepting lower case and converting it to upper case Y and N 

# 4. Nested Ifs & Multiple Conditions

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D or Fail")
Notes: above code checks what grade the user has secured, it compares with the rules equal or above 90 is A grade, equal or above 70 is B grade, equal or above 60 is C grade and anything below 60 is D grade or Fail 

