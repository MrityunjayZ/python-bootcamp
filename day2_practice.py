name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hi", name.upper())
print("Next year, you will be", age + 1)

length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle is:" , area)

celsius = float(input("Enter temprature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Fahenheit: ",fahrenheit)

principal = float(input("Principal amount: "))
rate = float(input("Annual interest rate (%): "))
time = float(input("Time in years: "))
si = (principal * rate * time) / 100
print("Total Simple interest: ", si)
