#Selenium scraper
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import re

#Set up the driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bol.com/nl/nl/l/eten-drinken-aanbiedingen-korting/36080+58334/?promo=promotionpage_100_category")
#press the button //*[@id="js-first-screen-accept-all-button"]
driver.find_element_by_xpath(" //*[@id=\"js-first-screen-accept-all-button\"]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/wsp-modal-window/div[2]/div[2]/wsp-country-language-modal/button").click()
time.sleep(1)
#get a list of all prices
prices_e = driver.find_elements_by_xpath("/html/body/div/main/wsp-async-browse/div/div/div[3]/div/div[2]/div/div[4]/div/ul/li/div[2]/div[2]/span/section/div/div/span[2]")
print(prices_e)
# its now a list of <selenium.webdriver.remote.webelement.WebElement (session="136413c0b6808007ca8441e8a4bffec9", element="EF9304B99BF9B0A1E8C7181018E2070A_element_478")>
prices=[]
#convert to a list of floats
for price in prices_e:
    price = price.text
    price = price.replace("\n", ".")
    price = float(price)
    prices.append(price)
    print(price)
#find the lowest price
lowest = prices[0]
for price in prices:
    if price < lowest:
        lowest = price
print("Lowest price:")
print(lowest)
#average price
total = 0
for price in prices:
    total = total + price
average = total / len(prices)
print("Average price:")
print(average)
driver.close()
