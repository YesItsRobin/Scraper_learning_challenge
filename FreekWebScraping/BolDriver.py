from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep  
import atexit

class BolDriver():
    __driver = None
    __cookies_accepted = False
    searchtext = input('Search: ').replace(' ','+')
    dict_of_sort = {"price low to high":"price0", "price hight to low":"price1" ,"realease date":'release_date1' ,"rating":"rating1" ,"Most wanted":"wishListRank1"}
    __URL = f'https://www.bol.com/nl/nl/s/?searchtext={searchtext}&view=list&'
    __page = 1

    def __init__(self):

        self.__driver = webdriver.Chrome(executable_path="C:\\Users\\Dinu\\Downloads\\chromedriver-win64\\chromedriver.exe")
        self.__driver.get(self.__URL)
        self.accept_cookies()   
        atexit.register(self.close_browser)

    def accept_cookies(self):
        if self.__cookies_accepted:
            return
        self.__driver.implicitly_wait(1)

        # Accepting cookies
        self.__driver.find_element(By.ID, "js-first-screen-accept-all-button").click()
        self.__driver.implicitly_wait(1)
        self.__driver.find_element(By.XPATH, "/html/body/wsp-modal-window/div[2]/div[2]/wsp-country-language-modal/button").click()
        self.__driver.implicitly_wait(1)
        self.__cookies_accepted = True


    def get_items(self, ammount:int, product_info_list:list = []):
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
                product_info['price'] = self.get_elements_attribute(product_element,".//*[@itemprop='price']","content")

                
                product_info_list.append(product_info)
            self.__next_page()
        except:
            self.__driver.get(self.__URL)
            return self.get_items(ammount, product_info_list)
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
    
    def __next_page(self):
        self.__page += 1
        self.__driver.get(f"{self.__URL}&page={self.__page}")
        self.__driver.implicitly_wait(10)
    
    
    
    def close_browser(self):
        self.__driver.close()
        self.__driver.quit()
