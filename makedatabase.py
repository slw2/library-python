import sqlite3

db = sqlite3.connect('mydb')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE loans(book_code INTEGER, user_code INTEGER)
''')
db.commit()

#loans = []
#cursor.executemany(''' INSERT INTO books(title, author, code) VALUES(?,?,?)''', books)
#db.commit()