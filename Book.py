class Book:

    title = ""
    author = ""
    code = 0

    def init(self, title, author, code):
        self.title = title
        self.author = author
        self.code = code

    def print(self):
        print(self.title)
        print(self.author)
        print(self.code)
