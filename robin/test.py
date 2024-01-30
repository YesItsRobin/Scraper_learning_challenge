#Selenium scraper
import time

#Set up the driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

urlbase = "https://www.bol.com/nl/nl/l/eten-drinken-aanbiedingen/36080+58334/?page="
urlend = "&promo=promotionpage_100_category"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.bol.com")
driver.find_element_by_xpath(" //*[@id=\"js-first-screen-accept-all-button\"]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/wsp-modal-window/div[2]/div[2]/wsp-country-language-modal/button").click()
time.sleep(1)

prices=[]
for i in range (1, 14):
    driver.get(urlbase + str(i) + urlend)
    time.sleep(1)
    prices_list = (driver.find_elements_by_xpath("/html/body/div/main/wsp-async-browse/div/div/div[3]/div/div[2]/div/div[4]/div/ul/li/div[2]/div[2]/span/section/div/div/span[2]"))
    for price in prices_list:
        price = price.text
        price = price.replace("\n", ".")
        price = float(price)
        prices.append(price)

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
