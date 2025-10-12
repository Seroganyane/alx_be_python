class Book:
    def __init__(self, title: str, author: str):
        """Initializes a Book instance with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a string representation of the book."""
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initializes an EBook instance with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns a string representation of the eBook."""
        return f"{super().__str__()} [EBook: {self.file_size}MB]"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initializes a PrintBook instance with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Returns a string representation of the print book."""
        return f"{super().__str__()} [PrintBook: {self.page_count} pages]"


class Library:
    def __init__(self):
        """Initializes a Library instance with an empty collection of books."""
        self.books = []

    def add_book(self, book: Book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book in the library."""
        for book in self.books:
            print(book)