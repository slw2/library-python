from Book import Book
import random

class Books:

    database = ""

    def __init__(self, database):
        self.database = database

    def books(self):
        self.database.cursor.execute('''SELECT title, author, code FROM books''')
        allrows = self.database.cursor.fetchall()
        list_of_books = []
        for row in allrows:
            newBook = Book()
            newBook.init(row[0], row[1], row[2])
            list_of_books.append(newBook)
        return list_of_books

    def booksearch_by_title(self, title):
        bookList = self.books()
        books_with_title = []
        for book in bookList:
            if book.title == title:
                books_with_title.append(book)
        return books_with_title

    def booksearch_by_author(self, author):
        bookList = self.books()
        books_by_author = []
        for book in bookList:
            if book.author == author:
                books_by_author.append(book)
        return books_by_author

    def booksearch_by_code(self, code):
        bookList = self.books()
        for book in bookList:
            if book.code == code:
                return book
        return False

    def add_book(self, title, author):
        code = random.randint(1, 1000)
        while self.booksearch_by_code(code) != False:
            code = random.randint(1, 1000)
        self.database.cursor.execute('''INSERT INTO books(title, author, code) 
                                        VALUES(?,?,?)''', (title, author, code))
        self.database.db.commit()

    def remove_book(self, book):
        self.database.cursor.execute('''DELETE FROM books WHERE code = ? ''', (book.code,))
        self.database.db.commit()