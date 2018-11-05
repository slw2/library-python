class Loans:

    books = ""
    users = ""
    database = ""

    def __init__(self, books, users, database):
        self.books = books
        self.users = users
        self.database = database
  
    def borrow(self, book, user):
        self.database.cursor.execute('''SELECT book_code FROM loans WHERE book_code = ?''', (book.code,))
        data = self.database.cursor.fetchone()
        if data is None:
            self.database.cursor.execute('''INSERT INTO loans(book_code, user_code)
                                            VALUES(?,?)''', (book.code, user.code))
            self.database.db.commit()
            return True
        else:
            return False

    def return_book(self, book):
        self.database.cursor.execute('''DELETE FROM loans WHERE book_code = ?''', (book.code,))

    def loans(self, user):
        on_loan = []
        self.database.cursor.execute('''SELECT book_code FROM loans WHERE user_code = ?''', (user.code,))
        allrows = self.database.cursor.fetchall()
        for row in allrows:
            on_loan.append(self.books.booksearch_by_code(row[0]))
        return on_loan

    def books_loaned(self):
        books_on_loan = []
        self.database.cursor.execute('''SELECT book_code FROM loans''')
        allrows = self.database.cursor.fetchall()
        for row in allrows:
            books_on_loan.append(self.books.booksearch_by_code(row[0]))
        return books_on_loan

    def books_not_loaned(self):
        books_in_lib = []
        self.database.cursor.execute('''SELECT code FROM books WHERE code NOT IN
                                        (SELECT book_code FROM loans)''')
        allrows = self.database.cursor.fetchall()
        for row in allrows:
            books_in_lib.append(self.books.booksearch_by_code(row[0]))
        return books_in_lib

    def users_with_loans(self):
        loaners = []
        self.database.cursor.execute('''SELECT user_code FROM loans''')
        allrows = self.database.cursor.fetchall()
        for row in allrows:
            loaners.append(self.users.usersearch_by_code(row[0]))
        return loaners
