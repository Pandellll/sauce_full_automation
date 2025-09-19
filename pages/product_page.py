from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.title = (By.CLASS_NAME, "title")
        self.products = {
            "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bike Light": "add-to-cart-sauce-labs-bike-light",
            "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Fleece Jacket": "add-to-cart-sauce-labs-fleece-jacket",
            "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie",
            "Test.allTheThings() T-Shirt (Red)":"add-to-cart-test.allthethings()-t-shirt-(red)"
        }
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.menu_btn = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")
    
    def get_title(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.title)).text
    
    def add_to_cart(self, product_name):
        product_id = self.products[product_name]
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, product_id))
        ).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()
    
    def get_cart_count(self):
        try:
            return self.driver.find_element(*self.cart_badge).text
        except:
            return "0"
    
    def select(self, option_visible_text):
        from selenium.webdriver.support.ui import Select
        sel = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.sort_dropdown)))
        sel.select_by_visible_text(option_visible_text)
    
    def open_menu_and_logout(self):
        self.driver.find_element(*self.menu_btn).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.logout_link)).click()