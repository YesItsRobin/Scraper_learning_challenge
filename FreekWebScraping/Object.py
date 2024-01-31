class Object():
    
    def __init__(self, name=None, price=None, link=None):
        self.name = name
        self.price = price
        self.link = link


    def __str__(self):
        return f"Object: [ Name: {self.name}, price: {self.price}, link: {self.link}]"