class Book:
    def __init__(self, name):
        self.name = name
        self.available = True


class Patron:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self):
        name = input("Enter book name: ")
        self.books.append(Book(name))
        print("Book added.")

    def register_patron(self):
        name = input("Enter patron name: ")
        self.patrons.append(Patron(name))
        print("Patron registered.")

    def borrow_book(self):
        name = input("Enter book name: ")
        for book in self.books:
            if book.name == name:
                if book.available:
                    book.available = False
                    print("Book borrowed.")
                else:
                    print("Book not available.")
                return
        print("Book not found.")

    def return_book(self):
        name = input("Enter book name: ")
        for book in self.books:
            if book.name == name:
                book.available = True
                print("Book returned.")
                return
        print("Book not found.")


library = Library()

while True:
    print("\n----- Library Menu -----")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_book()
    elif choice == 2:
        library.register_patron()
    elif choice == 3:
        library.borrow_book()
    elif choice == 4:
        library.return_book()
    elif choice == 5:
        print("Thank You!")
        break
    else:
        print("Invalid Choice")
