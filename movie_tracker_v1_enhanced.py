import json
from pathlib import Path

# Define the file where we'll store movies
file_path = Path("movies.json")

# Helper: Get a non-empty string input
def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")

# Helper: Get a valid 4-digit year input
def get_valid_year(prompt):
    while True:
        year = input(prompt).strip()
        if year.isdigit() and len(year) == 4:
            return year
        print("Please enter a valid 4-digit year (e.g., 2010).")

# Step 1: Load existing movies or start with an empty list
if file_path.exists():
    with open(file_path, 'r') as file:
        movie_list = json.load(file)
else:
    movie_list = []
# Additional code 1
# Ask the user to search for a movie by title
search_title = get_non_empty_input("Enter the title of the movie to search: ").lower()


# Flag to track if movie was found
movie_found = False

# Search through the loaded_movies list
for movie in movie_list:
    if movie["title"].lower() == search_title:
        print("\nMovie found:")
        print(f"Title: {movie['title']}")
        print(f"Year: {movie['year']}")
        print(f"Watched: {'Yes' if movie['watched'] else 'No'}")
        movie_found = True
        break

if not movie_found:
    print("Movie not found in the list.")

# Step 2: Menu loop
while True:
    print("\n🎬 Movie Tracker Menu")
    print("1. Show unwatched movies")
    print("2. Add a new movie")
    print("3. Mark movie as watched")
    print("4. Exit")
    print("5. Delete a movie")


    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        print("\n📽️ Unwatched Movies:")
        found = False
        for movie in movie_list:
            if not movie.get("watched", False):
                print(f"- {movie['title']} ({movie['year']})")
                found = True
        if not found:
            print("🎉 No unwatched movies! You're all caught up.")

    elif choice == "2":
        title = get_non_empty_input("Enter movie title: ")
        year = get_valid_year("Enter release year (e.g., 2015): ")
        movie = {"title": title, "year": year, "watched": False}
        movie_list.append(movie)
        print(f"✅ Added: {title} ({year})")


    elif choice == "3":
        title_to_mark = get_non_empty_input("Enter movie title to mark as watched: ").lower()
        found = False
        for movie in movie_list:
            if movie['title'].lower() == title_to_mark:
                movie['watched'] = True
                print(f"👍 Marked '{movie['title']}' as watched.")
                found = True
                break
        if not found:
            print("❌ Movie not found.")
# New code to delete a movie 
    elif choice == "5":
        title_to_delete = get_non_empty_input("Enter the title of the movie to delete: ").lower()
        new_list = [movie for movie in movie_list if movie["title"].lower() != title_to_delete]
        if len(new_list) != len(movie_list):
            movie_list = new_list
            print(f"🗑️ Movie '{title_to_delete.title()}' has been deleted.")
        else:
            print("❌ Movie not found.")
       

    elif choice == "4":
        # Step 3: Save movie list before exiting
        with open(file_path, 'w') as file:
            json.dump(movie_list, file, indent=4)
            total = len(movie_list)
            watched = sum(1 for movie in movie_list if movie.get("watched"))
            unwatched = total - watched

            print("\n📊 Summary Report:")
            print(f"🎞️ Total movies: {total}")
            print(f"✅ Watched: {watched}")
            print(f"🍿 Unwatched: {unwatched}")

            print("💾 Saved your movie list. Goodbye!")
            break

    else:
        print("❗ Invalid option. Please choose 1, 2, 3 or 4.")
