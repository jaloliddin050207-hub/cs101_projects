movies = {
    "Inception": ["Sci-Fi", "Action"],
    "The Matrix": ["Sci-Fi", "Action"],
    "Shrek": ["Animation", "Comedy"],
    "Toy Story": ["Animation", "Family"],
    "Interstellar": ["Sci-Fi", "Drama"]
}
genre_index={}
for title, genre_list in movies.items():
    for genre in genre_list:
        if genre not in genre_index:
            genre_index[genre]=[]
        genre_index[genre].append(title)
print(genre_index)
