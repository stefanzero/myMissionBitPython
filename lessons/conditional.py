# a_or_b = input("Enter a or b: ")
# print("input accepted")
# print(a_or_b)
# # print(a_or_b == "a" or a_or_b == "b")

import json

movies = [
    ["The Hunger Games", 5, "action"],
    ["Frozen", 4, "adventure"],
    ["Toy Story", 4, "adventure"],
    ["Inside Out", 3, "adventure"],
    ["Coco", 3, "musical"],
]

movies_by_genre = {}
for movie in movies:
    genre = movie[2]
    if genre in movies_by_genre:
        movies_by_genre[genre].append(movie[0])
    else:
        movies_by_genre[genre] = [movie[0]]

print(json.dumps(movies_by_genre, indent=2))  # print(movies_by_genre)
