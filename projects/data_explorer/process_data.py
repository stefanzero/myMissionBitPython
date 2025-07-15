# read the files in the subdirectory IMDB and return the root names of the files

import json
from operator import ge
import os
from pathlib import Path  # pathlib module is object-oriented
from os import path
import csv
import random
from pprint import pprint

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

GENRES = [
    "crime",
    "horror",
    "history",
    "romance",
    "film-noir",
    "family",
    "animation",
    "mystery",
    "sports",
    "adventure",
    "scifi",
    "fantasy",
    "war",
    "action",
    "thriller",
    "biography",
]

KEYS = [
    "movie_id",
    "movie_name",
    "year",
    "certificate",
    "runtime",
    "genre",
    "rating",
    "description",
    "director",
    "director_id",
    "star",
    "star_id",
    "votes",
    "gross(in $)",
]

print("beginning process_data.py")


def extract_genres():
    """
    Extracts and returns a list of genre names from files in the 'IMDB' directory.

    Each file in the 'IMDB' directory is expected to have a name corresponding to a genre
    followed by a file extension. This function reads the directory, extracts the genre
    names by removing the file extension, and compiles the genre names into a list.

    Returns:
        list: A list of genre names extracted from the files in the 'IMDB' directory.
    """

    imdb_dir = Path("./IMDB")
    genres = []
    for file in imdb_dir.iterdir():
        genre = file.name.split(".")[0]
        genres.append(genre)
    return genres


# read the csv file for the genre
def load_movies(genre):
    # check that file exists
    if path.exists(f"IMDB/{genre}.csv"):
        with open(f"IMDB/{genre}.csv", "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    else:
        print(f"File does not exist: IMDB/{genre}.csv")
        return None


def get_all_movies():
    all_movies = []
    imdb_dir = Path("./IMDB")
    for file in imdb_dir.iterdir():
        genre = file.name.split(".")[0]
        data = load_movies(genre)
        all_movies.extend(data)
    return all_movies


def get_all_movies_and_key_by_genre():
    all_movies = {}
    imdb_dir = Path("./IMDB")
    for file in imdb_dir.iterdir():
        genre = file.name.split(".")[0]
        data = load_movies(genre)
        all_movies[genre] = data
    return all_movies


def extract_keys(data):
    return list(data[0].keys())


def get_movie_recommendation(movie):
    rating = movie["rating"]
    if rating > 8:
        return "Great movie!"
    elif rating > 5:
        return "Okay movie."
    else:
        return "Not worth watching."


def print_movie_titles(movies):
    for movie in movies:
        print(f"{movie['movie_name']}")


# sum of the ratings of the movies
def sum_ratings(movies):
    total = 0
    for movie in movies:
        total += movie["rating"]
    return total


def print_movie_title_and_ratings(movies):
    for movie in movies:
        print(f"{movie['movie_name']} ({movie['rating']})")


def get_highest_rated_movie(movies):
    highest_rating = 0
    highest_rated_movie = None
    for movie in movies:
        if movie["rating"] > highest_rating:
            highest_rating = movie["rating"]
            highest_rated_movie = movie
    return highest_rated_movie


"""
genres = extract_genres()
print(genres)

for genre in genres:
    data = load_movies(genre)
    print(extract_keys(data))

selected_genre = random.choice(genres)
"""


def calculate_average_ratings(movies):
    total = 0
    for movie in movies:
        total += float(movie["rating"])
    return total / len(movies)


def find_highest_rated_movie(movies):
    highest_rating = 0
    highest_rated_movie = None
    for movie in movies:
        if movie["rating"] > highest_rating:
            highest_rating = movie["rating"]
            highest_rated_movie = movie
    return highest_rated_movie


def filter_by_genre(movies, genre):
    filtered_movies = []
    for movie in movies:
        if movie["genre"] == genre:
            filtered_movies.append(movie)
    return filtered_movies


# genre = "crime"
# print("Loading crime movies...")
# crime_movies = load_movies("crime")
# print(f"Number of crime movies: {len(crime_movies)}")
# print(json.dumps(crime_movies, indent=2))
# pprint(crime_movies)

"""
Integrate functions with the lists and loops practiced earlier:
Use the calculate_average_rating() function on a list of movie ratings.
Apply the find_highest_rated() function to a list of movies to identify the top-rated one.
Implement filter_by_genre() to filter and analyze the movie dataset.
"""


"""
✏️Task 1: Choose a genre and download a dataset from the link.
✏️Task 2: Write a function load_movies(filename) to read movie data from a file into a list. 
✏️Task 3: Using the functions you created earlier, perform a data analysis of your movie dataset. This can include calculating average ratings, finding the highest rated movie, and more.
✏️Task 4: Write a function save_analysis(results, filename) to save analysis results to a text file. 
Note: You may need to update your functions to match the format of the new dataset. Make sure they can handle different types of data.
"""


def perform_data_analysis():
    analyzed_data = {}
    for genre in GENRES:
        movies = load_movies(genre)
        average_rating = calculate_average_ratings(movies)
        highest_rated_movie = find_highest_rated_movie(movies)
        filtered_movies = filter_by_genre(movies, genre)
        analyzed_data[genre] = {
            "average_rating": average_rating,
            "highest_rated_movie": highest_rated_movie,
            "filtered_movies": filtered_movies,
        }
        # print(f"Genre: {genre}")
        # print(f"Average rating: {average_rating}")
        # print(f"Highest-rated movie: {highest_rated_movie}")
        # print(f"Filtered movies: {filtered_movies}")
        # print("\n")
    return analyzed_data


def save_analysis(analyzed_data):
    for genre in GENRES:
        with open(f"{genre}_analysis.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerows(analyzed_data[genre])

            # file.write(f"Genre: {genre}\n")
            # file.write(f"Average rating: {analyzed_data[genre]['average_rating']}\n")
            # file.write(
            #     f"Highest-rated movie: {analyzed_data[genre]['highest_rated_movie']}\n"
            # )
            # file.write(f"Filtered movies: {analyzed_data[genre]['filtered_movies']}\n")


# analyzed_data = perform_data_analysis()
# save_analysis(analyzed_data)
# pprint(get_all_movies())


def find_movies_with_no_ratings(movies):
    no_rating_movies = []
    for movie in movies:
        if movie["rating"] == "":
            no_rating_movies.append(movie)
    return no_rating_movies


movies = get_all_movies()
no_ratings = find_movies_with_no_ratings(movies)
print(f"Number of genres: {len(GENRES)}")
print(f"Number of movies: {len(movies)}")
print(f"Number of movies with no ratings: {len(no_ratings)}")
