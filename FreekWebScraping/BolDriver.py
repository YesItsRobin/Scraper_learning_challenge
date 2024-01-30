from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep  
from Book import Book


class BolDriver():
    __driver = None
    __cookiesAccepted = False
    __URL = "https://www.bol.com/nl/nl/l/boeken/8299/"
    __item = 1
    __itemsPerPage = 30
    __page = 1


    def __init__(self):
        self.__driver = webdriver.Firefox()
        self.__driver.get(self.__URL)
        self.acceptCookies()

    def acceptCookies(self):
        if (self.__cookiesAccepted):
            return
        sleep(0.3)

        # Accepting cookies
        self.__driver.find_element(By.ID, "js-first-screen-accept-all-button").click()
        self.__driver.find_element(By.XPATH, "/html/body/wsp-modal-window/div[2]/div[2]/wsp-country-language-modal/button").click()
        self.__cookiesAccepted = True

    def getNextItem(self):
        xPathString = "//*[@id=\"js_items_content\"]/li"        
        if (self.__item == self.__itemsPerPage):
            self.__nextPage(xPathString)


        xPathString = f"{xPathString}[{self.__item}]"
        self.__item = self.__item + 1
        return Book(
            self.getElementsText(xPathString+"/div[2]/div/ul[2]/li[3]/span"), 
            self.getElementsText(xPathString+"//a[contains(@class, \"product-title\")]"),
            self.getElementsText(xPathString+"/div[2]/div/ul[1]/li/a"), 
            self.getElementsText(xPathString+"/div[2]/div/ul[2]/li[1]/span"), 
            self.getElementsText(xPathString+"/div[2]/wsp-buy-block/div[1]/section/div/div/span[2]")
        )

    def getElementsText(self, XPATH):
        return self.__driver.find_element(By.XPATH, XPATH).text
    
    def __nextPage(self, xPathString):
        self.__driver.find_element(By.XPATH, "/html/body/div[1]/main/wsp-async-browse/div/div/div[3]/div/div[2]/div/div[5]/ul/li[8]/a").click();
        sleep(1)

        self.__itemsPerPage = len(self.__driver.find_elements(By.XPATH, xPathString))
        self.__item = 1
