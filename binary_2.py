# Phone Directory 

contacts = ["Alice", "Amelie", "Ben", "Charlie", "Daniel", "Emma", "Harry", "James", "Olivia", "Sophie"]

name = input("Enter a contact name: ").lower()

low = 0
high = len(contacts) - 1
found = False 

while low <= high: 
    mid = (low + high) // 2

    if contacts[mid].lower() == name: 
        print("Contact found at index:", mid)
        found = True
        break 

    elif contacts[mid].lower() < name: 
        low = mid + 1

    else: 
        high = mid - 1 

if found == False: 
    print("Contact not found.")