movies = []


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


def show_movies():
    for movie in movies:
        print(movie)


def find_movie():
    title = input("Enter the movie title: ")
    for movie in movies:
        if movie["title"] == title:
            print(movie)
            break
    else:
        print(f'Such movie {title} do not exist.')


MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see a movies, 'f' to find a movie by title or 'q' to quit: "

selection = input(MENU_PROMPT)

while selection != "q":
    if selection == "a":
        add_movie()
    elif selection == "l":
        show_movies()
    elif selection == "f":
        find_movie()
    else:
        print("Unknown command. Please try again!")

    selection = input(MENU_PROMPT)
