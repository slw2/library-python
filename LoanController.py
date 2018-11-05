class LoanController:

    books = ""
    users = ""
    loans = ""

    def __init__(self, books, users, loans):
        self.books = books
        self.users = users
        self.loans = loans

    def borrow(self, book_code, user_code):
        book = self.books.booksearch_by_code(book_code)
        user = self.users.usersearch_by_code(user_code)
        if not book:
            print("The book code does not match any books")
        elif not user:
            print("The user code does not match any users")
        elif book in self.loans.loans(user):
            print("You have already taken this book out")
        elif not self.loans.borrow(book, user):
            print("This book is already on loan")
        else:
            self.loans.borrow(book, user)
            print("You have successfully borrowed a book!")

    def return_book(self, book_code):
        book = self.books.booksearch_by_code(book_code)
        if not book:
            print("The book code does not match any books")
        else:
            self.loans.return_book(book)
            print("You have successfully returned the book!")

    def user_loans(self, user_code):
        user = self.users.usersearch_by_code(user_code)
        if not user:
            print("The user code does not match any users")
        on_loan = self.loans.loans(user)
        if on_loan == []:
            print("You have no books on loan")
        else:
            print("These are your loans: ")
            for book in on_loan:
                book.print()

    def print_books_loaned(self):
        books_loaned = self.loans.books_loaned()
        if books_loaned == []:
            print("There are currently no books on loan")
        else:
            for book in books_loaned:
                book.print()

    def print_books_not_loaned(self):
        books_not_loaned = self.loans.books_not_loaned()
        if books_not_loaned == []:
            print("There are no books currently available in the library")
        else:
            for book in books_not_loaned:
                book.print()

    def print_users_with_loans(self):
        users_with_loans = self.loans.users_with_loans()
        if users_with_loans == []:
            print("There are currently no users with loans")
        else:
            for user in users_with_loans:
                user.print()