from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep  
import atexit

class BolDriver():
    __driver = None
    __cookies_accepted = False
    __search = input('Search: ').replace(' ','+')
    __price_min = 0
    __price_max = 1000
    __dict_of_sort = {"price low to high":"price0", "price hight to low":"price1" ,"realease date":'release_date1' ,"rating":"rating1" ,"most wanted":"wishListRank1"}
    __sort = __dict_of_sort["most wanted"]
    __URL = "https://www.bol.com/nl/nl/s/?page=1&view=list"
    __page = 1

    def __init__(self):
        self.__driver = webdriver.Chrome(executable_path="C:\\Users\\Dinu\\Downloads\\chromedriver-win64\\chromedriver.exe")
        atexit.register(self.close_browser)

    def accept_cookies(self):
        if self.__cookies_accepted:
            return
        self.__driver.implicitly_wait(1)

        # Accepting cookies
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.ID, "js-first-screen-accept-all-button"))
        ).click()

        # Another explicit wait for the next element if necessary
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/wsp-modal-window/div[2]/div[2]/wsp-country-language-modal/button"))
        ).click()
        self.__cookies_accepted = True

    def go(self):
        self.__driver.get(self.__URL+f"&searchtext={self.__search}&12194={self.__price_min}-{self.__price_max}&sort={self.__sort}")
    
    def filter_price(self, price_min:int, price_max:int):
        self.__price_min = price_min
        self.__price_max = price_max
    
    def filter_sort(self, sort:str):
        self.__sort = sort
    
    def filter_search(self, search:str):
        self.__search = search

    def get_items(self, ammount:int, product_info_list:list = []):
        self.go()
        self.accept_cookies()
        x_path_string = "//*[@id=\"js_items_content\"]/li"
        product_elements = self.__driver.find_elements(By.XPATH, x_path_string)
        # Iterate through each product element and scrape data
        counter = 1
        try:
            for product_element in product_elements:
                print(counter)
                counter += 1
                if len(product_info_list) >= ammount:
                    return product_info_list
                
                product_info = {}
                # Scrape title and href
                product_info['title'] = self.get_elements_attribute(product_element,".//a[@data-test='product-title']","text")
                product_info['href'] = self.get_elements_attribute(product_element,".//a[@data-test='product-title']","href")
                product_info['price'] = self.get_elements_attribute(product_element,".//meta[@itemprop='price']","content")
                product_info['desc'] = self.get_elements_attribute(product_element,".//p[@data-test='product-description']","text")
                
                product_info_list.append(product_info)
            if len(product_elements) < 30:
                return product_info_list
            self.__next_page()
        except:
            self.go()
            return self.get_items(ammount, product_info_list)
        return self.get_items(ammount, product_info_list)


    
    def check_element(self,element,XPATH):
        l = element.find_elements(By.XPATH, XPATH)
        self.__driver.implicitly_wait(1)
        return len(l) > 0

    def get_elements_attribute(self, element, XPATH, attribute):
        if self.check_element(element, XPATH):
            child_element = element.find_element(By.XPATH, XPATH)
            if attribute == "text":
                return child_element.text
            else:
                return child_element.get_attribute(attribute)
        else:
            return None
    
    def __next_page(self):
        self.__page += 1
        self.__driver.get(f"{self.__URL}&page={self.__page}")
    
    
    
    def close_browser(self):
        self.__driver.close()
        self.__driver.quit()
