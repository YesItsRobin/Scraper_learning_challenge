from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep  
from Book import Book
from Object import Object
import atexit

class BolDriver():
    __driver = None
    __cookies_accepted = False
    __URL = "https://www.bol.com/nl/nl/l/boeken/8299/"+"?view=list"
    __item = 0
    __items_per_page = 30
    __page = 1

    def __init__(self):
        options = Options()
        options.add_argument("-headless")

        self.__driver = webdriver.Chrome(executable_path="C:\\Users\\Dinu\\Downloads\\chromedriver-win64\\chromedriver.exe", options=options)
        self.__driver.get(self.__URL)
        self.accept_cookies()
        atexit.register(self.close_browser)

    def accept_cookies(self):
        if self.__cookies_accepted:
            return
        sleep(0.3)

        # Accepting cookies
        self.__driver.find_element(By.ID, "js-first-screen-accept-all-button").click()
        self.__driver.implicitly_wait(20)
        self.__driver.find_element(By.XPATH, "/html/body/wsp-modal-window/div[2]/div[2]/wsp-country-language-modal/button").click()
        self.__driver.implicitly_wait(20)
        self.__cookies_accepted = True

    def get_next_item(self):
        x_path_string = "//*[@id=\"js_items_content\"]/li"
        if self.__item == 0:
            self.__items_per_page = len(self.__driver.find_elements(By.XPATH, x_path_string))
            self.__item = 1

        if self.__item == self.__items_per_page:
            self.__next_page(x_path_string)

        x_path_string = f"{x_path_string}[{self.__item}]"
        self.__item += 1
        return Object(
            self.get_elements_attribute(x_path_string + "//a[@data-test='product-title']","text"),
            self.get_elements_attribute(x_path_string + "//*[@itemprop='price']","content"),
            self.get_elements_attribute(x_path_string + "//a[@data-test='product-title']","href"),
            self.get_elements_attribute(x_path_string + "//div[@data-test='rating-stars']","title"),
            rating_count=self.get_elements_attribute(x_path_string + "//div[@data-test='rating-stars']","data-count")
        )
    
    def check_element(self,XPATH):
        return len(self.__driver.find_elements(By.XPATH, XPATH)) > 0

    def get_elements_attribute(self,XPATH,attribute):
        if self.check_element(XPATH):
            return self.__driver.find_element(By.XPATH, XPATH).get_attribute(attribute)
        else:
           return None
    
    def __next_page(self, x_path_string):
        self.__driver.get(f"{self.__URL}&page={self.__page}")
        sleep(1)

        self.__items_per_page = len(self.__driver.find_elements(By.XPATH, x_path_string))
        self.__item = 1
        self.__page += 1
    
    
    
    def close_browser(self):
        self.__driver.close()
        self.__driver.quit()
