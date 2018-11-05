from User import User
import random

class Users:

    database = ""

    def __init__(self, database):
        self.database = database

    def users(self):
        self.database.cursor.execute('''SELECT first_name, last_name, code FROM users''')
        allrows = self.database.cursor.fetchall()
        list_of_users = []
        for row in allrows:
            newUser = User()
            newUser.init(row[0], row[1], row[2])
            list_of_users.append(newUser)
        return list_of_users

    def usersearch_by_firstname(self, first_name):
        userList = self.users()
        users_with_firstname = []
        for user in userList:
            if user.first_name == first_name:
                users_with_firstname.append(user)
        return users_with_firstname

    def usersearch_by_lastname(self, last_name):
        userList = self.users()
        users_with_lastname = []
        for user in userList:
            if user.last_name == last_name:
                users_with_lastname.append(user)
        return users_with_lastname

    def usersearch_by_code(self, code):
        userList = self.users()
        for user in userList:
            if user.code == code:
                return user
        return False

    def add_user(self, first_name, last_name):
        code = random.randint(1, 1000)
        while self.usersearch_by_code(code) != False:
            code = random.randint(1, 1000)
        self.database.cursor.execute('''INSERT INTO users(first_name, last_name, code) 
                                        VALUES(?,?,?)''', (first_name, last_name, code))
        self.database.db.commit()

    def remove_user(self, user):
        self.database.cursor.execute('''DELETE FROM users WHERE code = ? ''', (user.code,))
        self.database.db.commit()