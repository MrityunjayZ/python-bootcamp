import csv

# Step 1: Define the list of Subjects for which we want marks
subjects = ["Physics", "Mathematics", "Biology", "Chemistry", "Statistics"]

# Step 2: Create an empty dictionary to store student names and their corresponding marks
marks = {}

# Step 3: Define a function to collect marks for each student
def user_entry(marks):
    num_students = int(input("How many students' marks do you want to enter? "))
    for _ in range(num_students):
        student_name = input("Enter student's name: ")
        student_marks = {}
        for subject in subjects:
            while True:  # Keeps asking until user enters a valid input
                user_marks = input(f"Enter marks for {subject} (0-100) for {student_name}: ")
                try:
                    user_marks = int(user_marks)  # Try converting input to integer
                    if 0 <= user_marks <= 100:
                        student_marks[subject] = user_marks  # Store valid marks
                        break  # Exit the loop if input is valid
                    else:
                        print("Marks should be between 0 and 100, try again.")
                except ValueError:
                    print("Please enter a valid number.")
        marks[student_name] = student_marks

# Step 4: Save student data to a CSV file
def save_to_csv(marks):
    with open("student_marks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Writing the header row
        writer.writerow(["Student Name"] + subjects)
        for student_name, student_marks in marks.items():
            row = [student_name] + [student_marks.get(subject, "") for subject in subjects]
            writer.writerow(row)
    print("\nData saved to student_marks.csv")

# Step 5: Display the summary of all students' marks
def display_summary(marks):
    print("\nSummary of Student Marks:")
    for student_name, student_marks in marks.items():
        print(f"\n{student_name}:")
        for subject, mark in student_marks.items():
            print(f"  {subject}: {mark}")

# Step 6: Main program execution
user_entry(marks)
save_to_csv(marks)
display_summary(marks)
