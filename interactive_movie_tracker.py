import json
from pathlib import Path

# Define the file where we'll store movies
file_path = Path("movies.json")

# Step 1: Load existing movies or start with an empty list
if file_path.exists():
    with open(file_path, 'r') as file:
        movie_list = json.load(file)
else:
    movie_list = []

# Step 2: Menu loop
while True:
    print("\n🎬 Movie Tracker Menu")
    print("1. Show unwatched movies")
    print("2. Add a new movie")
    print("3. Mark movie as watched")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

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
        title = input("Enter movie title: ").strip()
        year = input("Enter release year: ").strip()
        movie = {"title": title, "year": year, "watched": False}
        movie_list.append(movie)
        print(f"✅ Added: {title} ({year})")

    elif choice == "3":
        title_to_mark = input("Enter movie title to mark as watched: ").strip().lower()
        found = False
        for movie in movie_list:
            if movie['title'].lower() == title_to_mark:
                movie['watched'] = True
                print(f"👍 Marked '{movie['title']}' as watched.")
                found = True
                break
        if not found:
            print("❌ Movie not found.")

    elif choice == "4":
        # Step 3: Save movie list before exiting
        with open(file_path, 'w') as file:
            json.dump(movie_list, file, indent=4)
        print("💾 Saved your movie list. Goodbye!")
        break

    else:
        print("❗ Invalid option. Please choose 1, 2, 3 or 4.")
