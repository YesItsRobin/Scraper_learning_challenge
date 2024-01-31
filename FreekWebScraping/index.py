from BolDriver import *
import time

bolDriver = BolDriver()
items = bolDriver.get_items(50)
for item in items:
    print(item)
f = time.time()