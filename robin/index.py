from BolDriver import *

bolDriver = BolDriver()
bolDriver.filter_price(15, 18)
bolDriver.filter_search("python")
bolDriver.filter_sort("relevance1")
items = bolDriver.getItems(5)
for item in items:
    print(item)