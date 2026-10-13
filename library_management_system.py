# Library Management System


from abc import ABC, abstractmethod


class LibraryItem(ABC):

    def __init__(self, item_id, title, year):
        self.__item_id = item_id
        self.title = title
        self.year = year
        self.__is_issued = False

    def get_item_id(self):
        return self.__item_id

    def get_issue_status(self):
        return self.__is_issued

    def issue_item(self):
        if not self.__is_issued:
            self.__is_issued = True
            print("Item issued successfully!")
        else:
            print("Item is already issued.")

    def return_item(self):
        if self.__is_issued:
            self.__is_issued = False
            print("Item returned successfully!")
        else:
            print("Item is not currently issued.")

    def update_details(self, title, year):
        self.title = title
        self.year = year
        print("Item updated successfully!")

    @abstractmethod
    def display_details(self):
        pass


class Book(LibraryItem):

    def __init__(self, item_id, title, year, author):
        super().__init__(item_id, title, year)
        self.author = author

    def display_details(self):
        print("\n----- BOOK -----")
        print("ID:", self.get_item_id())
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)

        if self.get_issue_status():
            print("Status: Issued")
        else:
            print("Status: Available")


class Magazine(LibraryItem):

    def __init__(self, item_id, title, year, issue_number):
        super().__init__(item_id, title, year)
        self.issue_number = issue_number

    def display_details(self):
        print("\n----- MAGAZINE -----")
        print("ID:", self.get_item_id())
        print("Title:", self.title)
        print("Issue Number:", self.issue_number)
        print("Year:", self.year)

        if self.get_issue_status():
            print("Status: Issued")
        else:
            print("Status: Available")


library_items = []


def find_item(item_id):

    for item in library_items:
        if item.get_item_id() == item_id:
            return item

    return None


def add_item():

    print("\n----- ADD LIBRARY ITEM -----")
    print("1. Book")
    print("2. Magazine")

    item_type = input("Choose item type: ")

    if item_type not in ("1", "2"):
        print("Invalid item type.")
        return

    item_id = input("Enter item ID: ")

    if find_item(item_id) is not None:
        print("This item ID already exists.")
        return

    title = input("Enter title: ")

    try:
        year = int(input("Enter publication year: "))

        if year <= 0:
            raise ValueError

    except ValueError:
        print("Please enter a valid year.")
        return

    if item_type == "1":
        author = input("Enter author: ")
        item = Book(item_id, title, year, author)

    elif item_type == "2":
        issue_number = input("Enter issue number: ")
        item = Magazine(item_id, title, year, issue_number)

    library_items.append(item)

    print("Item added successfully!")


def view_items():

    if len(library_items) == 0:
        print("No library items found.")
        return

    for item in library_items:
        item.display_details()


def issue_item():

    item_id = input("Enter item ID to issue: ")
    item = find_item(item_id)

    if item is None:
        print("Item not found.")
        return

    item.issue_item()


def return_item():

    item_id = input("Enter item ID to return: ")
    item = find_item(item_id)

    if item is None:
        print("Item not found.")
        return

    item.return_item()


def update_item():

    item_id = input("Enter item ID to update: ")
    item = find_item(item_id)

    if item is None:
        print("Item not found.")
        return

    new_title = input("Enter new title: ")

    try:
        new_year = int(input("Enter new publication year: "))

        if new_year <= 0:
            raise ValueError

    except ValueError:
        print("Please enter a valid year.")
        return

    item.update_details(new_title, new_year)

    if isinstance(item, Book):
        item.author = input("Enter new author: ")

    elif isinstance(item, Magazine):
        item.issue_number = input("Enter new issue number: ")


def delete_item():

    item_id = input("Enter item ID to delete: ")
    item = find_item(item_id)

    if item is None:
        print("Item not found.")
        return

    if item.get_issue_status():
        print("Cannot delete an issued item.")
        return

    library_items.remove(item)

    print("Item deleted successfully!")


while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Item")
    print("2. View Items")
    print("3. Issue Item")
    print("4. Return Item")
    print("5. Update Item")
    print("6. Delete Item")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        view_items()

    elif choice == "3":
        issue_item()

    elif choice == "4":
        return_item()

    elif choice == "5":
        update_item()

    elif choice == "6":
        delete_item()

    elif choice == "7":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
