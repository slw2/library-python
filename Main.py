from Books import Books
from Users import Users
from UserController import UserController
from BookController import BookController
from LoanController import LoanController
from Loans import Loans
from Database import Database

print("Welcome to the library\n")

database = Database()
books = Books(database)
users = Users(database)
loans = Loans(books, users, database)
userController = UserController(books, users, loans)
bookController = BookController(books, users, loans)
loanController = LoanController(books, users, loans)


def top_menu():
    print("Option 1: List all users")
    print("Option 2: List all books")
    print("Option 3: Search for a user")
    print("Option 4: Search for a book")
    print("Option 5: Borrow a book")
    print("Option 6: Return a book")
    print("Option 7: Check my loans")
    print("Option 8: Add a user")
    print("Option 9: Remove a user")
    print("Option 10: Add a book")
    print("Option 11: Remove a book")
    print("Option 12: List books on loan")
    print("Option 13: List books not on loan")
    print("Option 14: List users with loans")
    choice = input("Select an option: ")
    if choice == "1":
        userController.print_users()
    elif choice == "2":
        bookController.print_books()
    elif choice == "3":
        search_user_menu()
    elif choice == "4":
        search_book_menu()
    elif choice == "5":
        borrow_menu()
    elif choice == "6":
        return_menu()
    elif choice == "7":
        check_loans()
    elif choice == "8":
        add_a_user()
    elif choice == "9":
        remove_a_user()
    elif choice == "10":
        add_a_book()
    elif choice == "11":
        remove_a_book()
    elif choice == "12":
        loanController.print_books_loaned()
    elif choice == "13":
        loanController.print_books_not_loaned()
    elif choice == "14":
        loanController.print_users_with_loans()


def search_user_menu():
    print("Option 1: Search by first name")
    print("Option 2: Search by last name")
    print("Option 3: Search by code")
    choice = input("Select an option: ")
    if choice == "1":
        first_name = input("Please enter a first name: ")
        userController.usersearch(1, first_name)
    elif choice == "2":
        last_name = input("Please enter a last name: ")
        userController.usersearch(2, last_name)
    elif choice == "3":
        code = int(input("Please enter a code: "))
        userController.usersearch(3, code)

def search_book_menu():
    print("Option 1: Search by title")
    print("Option 2: Search by author")
    print("Option 3: Search by code")
    choice = input("Select an option: ")
    if choice == "1":
        title = input("Please enter a book title: ")
        bookController.booksearch(1, title)
    elif choice == "2":
        author = input("Please enter an author: ")
        bookController.booksearch(2, author)
    elif choice == "3":
        code = int(input("Please enter a code: "))
        bookController.booksearch(3, code)

def borrow_menu():
    user = int(input("Please enter your user code: "))
    book = int(input("Please enter the book code of the book you want to borrow: "))
    loanController.borrow(book, user)

def return_menu():
    book = int(input("Please enter the book code of the book you want to return: "))
    loanController.return_book(book)

def check_loans():
    user = int(input("Please enter your user code: "))
    loanController.user_loans(user)

def add_a_user():
    first_name = input("Please enter a first name: ")
    last_name = input("Please enter a last name: ")
    userController.add_user(first_name, last_name)

def remove_a_user():
    user = int(input("Please enter the user code of the user you want to remove: "))
    userController.remove_user(user)

def add_a_book():
    title = input("Please enter the title: ")
    author = input("Please enter the author: ")
    bookController.add_book(title, author)

def remove_a_book():
    book = int(input("Please enter the book code of the book you want to remove: "))
    bookController.remove_book(book)

while True:
    top_menu()