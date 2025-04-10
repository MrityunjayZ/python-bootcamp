user_age = int(input("Enter your age: ")) #Takes user's age and license status (Y/N)
user_licence = str(input("Do you have licence Y/N :"))

if user_licence == "Y" and user_age >= 18:  #If age ≥ 18 and license == Y → print "You can drive"
    print("You can drive")
if user_age >= 18 and license == "N":
    print("Get a license")
else:
    print("You're not old enough")

