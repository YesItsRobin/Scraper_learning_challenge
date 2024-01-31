class Object():
    
    def __init__(self, name=None, price=None, link=None,rating = None, rating_count = None):
        self.name = name
        self.price = price
        self.link = link
        self.rating  = rating
        self.rating_count = rating_count

    def __str__(self):
        return f"Object: [ Name: {self.name}, price: {self.price}, link: {self.link}, rating: {self.rating}, rating_count: {self.rating_count}]"