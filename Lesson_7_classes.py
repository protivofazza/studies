class Book:
    reads_now = ''

    def __init__(self, book_title, book_author, year_of_public, reads_now=None):
        self.book_title = book_title
        self.book_author = book_author
        self.year_of_public = year_of_public
        if reads_now:
            self.reads_now = reads_now      # Непонятно - сделал по аналогии

    def write_to_reader(self, reader):
        self.reads_now = reader


class BookCatalog(Book):
    books = [[], [], []]

    def __init__(self):
        self.books = Book.reads_now

    def book_issuance(self, date):
        self.books[1] = date

    def book_return(self, date):
        self.books[2] = date

    def find_a_book_by_author(self):
        pass

    def find_a_book_by_title(self):
        pass


