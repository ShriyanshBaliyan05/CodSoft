print("=" * 70)
print("🍿 MOVIE RECOMMENDATION SYSTEM 🎬".center(70))
print("=" * 70)

print("\n📽️  Select the movies you liked from the list below:\n")

movies = [
    "Avengers: Endgame",
    "Iron Man",
    "The Dark Knight",
    "Joker",
    "Inception",
    "Interstellar",
    "The Shawshank Redemption",
    "The Pursuit of Happyness",
    "3 Idiots",
    "Dangal",
    "Zindagi Na Milegi Dobara",
    "Drishyam",
    "RRR",
    "KGF Chapter 2",
    "Pushpa: The Rise",
    "Dilwale Dulhania Le Jayenge",
    "Yeh Jawaani Hai Deewani",
    "Pathaan",
    "Veer-Zaara",
    "Kalki 2989 AD",
    "Jab We Met",
    "Sita Ramam",
    "Rockstar",
    "Kal Ho Naa Ho",
    "Barfi!",
    "Andhadhun",
    "Kahaani",
    "Gangs of Wasseypur",
    "Special 26",
    "Animal"
]

for i, movie in enumerate(movies, 1):
    print(f"  {i:2d}. 🎬 {movie}")

movie_genres = {
    "Avengers: Endgame": ["Action", "Sci-Fi", "Adventure"],
    "Iron Man": ["Action", "Sci-Fi"],
    "The Dark Knight": ["Action", "Crime", "Thriller"],
    "Joker": ["Drama", "Crime", "Psychological"],
    "Inception": ["Sci-Fi", "Thriller", "Mystery"],
    "Interstellar": ["Sci-Fi", "Drama", "Adventure"],
    "The Shawshank Redemption": ["Drama"],
    "The Pursuit of Happyness": ["Drama", "Inspirational"],
    "3 Idiots": ["Comedy", "Drama"],
    "Dangal": ["Sports", "Drama", "Inspirational"],
    "Zindagi Na Milegi Dobara": ["Comedy", "Drama", "Adventure"],
    "Drishyam": ["Thriller", "Mystery", "Crime"],
    "RRR": ["Action", "Drama", "Historical"],
    "KGF Chapter 2": ["Action", "Crime", "Drama"],
    "Pushpa: The Rise": ["Action", "Crime", "Drama"],
    "Dilwale Dulhania Le Jayenge": ["Romance", "Drama"],
    "Yeh Jawaani Hai Deewani": ["Romance", "Drama", "Comedy"],
    "Pathaan": ["Action", "Thriller", "Adventure"],
    "Veer-Zaara": ["Romance", "Drama"],
    "Kalki 2989 AD": ["Sci-Fi", "Action", "Fantasy"],
    "Jab We Met": ["Romance"],
    "Sita Ramam":["Romance","Drama"],
    "Rockstar":["Romance,Inspirational"],
    "Kal Ho Naa Ho":["Romance","Drama"],
    "Barfi!":["Romance","Drama"],
    "Andhadhun":["Thriller","Drama","Crime"],
    "Kahaani":["Thriller","Crime"],
    "Gangs of Wasseypur":["Crime"],
    "Special 26":["Crime","Action","Drama"],
    "Animal":["Action","Romance"]
}

Action_movie = [
    "Avengers: Endgame",
    "Pathaan",
    "Animal",
    "KGF Chapter 2",
    "Pushpa: The Rise",
    "Kalki 2989 AD"
]

Sci_Fi_movie = [
    "Interstellar",
    "Inception",
    "Kalki 2989 AD",
    "The Martian",
    "Blade Runner 2049",
    "Dune"
]

Fantasy_movie = [
    "Kalki 2989 AD",
    "The Lord of the Rings",
    "Narnia",
    "The Princess Bride"
]

Comedy_movie = [
    "3 Idiots",
    "Zindagi Na Milegi Dobara",
    "Hera Pheri",
    "Chhichhore",
    "Welcome"
]

Romance_movie = [
    "Dilwale Dulhania Le Jayenge",
    "Kabir Singh",
    "Ae Dil Hai Mushkil",
    "Rab Ne Bana Di Jodi",
    "Raanjhanna"
]

Drama_movie = [
    "The Shawshank Redemption",
    "The Pursuit of Happyness",
    "3 Idiots",
    "Dangal",
    "Taare Zameen Par"
]

Crime_movie = [
    "Joker",
    "Pushpa: The Rise",
    "KGF Chapter 2",
    "The Godfather",
    "Gangs of Wasseypur"
]

Thriller_movie = [
    "Drishyam",
    "Inception",
    "Andhadhun",
    "Gone Girl",
    "Se7en"
]

Adventure_movie = [
    "Zindagi Na Milegi Dobara",
    "RRR",
    "Pathaan",
    "Life of Pi",
    "Into the Wild"
]

Inspirational_movie = [
    "Dangal",
    "The Pursuit of Happyness",
    "Super 30",
    "Chak De! India",
    "12th Fail"
]

action = 0
sci_fi = 0
comedy = 0
inspirational = 0
adventure = 0
thriller = 0
crime = 0
drama = 0
romance = 0
fantasy = 0

print("\nEnter upto 5 movies you like 🍿")
print("Enter movie numbers (separated by space): ", end="")
user_input = input()

liked_movies = []
for num_str in user_input.split():
    try:
        num = int(num_str)
        if 1 <= num <= len(movies):
            liked_movies.append(movies[num - 1])
        else:
            print(f"⚠️  Invalid number: {num} (must be 1-{len(movies)})")
    except ValueError:
        print(f"⚠️  Invalid input: {num_str}")

for movie in liked_movies:
    if movie in movie_genres:
        if "Action" in movie_genres[movie]:
            action += 1
        if "Sci-Fi" in movie_genres[movie]:
            sci_fi += 1
        if "Comedy" in movie_genres[movie]:
            comedy += 1
        if "Inspirational" in movie_genres[movie]:
            inspirational += 1
        if "Adventure" in movie_genres[movie]:
            adventure += 1
        if "Thriller" in movie_genres[movie]:
            thriller += 1
        if "Crime" in movie_genres[movie]:
            crime += 1
        if "Romance" in movie_genres[movie]:
            romance += 1
        if "Drama" in movie_genres[movie]:
            drama += 1
        if "Fantasy" in movie_genres[movie]:
            fantasy += 1

genre_scores = {
    "Action": action,
    "Comedy": comedy,
    "Thriller": thriller,
    "Adventure": adventure,
    "Inspirational": inspirational,
    "Drama": drama,
    "Romance": romance,
    "Fantasy": fantasy,
    "Sci-Fi": sci_fi,
    "Crime": crime
}

best_genre = max(genre_scores, key=genre_scores.get)

print("\n" + "=" * 70)
print(f"🎯 Your Favourite Genre: {best_genre}".center(70))
print("=" * 70)

print(f"\n🍿 Recommended Movies for {best_genre} Genre:\n")

genre_movie_map = {
    "Action": Action_movie,
    "Comedy": Comedy_movie,
    "Thriller": Thriller_movie,
    "Adventure": Adventure_movie,
    "Inspirational": Inspirational_movie,
    "Drama": Drama_movie,
    "Romance": Romance_movie,
    "Fantasy": Fantasy_movie,
    "Sci-Fi": Sci_Fi_movie,
    "Crime": Crime_movie
}

recommendations = genre_movie_map.get(best_genre, [])
for i, movie in enumerate(recommendations, 1):
    print(f"  ⭐ {i}. {movie}")

print("\n" + "=" * 70)
print("Happy Watching! 🎬".center(70))
print("=" * 70)