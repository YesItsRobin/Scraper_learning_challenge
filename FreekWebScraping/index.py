from BolDriver import *
import time

bolDriver = BolDriver()
for i in range(5):
    print(bolDriver.get_next_item())