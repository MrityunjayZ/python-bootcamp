
print('Hello, world!')
print('What is your name?')    # ask for their name
myName = input()
print('What is your favorite color:')
favCol = input()
print('Hello, ' + myName, 'your favorite color is ' + favCol)
print()
print('It is good to meet you, ' + myName)
print('Enter a word:')
usrWord = input()
print('The length of the word you entered is:')
print(len(usrWord))
print() # print a blanck line

print('What is your age?')    # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 10) + ' in 10 years from now.')

print('Your name is ' + input('Enter your name: ') + '10')  # corrected code for Q.4
print()

print('What is your Name again? ') # for Q. 5
newName = input()
print('Hi ' + newName + '! Your name has ' + str(len(newName)) + ' letters.')
