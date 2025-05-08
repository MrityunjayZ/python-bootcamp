import json  # imports JavaScript Object Notation
from pathlib import Path

# Create initial movie list 
movies = [
    {"title": "Inception", "year": "2010", "watched": True},
    {"title": "Interstellar", "year": 2014, "watched": False},
    {"title": "The Diplomat", "year": 2025, "watched": False},
    {"title": "Dhoom Dhaam", "year": 2025, "watched": False}
]

file_path = Path("movie.json")  # Corrected the typo

# Write movies to JSON file
with open(file_path, 'w') as file:
    json.dump(movies, file, indent=4)

# Read the file back
with open(file_path, 'r') as file:
    loaded_movies = json.load(file)

# Print unwatched movies 
print("You still need to watch:")
for movie in loaded_movies:
    if not movie["watched"]:
        print(f"- {movie['title']}")  # Fixed the quote issue

# Add a new movie
new_movie = {"title": "The Matrix 2", "year": "2001", "watched": False}
loaded_movies.append(new_movie)
print(f"\nNew movie added: {new_movie['title']} ({new_movie['year']})")

# Save updated movie list
with open(file_path, 'w') as file:
    json.dump(loaded_movies, file, indent=4)
