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
    
    def search(self, query):
        self.spider.get(self.get_base_url() + "nl/s/?searchtext="+ query)
    def get_base_url(self):
        return self.baseurl
    def get_spider(self):
        return self.spider