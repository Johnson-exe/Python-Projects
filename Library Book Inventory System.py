print("Library Book Inventory System")
print("-----------------------------------")
menu_choice = int(input("1. Add Book\n2. Edit Book Status\n3. Delete a Book\n4. Check All Books\n5. Exit\nEnter Choice: "))

match menu_choice:
    case 1:
        print("Add Book")
    case 2:
        print("Edit Book Status")
    case 3:
        print("Delete a Book")
    case 4:
        print("List All Books")
    case 5:
        print("Exiting...")
    case _:
        print("Invalid Choice")

    