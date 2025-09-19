from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_btn =(By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def remove_item(self, product_name):
        xpath = f"//div[@class='cart_item']//div[text()='{product_name}']/ancestor::div[@class='cart_item']//button"
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def checkout(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.checkout_btn)).click()

    def count_items(self):
        items = self.driver.find_elements(*self.cart_items)
        return len(items)