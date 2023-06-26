class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"You have borrowed '{book.title}' by {book.author}.")
        else:
            print("Sorry, the book is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"You have returned '{book.title}' by {book.author}.")
        else:
            print("You haven't borrowed this book.")

class Admin:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def add_book(self, library, title, author):
        book = Book(title, author)
        library.books.append(book)
        print(f"'{book.title}' by {book.author} has been added to the library.")

class Library:
    def __init__(self):
        self.books = []

    def display_available_books(self):
        print("Available books:")
        for book in self.books:
            if book.available:
                print(f"'{book.title}' by {book.author}")


library = Library()
admin = Admin("admin@example.com", "adminpassword")
user = User("user@example.com", "userpassword")
admin.add_book(library, "Book 1", "Author 1")
admin.add_book(library, "Book 2", "Author 2")
library.display_available_books()
user.borrow_book(library.books[0])
user.borrow_book(library.books[0])
user.return_book(library.books[0])
user.return_book(library.books[0])
library.display_available_books()
