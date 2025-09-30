"""
Extract a subset of the data from the original data file and save it to a new file.
"""

import os
import random
import json
import csv
from pathlib import Path  # pathlib module is object-oriented

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)


def set_dir():
    script_dir = os.path.dirname(__file__)
    os.chdir(script_dir)


def load_movies(genre):
    # check that file exists
    if os.path.exists(f"IMDB/{genre}.csv"):
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


def save_to_file(movies=get_all_movies(), num_movies=10, min_rating=6):
    SELECTED_KEYS = ["movie_name", "rating", "genre"]
    selected_movies = []
    random.shuffle(movies)
    while num_movies:
        movie = movies.pop()
        if movie["rating"] != "" and float(movie["rating"]) >= min_rating:
            movie["genre"] = movie["genre"].split(", ")
            selected_data = [movie[key] for key in SELECTED_KEYS]
            selected_movies.append(selected_data)
            num_movies -= 1
    with open("random_movies.json", "w") as f:
        json.dump(obj=selected_movies, indent=2, fp=f)


def run():
    # set_dir()
    save_to_file()


if __name__ == "__main__":
    run()
