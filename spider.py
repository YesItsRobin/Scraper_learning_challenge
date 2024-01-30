from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class Spider:
    def __init__(self) -> None:
        self.base_url = "https://www.bol.com/nl/"
        self.spider = webdriver.Chrome(ChromeDriverManager().install())
        self.spider.get(self.get_base_url())
        self.spider.find_element_by_xpath(" //*[@id=\"js-first-screen-accept-all-button\"]").click()
        time.sleep(1)
        self.spider.find_element_by_xpath("/html/body/wsp-modal-window/div[2]/div[2]/wsp-country-language-modal/button").click()
        time.sleep(1)
    
    def search(self, query:str):
        self.spider.get(self.get_base_url() + "nl/s/?searchtext="+ query)

    def get_items_on_page(self) -> list:
        prices=[]
        prices_list = (self.get_spider().find_elements_by_xpath("/html/body/div[1]/main/wsp-async-browse/div/div/div[3]/div/div[2]/div/div[4]/div/ul/li"+"/div[2]/wsp-buy-block/div[1]/section/div/div/span[2]"))
        for price in prices_list:
            price = price.text
            price = price.replace("\n", ".")
            price = price.replace(".-", ".00")
            price = float(price)
            prices.append(price)
        return prices
    def get_base_url(self) -> str:
        return self.base_url
    def get_spider(self) -> webdriver:
        return self.spider