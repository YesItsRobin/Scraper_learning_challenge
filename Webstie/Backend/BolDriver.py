from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep  
import atexit

class BolDriver():
    __driver = None
    __cookies_accepted = False
    __URL = "https://www.bol.com/nl/nl/l/boeken/8299/"+"?view=list"
    __page = 1

    def __init__(self):
        options = Options()
        options.add_argument("--headless")

        self.__driver = webdriver.Firefox(options=options)
        self.__driver.get(self.__URL)
        self.accept_cookies()
        atexit.register(self.close_browser)

    def accept_cookies(self):
        if self.__cookies_accepted:
            return
        sleep(0.3)
        self.__driver.find_element(By.ID, "js-first-screen-accept-all-button").click()
        sleep(1.5)
        self.__driver.find_element(By.XPATH, "/html/body/wsp-modal-window/div[2]/div[2]/wsp-country-language-modal/button").click()
        print("-> Cookies accepted")
        self.__cookies_accepted = True



    def get_items(self, ammount:int, product_info_list:list = []):
        x_path_string = "//*[@id=\"js_items_content\"]/li"
        product_elements = self.__driver.find_elements(By.XPATH, x_path_string)

        # Iterate through each product element and scrape data
        for product_element in product_elements:
            if len(product_info_list) >= ammount:
                return product_info_list
            
            product_info = {}
            # Scrape title and href
            product_info['title'] = self.get_elements_attribute(product_element,".//a[@data-test='product-title']","text")
            product_info['href'] = self.get_elements_attribute(product_element,".//a[@data-test='product-title']","href")
            product_info['price'] = self.get_elements_attribute(product_element,".//*[@itemprop='price']","content") 
            product_info['description'] = 'De LG 43UR78006LK is een 4K LED televisie met 4K upscaling. De televisie beschikt over verschillende…'

            product_info_list.append(product_info)
        self.__next_page(x_path_string)
        return self.get_items(ammount, product_info_list)


    
    def check_element(self,element,XPATH):
        l = element.find_elements(By.XPATH, XPATH)
        self.__driver.implicitly_wait(1)
        return len(l) > 0

    def get_elements_attribute(self, element, XPATH, attribute):
        if self.check_element(element,XPATH):
            return element.find_element(By.XPATH, XPATH).get_attribute(attribute)
        else:
            return None
    
    def __next_page(self, x_path_string):
        self.__items_per_page = len(self.__driver.find_elements(By.XPATH, x_path_string))
        self.__item = 1
        self.__page += 1
        self.__driver.get(f"{self.__URL}&page={self.__page}")
        self.__driver.implicitly_wait(10)
    
    
    
    def close_browser(self):
        self.__driver.close()
        self.__driver.quit()

# bolDriver = BolDriver()
# items = bolDriver.get_items(30)
# for item in items:
#     print(item)