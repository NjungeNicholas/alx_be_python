class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def list_available_books(self):
        """List all available books in the library."""
        for book in self._books:
            if not book._is_checked_out:
                print(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                print(f"Checked out: {book}")
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self):
        """Return a checked-out book by title."""
        for book in self._books:
            if book.title == book.title and book._is_checked_out:
                book._is_checked_out = False
                print(f"Returned: {book}")
                return
        print(f"Book '{book.title}' was not checked out.")