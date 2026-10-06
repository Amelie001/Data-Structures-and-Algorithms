# Music Recommendation Engine

class Recommendation:
    def recommend(self):
        pass


class PopularSongs(Recommendation):
    def recommend(self):
        return ["Espresso", "Blinding Lights", "Cruel Summer"]


class HappySongs(Recommendation):
    def recommend(self):
        return ["Water", "Levitating", "Shake It Off"]


class RockSongs(Recommendation):
    def recommend(self):
        return ["Sweet Child O' Mine", "Don't Stop Me Now", "Bring Me to Life"]


popular = PopularSongs()
happy = HappySongs()
rock = RockSongs()


while True:
    print("\nMUSIC RECOMMENDATION ENGINE")
    print("1. Popular Songs")
    print("2. Happy Songs")
    print("3. Rock Songs")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        songs = popular.recommend()

    elif choice == "2":
        songs = happy.recommend()

    elif choice == "3":
        songs = rock.recommend()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number 1-4.")
        continue

    print("\nRecommended songs:")
    for song in songs:
        print("-", song)