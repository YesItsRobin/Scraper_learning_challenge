from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep  
from Book import Book
from webdriver_manager.chrome import ChromeDriverManager
from Object import Object
import atexit


class BolDriver():
    __driver = None
    __cookiesAccepted = False
    __URL = "https://www.bol.com/nl/nl/l/boeken/8299/"+"?view=list"
    __item = 0
    __itemsPerPage = 30
    __page = 1


    def __init__(self):
        self.__driver = webdriver.Chrome(ChromeDriverManager().install())
        self.__driver.get(self.__URL)
        self.acceptCookies()
        atexit.register(self.closeBrowser)

    def acceptCookies(self):
        if (self.__cookiesAccepted):
            return
        sleep(0.3)

        # Accepting cookies
        self.__driver.find_element(By.ID, "js-first-screen-accept-all-button").click()
        self.__driver.implicitly_wait(20)
        self.__driver.find_element(By.XPATH, "/html/body/wsp-modal-window/div[2]/div[2]/wsp-country-language-modal/button").click()
        self.__driver.implicitly_wait(20)
        self.__cookiesAccepted = True


    def getItems(self, ammount:int, product_info_list:list = []):
        product_elements = self.__driver.find_elements(By.XPATH, '/html/body/div[1]/main/wsp-async-browse/div/div/div[3]/div/div[2]/div/div[4]/div/ul/li')
        # Iterate through each product element and scrape data
        for product_element in product_elements:
            if len(product_info_list) >= ammount:
                return product_info_list
            
            product_info = {}
            
            # Scrape title and href
            product_info['title'] = product_element.find_element_by_css_selector('a.product-title').text
            product_info['href'] = product_element.find_element_by_css_selector('a.product-title').get_attribute('href')

            price_element = product_element.find_element_by_css_selector('.promo-price')
            if price_element:
                product_info['price'] = price_element.text.replace('\n', '.').replace('.-', '.00')
            else:
                product_info['price'] = 'No price available'
            product_info_list.append(product_info)
        self.__nextPage()
        return self.getItems(ammount, product_info_list)
        
    def getNextItem(self):
        xPathString = "//*[@id=\"js_items_content\"]/li"
        if (self.__item == 0):
            self.__itemsPerPage = len(self.__driver.find_elements(By.XPATH, xPathString))
            self.__item = 1

        if (self.__item == self.__itemsPerPage):
            self.__nextPage(xPathString)


        xPathString = f"{xPathString}[{self.__item}]"
        self.__item = self.__item + 1
        return Object(
            self.getElementsText(xPathString+"//a[@data-test='product-title']"),
            self.getElementsContent(xPathString+"//*[@itemprop='price']"),
            self.getElementsLink(xPathString+"//a[@data-test='product-title']"),
        )


    def getElementsText(self, XPATH):
        return self.__driver.find_element(By.XPATH, XPATH).text
    
    def getElementsContent(self, XPATH):
        return self.__driver.find_element(By.XPATH, XPATH).get_attribute('content')
    
    def getElementsLink(self, XPATH):
        return self.__driver.find_element(By.XPATH, XPATH).get_attribute('href')
    
    def getElementsImage(self, XPATH):
        print(len(self.__driver.find_elements(By.XPATH, XPATH)))
        return self.__driver.find_elements(By.XPATH, XPATH).get_attribute('src')

    
    def __nextPage(self):
        self.__page = self.__page + 1
        self.__driver.get(f"{self.__URL}&page={self.__page}")
        sleep(1)
    
    def closeBrowser(self):
        self.__driver.close()
        self.__driver.quit()
