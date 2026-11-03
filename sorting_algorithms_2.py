
movies = []

def add_movie(): 

    name = input("Enter movie name: ")
    rating = float(input("Enter rating (out of 10): "))

    if 0 <= rating <= 10: 
        movies.append([name, rating])
        print("Movie added!")

    else: 
        print("Rating must be between 0 and 10.")

def display_movies(): 

    if not movies: 
        print("No movies available.")

    else: 
        for movie in movies: 
            print(movie[0], "-", movie[1], "/ 10")

def bubble_sort():

    sorted_movies =  movies.copy()
    n = len(sorted_movies)

    for i in range(n): 
        for j in range(0, n - i - 1): 
            if sorted_movies[j][1] < sorted_movies[j + 1][1]: 
                sorted_movies[j], sorted_movies[j + 1] = (
                    sorted_movies[j + 1], sorted_movies[j]
                )

        return sorted_movies

def insertion_sort(): 

    sorted_movies = movies.copy()

    for i in range(1, len(sorted_movies)): 
        key = sorted_movies[i]
        j = i - 1

        while j >= 0 and sorted_movies[j][1] < key[1]: 
            sorted_movies[j + 1] = sorted_movies[j]
            j = j - 1

        