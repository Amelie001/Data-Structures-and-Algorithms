
movies = []

def add_movie(): 

    name = input("Enter movie name: ")
    rating = float(input("Enter rating (out of 10): "))

    if 0 <= rating <= 10: 
        movies.append([name, rating])
        print("Movie added!")

    else: 
        print("Rating must be between 0 and 10.")

def display_movies(movies): 

    if not movies: 
        print("No movies available.")

    else: 
        for movie in movies: 
            print(movie[0], "-", movie[1], "/ 10")

def bubble_sort():

    sorted_movies =  movies.copy()
    n = len(sorted_movies)

    for i in range(n):

        for j in range(n - i - 1): 

            if sorted_movies[j][1] < sorted_movies[j + 1][1]: 
            
                temp = sorted_movies[j]
                sorted_movies[j] = sorted_movies[j + 1]
                sorted_movies[j + 1] = temp
            
    print("\nSorted using Bubble Sort:")
    display_movies(sorted_movies)

def insertion_sort(): 

    sorted_movies = movies.copy()

    for i in range(1, len(sorted_movies)): 
        key = sorted_movies[i]
        j = i - 1

        while j >= 0 and sorted_movies[j][1] < key[1]: 
            sorted_movies[j + 1] = sorted_movies[j]
            j = j - 1

        sorted_movies[j + 1] = key 

    print("\nSorted using Insetion Sort:")
    display_movies(sorted_movies)

def merge(left, right): 

    result = []

    while len(left) > 0 and len(right) > 0: 

        if left[0][1] >= right[0][1]: 

            result.append(left[0])
            left.pop(0)

        else:

            result.append(right[0])
            right.pop(0)

        for movie in left:
            result.append(movie)

        for movie in right: 
            result.append(movie)

        return result 

def merge_sort(sorted_movies): 

    if len(sorted_movies) <= 1: 
        return sorted_movies

    mid = len(sorted_movies) // 2

    left = sorted_movies[:mid]
    right = sorted_movies[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def movie_ranking(): 

    if len(movies) == 0: 
        print("No movies found!")

    else: 
        sorted_data = merge_sort(movies.copy())

        print("Highest Rated Movie:", sorted_data[0])
        print("Lowest Rated Movie:", sorted_data[-1])

while True: 

    print("\n----- Movie Rating System -----")
    print("1. Add movie")
    print("2. Display all movies")
    print("3. Bubble sort")
    print("4. Insertion sort")
    print("5. Merge sort")
    print("6. Movie ranking")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1": 
        add_movie()

    elif choice == "2": 
        display_movies(movies)

    elif choice == "3": 
        bubble_sort()

    elif choice == "4": 
        insertion_sort()

    elif choice == "5": 
        sorted_movies = merge_sort(movies.copy())
        print("\nSorted using Merge Sort:")
        display_movies(sorted_movies)

    elif choice == "6": 
        movie_ranking()

    elif choice == "7": 
        print("Goodbye!")
        break 

    else: 
        print("Invalid choice. Please try again.")