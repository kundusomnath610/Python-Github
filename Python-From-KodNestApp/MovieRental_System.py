def add_movie(title, available_movies):
    if title not in available_movies:
        available_movies.append(title)

def search_movie(title, available_movies):
    if title in available_movies:
        print(f"'{title}' is available in the collection.")
    else:
        print(f"'{title}', is not available in Movie List")


def view_movies(available_movies):
    print(f"Available movies: {available_movies}")

available_movies = ['The Matrix', 'Interstellar', 'The Godfather']

view_movies(available_movies)

add_movie('Inception', available_movies)

view_movies(available_movies)

search_movie('The Matrix', available_movies)

search_movie('The Godfather', available_movies)
    