#Selenium scraper
import time

#Set up the driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from spider import Spider

my_spider = Spider()
my_spider.search("eten")
prices = my_spider.get_items_on_page()
print(prices)
#show some statistics
#sort the list
prices.sort()

#find the lowest price
lowest = prices[0]
highest = prices[-1]
print("Lowest price: " + str(lowest))
print("Highest price: " + str(highest))

#average price
total = 0
for price in prices:
    total = total + price
average = total / len(prices)
print("Average price: " + str(average))
