import requests

def fetch_shows(search_term):
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_rating(show):
    return show["rating"]["average"] if show["rating"]["average"] else 0

def save_to_file(shows):
    with open("tv_shows_results.txt", "w") as file:
        file.write("Top TV Show Results\n")
        file.write("=" * 30 + "\n\n")
        for show in shows:
            file.write(f"Title: {show['name']}\n")
            file.write(f"Rating: {show['rating']['average'] if show['rating']['average'] else 'N/A'}\n")
            genres = ", ".join(show["genres"]) if show["genres"] else "N/A"
            file.write(f"Genres: {genres}\n")
            file.write("-" * 30 + "\n")
    print("\n📁 Results saved to 'tv_shows_results.txt'")

def main():
    print("🎬 Welcome to TV Show Finder")

    try:
        search_term = input("Enter a TV show name: ").strip()
        if not search_term:
            raise ValueError("Search term cannot be empty.")

        min_rating = float(input("Enter minimum rating (0 to 10): "))
        if min_rating < 0 or min_rating > 10:
            raise ValueError("Rating must be between 0 and 10.")

        results = fetch_shows(search_term)
        if not results:
            print("No shows found for this keyword.")
            return

        filtered_shows = [item["show"] for item in results
                          if get_rating(item["show"]) >= min_rating]

        if not filtered_shows:
            print("No shows matched your rating criteria.")
            return

        filtered_shows.sort(key=get_rating, reverse=True)
        top_shows = filtered_shows[:5]

        print("\n⭐ Top Matching Shows:\n")
        for show in top_shows:
            print(f"Title: {show['name']}")
            print(f"Rating: {show['rating']['average'] if show['rating']['average'] else 'N/A'}")
            print(f"Genres: {', '.join(show['genres']) if show['genres'] else 'N/A'}")
            print("-" * 30)

        save_to_file(top_shows)

    except ValueError as error:
        print(" Input error:", error)
    except Exception as error:
        print(" Unexpected error:", error)
main()
