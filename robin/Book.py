
class Book():
    
    def __init__(self, id, title, author, language, price):
        self.id = id
        self.title = title
        self.author = author
        self.language = language
        self.price = price.replace("\n", ",")

    def __str__(self):
        return f"Book: [ title: {self.title}, author: {self.author}, language: {self.language}, price: {self.price}, id: {self.id} ]"