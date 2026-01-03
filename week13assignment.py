import requests 

def fetch_shows(search_term):
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_rating(show):
    return show["rating"]["average"]

def save_to_file(shows):
    with open("tv_shows_results.txt", "w") as file:
        file.write("Top TV Show Results\n")
        file.write("=" * 30 + "\n\n")

        for show in shows:
            file.write(f"Title: {show['name']}\n")
            file.write(f"Rating: {show['rating']['average']}\n")

            if show["genres"]:
                genres = ", ".join(show["genres"])
            else:
                genres = "N/A"

            file.write(f"Genres: {genres}\n")
            file.write("-" * 30 + "\n")

    print("\n Results saved to 'tv_shows_results.txt'")

def main():
    print("🎬 Welcome to TV Show Finder")

    try:
        search_term = input("Enter a TV show keyword: ").strip()
        if search_term == "":
            raise ValueError("Search term cannot be empty.")

        min_rating = float(input("Enter minimum rating (0 to 10): "))
        if min_rating < 0 or min_rating > 10:
            raise ValueError("Rating must be between 0 and 10.")

        results = fetch_shows(search_term)
        if not results:
            print("No shows found.")
            return

        filtered_shows = []
        for item in results:
            show = item["show"]
            rating = show["rating"]["average"]

            if rating is not None and rating >= min_rating:
                filtered_shows.append(show)

        if not filtered_shows:
            print("No shows matched your rating criteria.")
            return

        filtered_shows.sort(key=get_rating, reverse=True)

        top_shows = filtered_shows[:5]

        print("\n⭐ Top Matching Shows:\n")
        for show in top_shows:
            print(f"Title: {show['name']}")
            print(f"Rating: {show['rating']['average']}")
            print(f"Genres: {', '.join(show['genres']) if show['genres'] else 'N/A'}")
            print("-" * 30)

        save_to_file(top_shows)

    except requests.exceptions.ConnectionError:
        print(" Network error: Check your internet connection.")
    except requests.exceptions.HTTPError:
        print(" API error: Failed to fetch data.")
    except ValueError as error:
        print(" Input error:", error)
    except Exception as error:
        print(" Unexpected error:", error)

if __name__ == "__main__":
    main()