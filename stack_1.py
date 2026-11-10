# Browser History Manager 

class BrowserHistory: 

    def __init__(self): 
        self.history = []

    def visit_website(self): 
        url = input("Enter website URL: ")

        self.history.append(url)

        print("Website visited successfully!")

    def display_history(self): 
        if len(self.history) == 0: 
            print("No browsing history available.")

        else: 
            print("\nBrowsing History:")

            for website in self.history: 
                print(website)

    def current_website(self): 
        if len(self.history) == 0:
            print("No webiste currently open.")

        else: 
            print("Current Website:", self.history[-1])

    def update_website(self): 
        if len(self.history) == 0: 
            print("History is empty.")

        else: 
            new_url = input("Enter updated URL: ")

            self.history[-1] = new_url

            print("Website updated successfully!")

    def go_back(self): 
        if len(self.history) == 0: 
            print("No previous website available.")

        else: 
            removed = self.history.pop()

            print("Going back from:", removed)

browser = BrowserHistory()

while True: 

    print("\n--- BROWSER HISTORY MANAGER ---")
    print("1. Visit website")
    print("2. Display history")
    print("3. Current Website")
    print("4. Update current website")
    print("5. Go back")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1": 
        browser.visit_website()

    elif choice == "2": 
        browser.display_history()

    elif choice == "3": 
        browser.current_website()

    elif choice == "4": 
        browser.update_website()

    elif choice == "5": 
        browser.go_back()

    elif choice == "6": 
        print("Thank you!")
        break

    else: 
        print("Invalid choice.")