import os

class Library:
    def __init__(self, filename="library.txt"):
        self.filename = filename
        self.books = []
        self.load_from_file()

    # ---------------- FILE HANDLING ----------------
    def load_from_file(self):
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r") as file:
                for line in file:
                    data = line.strip().split("|")
                    if len(data) == 4:
                        book = {
                            "id": int(data[0]),
                            "title": data[1],
                            "author": data[2],
                            "is_issued": data[3] == "True"
                        }
                        self.books.append(book)
        except Exception as e:
            print("Error loading file:", e)

    def save_to_file(self):
        try:
            with open(self.filename, "w") as file:
                for book in self.books:
                    file.write(f"{book['id']}|{book['title']}|{book['author']}|{book['is_issued']}\n")
        except Exception as e:
            print("Error saving file:", e)

    # ---------------- ADD BOOK ----------------
    def add_book(self):
        try:
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()

            # Check duplicate ID
            for book in self.books:
                if book["id"] == book_id:
                    raise ValueError("Book ID already exists!")

            new_book = {
                "id": book_id,
                "title": title,
                "author": author,
                "is_issued": False
            }

            self.books.append(new_book)
            self.save_to_file()
            print("Book added successfully!")

        except ValueError as ve:
            print("Error:", ve)
        except Exception:
            print("Invalid input! Please try again.")

    # ---------------- VIEW BOOKS ----------------
    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            print("\n------------------------")
            print("ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Status:", "Issued" if book["is_issued"] else "Available")
        print("------------------------")

    # ---------------- SEARCH BOOK ----------------
    def search_book(self):
        keyword = input("Enter title to search: ").lower()

        found = False
        for book in self.books:
            if keyword in book["title"].lower():
                print("\nBook Found:")
                print("ID:", book["id"])
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Status:", "Issued" if book["is_issued"] else "Available")
                found = True

        if not found:
            print("Book not found.")

    # ---------------- ISSUE BOOK ----------------
    def issue_book(self):
        try:
            book_id = int(input("Enter Book ID to issue: "))
            for book in self.books:
                if book["id"] == book_id:
                    if book["is_issued"]:
                        print("Book already issued!")
                    else:
                        book["is_issued"] = True
                        self.save_to_file()
                        print("Book issued successfully!")
                    return
            print("Book not found!")
        except ValueError:
            print("Invalid ID!")

    # ---------------- RETURN BOOK ----------------
    def return_book(self):
        try:
            book_id = int(input("Enter Book ID to return: "))
            for book in self.books:
                if book["id"] == book_id:
                    if not book["is_issued"]:
                        print("Book was not issued!")
                    else:
                        book["is_issued"] = False
                        self.save_to_file()
                        print("Book returned successfully!")
                    return
            print("Book not found!")
        except ValueError:
            print("Invalid ID!")

    # ---------------- DELETE BOOK ----------------
    def delete_book(self):
        try:
            book_id = int(input("Enter Book ID to delete: "))
            for book in self.books:
                if book["id"] == book_id:
                    self.books.remove(book)
                    self.save_to_file()
                    print("Book deleted successfully!")
                    return
            print("Book not found!")
        except ValueError:
            print("Invalid ID!")

# ---------------- MAIN PROGRAM ----------------
def main():
    library = Library()

    while True:
        print("\n====== Library Management System ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.search_book()
        elif choice == "4":
            library.issue_book()
        elif choice == "5":
            library.return_book()
        elif choice == "6":
            library.delete_book()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()