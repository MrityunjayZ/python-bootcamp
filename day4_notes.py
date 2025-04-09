# Day 4 Concepts: Loops & Iteration
# 1. for Loop Basics
for i in range(5):
    print(i)  # prints 0 to 4

# range(n) where (n) is the limit when the execution stops meaning it will stop at 4 or n-1
# range(stop): Generates a sequence of numbers starting from 0 up to (but not including) stop.
# range(start, stop): Generates a sequence of numbers starting from start up to (but not including) stop.
#range(start, stop, step): Generates a sequence of numbers starting from start, incrementing by step, up to (but not including) stop.

#2. while Loop Basics
counter = 1
while counter <= 5:
    print(counter)
    counter += 1
# the code repeats while the condition is True, in this case it will run printing 0 to 5
# Risk: Infinite loop if no update (counter += 1) meaning if we do not specify to increase the counter by 1 or any other number after each execution the code will keep on running without termination

# 3. Loop Control Statements

# break example
for i in range(10):
    if i == 5:
        break
    print(i)

# continue example
for i in range(5):
    if i == 2:
        continue
    print(i)
# break exits the loop early, meaning even if the range is higher this code will break or stop executing once it reache 5
# continue skips the current iteration meaning this code will skip printing any value given to the i for range(n)



