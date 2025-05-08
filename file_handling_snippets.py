# --- File Handling Snippets ---

# --- File Reading ---
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)

# --- File Writing ---
with open('file.txt', 'w') as file:
    file.write("This is a new file created using Python.\n")
    file.write("It contains some text written by our script.\n")

# --- File Appending ---
with open('file.txt', 'a') as file:
    file.write("This is a new line appended to the file.\n")
    file.write("Appending doesn't overwrite the existing content.\n")

# --- File Reading Line by Line ---
with open('file.txt', 'r') as file:
    for line in file:
        print(line.strip())

# --- Check if File Exists ---
import os
if os.path.exists('file.txt'):
    print("File exists.")
else:
    print("File not found.")

# --- File Existence Check using os ---
import os

file_path = 'output.txt'
if os.path.exists(file_path):
    print(f"'{file_path}' exists.")
else:
    print(f"'{file_path}' does not exist.")

# --- File Existence Check using pathlib ---
from pathlib import Path

file = Path('output.txt')
if file.exists():
    print(f"{file} exists.")
else:
    print(f"{file} does not exist.")

# pathlib Snippets for File and Directory Handling

from pathlib import Path

# 1. Creating a Path object
file_path = Path("example.txt")

# 2. Writing text to a file using write_text()
file_path.write_text("This is a simple example using pathlib.")

# 3. Reading text from a file using read_text()
content = file_path.read_text()
print("File Content:\n", content)

# 4. Checking if a file or directory exists
print("Does the file exist?", file_path.exists())
print("Is it a file?", file_path.is_file())
print("Is it a directory?", file_path.is_dir())

# 5. Creating a new directory
dir_path = Path("my_folder")
dir_path.mkdir(exist_ok=True)

# 6. Joining paths (cross-platform)
nested_file = dir_path / "nested.txt"
nested_file.write_text("This file is inside my_folder.")

# 7. Listing all files in a directory
print("All files in 'my_folder':")
for file in dir_path.iterdir():
    print(file)

# 8. Filtering files with a specific pattern (e.g., .txt)
print("Text files in 'my_folder':")
for file in dir_path.glob("*.txt"):
    print(file)

from pathlib import Path

# Create a directory
dir_path = Path("my_new_folder")
dir_path.mkdir(exist_ok=True)  # exist_ok=True ensures no error if folder already exists
print(f"Directory created: {dir_path}")

# Create a new file inside the new directory
file_path = dir_path / "example.txt"
file_path.write_text("This is a file inside 'my_new_folder'.")
print(f"File created: {file_path}")

# Rename a file
new_file_path = dir_path / "renamed_example.txt"
file_path.rename(new_file_path)
print(f"File renamed to: {new_file_path}")

# Delete a file
new_file_path.unlink()  # Deletes the renamed file
print(f"File deleted: {new_file_path}")

# Delete an empty directory
dir_path.rmdir()  # Be sure the folder is empty before removing it
print(f"Directory deleted: {dir_path}")

# List all contents in a directory
for item in dir_path.iterdir():
    print(item)

# List all text files in a directory
for txt_file in dir_path.glob("*.txt"):
    print(txt_file)


# Read and Write JSON in Python
import json

# Python dictionary
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "Data Analysis"],
    "is_active": True
}

# Write to JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Read from JSON file
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print(loaded_data)
