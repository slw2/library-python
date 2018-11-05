class UserController:

    books = ""
    users = ""
    loans = ""

    def __init__(self, books, users, loans):
        self.books = books
        self.users = users
        self.loans = loans

    def usersearch(self, choice, input):
        if choice == 1:
            list_of_users = self.users.usersearch_by_firstname(input)
            if list_of_users == []:
                print("No search results")
            else:
                for user in list_of_users:
                    user.print()
        elif choice == 2:
            list_of_users = self.users.usersearch_by_lastname(input)
            if list_of_users == []:
                print("No search results")
            else:
                for user in list_of_users:
                    user.print()
        elif choice == 3:
            user = self.users.usersearch_by_code(input)
            if not user:
                print("No search results")
            else:
                user.print()

    def print_users(self):
        all_users = self.users.users()
        if all_users == []:
            print("There are currently no users")
        else:
            for user in all_users:
                user.print()

    def add_user(self, first_name, last_name):
        self.users.add_user(first_name, last_name)
        print("The user has been added")

    def remove_user(self, user_code):
        user = self.users.usersearch_by_code(user_code)
        if not user:
            print("User not found")
        elif user in self.loans.users_with_loans():
            print("This user has loans")
        else:
            self.users.remove_user(user)
            print("User successfully removed")

