# Reading from a file (sample.txt)
try:
    with open('sample.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print("The file 'sample.txt' does not exist!")

# Writing to a file (output.txt)
try:
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write("This is a new file created using Python.\n")
        file.write("It contains some text written by our script.\n")
        print("Content written to 'output.txt'.")
except Exception as e:
    print(f"An error occurred: {e}")

# Appending to a file (output.txt)
try:
    with open('output.txt', 'a', encoding='utf-8') as file:
        file.write("This is a new line appended to the file.\n")
        file.write("Appending doesn't overwrite the existing content.\n")
        print("Content appended to 'output.txt'.")
except Exception as e:
    print(f"An error occurred: {e}")

# Reading a file line by line
try:
    with open('output.txt', 'r', encoding='utf-8') as file:
        print("Reading file line by line:")
        for line in file:
            print(line.strip())  # strip() removes any extra newline characters
except FileNotFoundError:
    print("The file 'output.txt' does not exist!")

# Bonus Exercise: Check if File Exists Before Reading
import os

file_name = 'output.txt'

if os.path.exists(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        print("\n[Check] File exists. Here’s the content again:")
        print(f.read())
else:
    print(f"[Check] File '{file_name}' does not exist.")

# Open file in append + read mode
with open('logfile.txt', 'a+', encoding='utf-8') as file:
    # Move the file pointer to the beginning before reading
    file.seek(0)
    print("Current file content:")
    print(file.read())

    # Append new log entry
    file.write("New entry added to the log.\n")
    print("New entry appended.")


# Creating Folders and Files Dynamically
from pathlib import Path

# Create a directory
dir_path = Path("my_new_folder")
dir_path.mkdir(exist_ok=True)  # exist_ok=True ensures no error if folder already exists
print(f"Directory created: {dir_path}")

# Create a new file inside the new directory
file_path = dir_path / "example.txt"
file_path.write_text("This is a file inside 'my_new_folder'.")
print(f"File created: {file_path}")

# Rename a file, deleting the existing renamed file if necessary
new_file_path = dir_path / "renamed_example.txt"
if new_file_path.exists():
    new_file_path.unlink()  # Delete the existing renamed file
    print(f"Deleted existing file: {new_file_path}")
file_path.rename(new_file_path)
print(f"File renamed to: {new_file_path}")

# Delete a file
new_file_path.unlink()  # Deletes the renamed file
print(f"File deleted: {new_file_path}")

# Delete an empty directory
dir_path.rmdir()  # Be sure the folder is empty before removing it
print(f"Directory deleted: {dir_path}")

# List all text files in a directory
for txt_file in dir_path.glob("*.txt"):
    print(txt_file)