import sqlite3

class Database:
    db = sqlite3.connect('mydb')
    cursor = db.cursor()


