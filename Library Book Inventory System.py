from datetime import datetime

class Library:
    def __init__(self): # Presaved Books
        self.inventory = {
            "9780747573609": {
                "title": "Harry Potter and the Philosopher's Stone",
                "author": "J.K. Rowling",
                "genre": "Fantasy",
                "publisher": "Bloomsbury",
                "publication_date": "1997-06-26",
                "status": "Available"
            },
            "9780547928227": {
                "title": "The Hobbit",
                "author": "J.R.R. Tolkien",
                "genre": "Fantasy",
                "publisher": "George Allen & Unwin",
                "publication_date": "1937-09-21",
                "status": "Available"
            },
             "9780441172719": {
                "title": "Dune",
                "author": "Frank Herbert",
                "genre": "Science Fiction",
                "publisher": "Chilton Books",
                "publication_date": "1965-08-01",
                "status": "Available"
            },
             "9780007136834": {
                "title": "And Then There Were None",
                "author": "Agatha Christie",
                "genre": "Mystery",
                "publisher": "Collins Crime Club",
                "publication_date": "1939-11-06",
                "status": "Available"
            },
             "9780316015844": {
                "title": "Twilight",
                "author": "Stephenie Meyer",
                "genre": "Young Adult / Fantasy Romance",
                "publisher": "Little, Brown and Company",
                "publication_date": "2005-10-05",
                "status": "Available"
            },
             "9780141439518": {
                "title": "Pride and Prejudice",
                "author": "Jane Austen",
                "genre": "Classic Romance",
                "publisher": "T. Egerton, Whitehall",
                "publication_date": "1813-01-28",
                "status": "Available"
            },
             "9780061122415": {
                "title": "The Alchemist",
                "author": "Paulo Coelho",
                "genre": "Fiction / Philosophy",
                "publisher": "HarperTorch",
                "publication_date": "1988-01-01",
                "status": "Available"
            }
        }

    def book_add(self): # Add a Book
        print("\n--- ADD A BOOK ---")
        isbn = input("Enter ISBN (must be 13 digits): ").strip()
        title = input("Enter the title of the book: ").strip()
        author = input("Enter the author: ").strip()
        genre = input("Enter the genre: ").strip()
        publisher = input("Enter the publisher: ").strip()
        pub_date = input("Enter publication date (YYYY-MM-DD): ").strip()

        if not title or not author or not genre or not publisher or not pub_date:
            print("❌ Book not added. All fields must be filled.\n")
            return False

        if len(isbn) != 13 or not isbn.isdigit():
            print("❌ Book not added. ISBN must be exactly 13 digits.\n")
            return False

        if isbn in self.inventory:
            print(f"❌ A book with ISBN {isbn} already exists.\n")
            return False

        self.inventory[isbn] = {
            "title": title,
            "author": author,
            "genre": genre,
            "publisher": publisher,
            "publication_date": pub_date,
            "status": "Available"
        }
        print(f"✅ Book '{title}' by {author} has been added.\n")
        return True

    def edit_book(self): # Edit Book
        if not self.inventory:
            print("📭 No books to edit!\n")
            return

        print("\n--- EDIT BOOK ---")
        isbn = input("Enter ISBN to edit: ").strip()

        if isbn not in self.inventory:
            print("❌ Book not found!\n")
            return

        book = self.inventory[isbn]
        print(
            f"\nBook Info:\n"
            f"Title: {book['title']}\nAuthor: {book['author']}\nGenre: {book['genre']}\n"
            f"Publisher: {book['publisher']}\nPublication Date: {book['publication_date']}\n"
            f"Status: {book['status']}\n"
            f"{'Borrower: ' + book['borrower'] if 'borrower' in book else ''}"
        )

        print("\nWhat would you like to do?")
        print("1. Borrow this book")
        print("2. Return this book")
        print("3. Change status manually (Available/Borrowed)")
        print("4. Edit book information")
        print("5. Cancel")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":  # Borrow
            if book["status"] == "Borrowed":
                print("❌ Book is already borrowed.\n")
                return
            borrower = input("Enter borrower's name: ").strip()
            if not borrower:
                print("❌ Borrower name cannot be empty.\n")
                return
            book["status"] = "Borrowed"
            book["borrower"] = borrower
            book["borrow_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"✅ Book borrowed by {borrower} on {book['borrow_date']}.\n")

        elif choice == "2":  # Return
            if book["status"] == "Available":
                print("❌ Book is not borrowed.\n")
                return
            book["status"] = "Available"
            book.pop("borrower", None)
            book.pop("borrow_date", None)
            print("✅ Book returned successfully.\n")

        elif choice == "3":  # Manual status edit
            new_status = input("Enter new status (Available/Borrowed): ").strip().capitalize()
            if new_status in ["Available", "Borrowed"]:
                book["status"] = new_status
                if new_status == "Available":
                    book.pop("borrower", None)
                    book.pop("borrow_date", None)
                print(f"✅ Book status updated to {new_status}.\n")
            else:
                print("❌ Invalid status.\n")

        elif choice == "4":  # Edit book info
            print("\n--- EDIT BOOK INFORMATION ---")
            new_title = input(f"Enter new title (current: {book['title']}): ").strip()
            new_author = input(f"Enter new author (current: {book['author']}): ").strip()
            new_genre = input(f"Enter new genre (current: {book['genre']}): ").strip()
            new_publisher = input(f"Enter new publisher (current: {book['publisher']}): ").strip()
            new_pub_date = input(f"Enter new publication date (current: {book['publication_date']}): ").strip()

            book["title"] = new_title or book["title"]
            book["author"] = new_author or book["author"]
            book["genre"] = new_genre or book["genre"]
            book["publisher"] = new_publisher or book["publisher"]
            book["publication_date"] = new_pub_date or book["publication_date"]
            print("✅ Book information updated successfully.\n")

        else:
            print("❌ Edit cancelled.\n")

    def delete_book(self): #Delete
        if not self.inventory:
            print("📭 No books to delete!\n")
            return
        
        print("\n--- DELETE BOOK ---")
        isbn = input("Enter ISBN to delete: ").strip()
        
        if isbn in self.inventory:
            confirm = input(f"Are you sure you want to delete '{self.inventory[isbn]['title']}'? (y/n): ").lower()
            if confirm == 'y':
                del self.inventory[isbn]
                print("✅ Book deleted!\n")
            else:
                print("❌ Not deleted.\n")
        else:
            print("❌ Book not found!\n")

    def list_books(self): # List all Books
        if not self.inventory:
            print("📭 Inventory is empty.\n")
            return

        print("\n📚 Library Inventory:")
        print("-" * 110)
        for isbn, details in self.inventory.items():
            borrow_info = f" | Borrower: {details.get('borrower', '-')}" if details["status"] == "Borrowed" else ""
            borrow_date = f" | Borrowed On: {details.get('borrow_date', '-')}" if details["status"] == "Borrowed" else ""
            print(
                f"ISBN: {isbn} | Title: {details['title']} | Author: {details['author']} | "
                f"Genre: {details['genre']} | Publisher: {details['publisher']} | "
                f"Pub Date: {details['publication_date']} | Status: {details['status']}{borrow_info}{borrow_date}"
            )
        print("-" * 110 + "\n")

        # Sub-option for search
        choice = input("Would you like to search for a book? (y/n): ").lower()
        if choice == "y":
            keyword = input("Enter ISBN, title, or author to search: ").strip().lower()
            results = []
            for isbn, details in self.inventory.items():
                if (
                    keyword in isbn.lower() or
                    keyword in details["title"].lower() or
                    keyword in details["author"].lower()
                ):
                    results.append((isbn, details))
            if results:
                print("\n🔍 Search Results:")
                for isbn, details in results:
                    borrow_info = f" | Borrower: {details.get('borrower', '-')}" if details["status"] == "Borrowed" else ""
                    borrow_date = f" | Borrowed On: {details.get('borrow_date', '-')}" if details["status"] == "Borrowed" else ""
                    print(
                        f"ISBN: {isbn} | Title: {details['title']} | Author: {details['author']} | "
                        f"Genre: {details['genre']} | Publisher: {details['publisher']} | "
                        f"Pub Date: {details['publication_date']} | Status: {details['status']}{borrow_info}{borrow_date}"
                    )
            else:
                print("❌ No matching books found.\n")


def main():
    print("\n=== Stitches Library Book Inventory System ===")
    print("1. 📚 Add a book to the inventory")
    print("2. 📝 Edit book (borrow/return/status/info)")
    print("3. ⛔ Delete a book from the inventory")
    print("4. 📃 List all books (with search)")
    print("5. ❌ Exit the program")
    choice = input("Enter your choice (1-5): ").strip()
    return choice


if __name__ == "__main__":
    library_system = Library()

    while True:
        choice = main()
        if choice == "1":
            library_system.book_add()
        elif choice == "2":
            library_system.edit_book()
        elif choice == "3":
            library_system.delete_book()
        elif choice == "4":
            library_system.list_books()
        elif choice == "5":
            print("👋 Exiting program. Goodbye!\n")
            break
        else:
            print("❌ Invalid choice. Please enter 1-5.\n")
