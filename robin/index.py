from BolDriver import *

bolDriver = BolDriver()
items = bolDriver.getItems(50)
for item in items:
    print(item)