class User:

    first_name = ""
    last_name = ""
    code = 0

    def init(self, first_name, last_name, code):
        self.first_name = first_name
        self.last_name = last_name
        self.code = code

    def print(self):
        print(self.first_name)
        print(self.last_name)
        print(self.code) 