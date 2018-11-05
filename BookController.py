class BookController:

    books = ""
    users = ""
    loans = ""

    def __init__(self, books, users, loans):
        self.books = books
        self.users = users
        self.loans = loans

    def booksearch(self, choice, input):
        if choice == 1:
            list_of_books = self.books.booksearch_by_title(input)
            if list_of_books == []:
                print("No search results")
            else:
                for book in list_of_books:
                    book.print()
        elif choice == 2:
            list_of_books = self.books.booksearch_by_author(input)
            if list_of_books == []:
                print("No search results")
            else:
                for book in list_of_books:
                    book.print()
        elif choice == 3:
            book = self.books.booksearch_by_code(input)
            if not book:
                print("No search results")
            else:
                book.print()

    def print_books(self):
        all_books = self.books.books()
        if all_books == []:
            print("There are currently no books")
        else:
            for book in all_books:
                book.print()

    def add_book(self, title, author):
        self.books.add_book(title, author)
        print("The book has been added")

    def remove_book(self, book_code):
        book = self.books.booksearch_by_code(book_code)
        if not book:
            print("Book not found")
        elif book in self.loans.books_loaned():
            print("This book is on loan")
        else:
            self.books.remove_book(book)
            print("Book successfully removed")


