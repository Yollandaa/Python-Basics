from pprint import pprint

movies = [
    {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},
    {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},
    {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},
    {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},
    {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},
]

# Get the movie titles
titles = list(map(lambda movie: movie["title"], movies))
pprint(titles)

# Task 1: Find average rating for all - map, filter, all ...
# Do not use for loop
rates = list(map(lambda x: sum(x["ratings"]) / len(x["ratings"]), movies))
pprint(rates)

def get_avg(movie):
  return sum(movie["ratings"]) / len(movie["ratings"])


print()
# Output should have an extra key on the dictionary "average_rating"
# Create a new list of dictionaries with average rating key using rates list
# Output example: movies_with_average_rating = list(map(lambda movie: "title": "Inception", "ratings": [5, 4, 5, 4, 5], "average_rating": 4.6})}

# lambda function that creates a copy {**movie, "average_rating": rate}}
ratings_movies = list(map(lambda movie, rate: {**movie, "average_rating": rate}, movies, rates))
pprint(ratings_movies)
# movies_average_ratings = map(lambda movie: {**movie, "average_rating": find_avg(movie)}, movies)

print()
# Task 2: Find the top rated movie - max(key=fn)
# Output should be "The Dark Knight"
# Key is which value to use when looking for the maximum, so the average rating
top_rated_movie = max(ratings_movies, key=lambda x: x["average_rating"])
pprint(f"{top_rated_movie['title']} is the most top rated movie")

print()
# Task 3: Get the movie titles with average rating >= 4.6
# Output is a list of titles ['intersteller', ]
high_rates_movie = filter(lambda movie: get_avg(movie) >= 4.6, movies)
titles_only = list(map(lambda movie: movie["title"], high_rates_movie))
print(titles_only)

print()
# Task 4: Get the movies in order of rating
ordered_rated_movies = sorted(ratings_movies, key=lambda x: x["average_rating"], reverse=True)
ordered_only_titles = list(map(lambda movie: movie["title"], ordered_rated_movies))
pprint(" ,".join(ordered_only_titles[0:3]))