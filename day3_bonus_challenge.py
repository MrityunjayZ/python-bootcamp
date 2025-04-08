# Day 3 Bonus Challenge: Driving School Eligibility
Write a Python program to determine if a person is eligible to enroll in a driving school. The school has the following conditions:

Age must be between 18 and 60.
If the person is between 16 and 18, they can join a pre-license course.
If under 16 or over 60, they are not eligible.
If eligible, ask if they own a car (Y/N).
If yes → print "Great! You can start driving once licensed."
If no → print "No problem! We'll help you with car rentals."

print("Welcome to Drive Safe Driving Eligibility Check")
input("Press enter to continue...")

try:
    user_age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number for age.")
    exit()

# Check eligibility
if user_age < 16 or user_age > 60:
    print("Sorry, you're not eligible for driving school.")
elif 16 <= user_age < 18:
    print("You're eligible for our pre-license course.")
else:
    print("You are eligible for the full license course.")
    user_licence = input("Do you own a car? (Y/N): ").strip().upper()
    if user_licence == "Y":
        print("Great! You can start driving once licensed.")
    elif user_licence == "N":
        print("No problem! We'll help you with car rentals.")
    else:
        print("Invalid input. Please enter Y or N.")