movies = []


# Add new movie to dictionary by user
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    genre = input("What type of genre is this movie: ")

    movies.append({
        "title": title,
        "director": director,
        "year": year,
        "genre": genre
    })


# Gives us a list of existing movies in the list
def show_movies():
    for movie in movies:
        print_movies(movie)


# Print info about movie
def print_movies(movie):
    print(f'Title: {movie["title"]}')
    print(f'Director: {movie["director"]}')
    print(f'Release year: {movie["year"]}')
    print(f'Movie genre: {movie["genre"]}')


# finds a movie by a title provided by user
def find_movie():
    title = input("Enter the movie title: ")
    for movie in movies:
        if movie["title"] == title:
            print_movies(movie)
            break
    else:
        print(f'Such movie {title} do not exist.')


MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see a movies, 'f' to find a movie by title or 'q' to quit: "
# defined dictionary with user options and actions
user_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movie
}


# Menu function with options for user to select
def menu():
    selection = input(MENU_PROMPT)
    while selection != "q":
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Unknown command. Please try again!")
        selection = input(MENU_PROMPT)


menu()
