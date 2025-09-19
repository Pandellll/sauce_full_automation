from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.fristname = (By.ID, "first-name")
        self.lastname = (By.ID, "last-name")
        self.zip = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")
        self.error_msg = (By.CSS_SELECTOR, "h3[data-test='error']")
        self.complete_msg = (By.CLASS_NAME, "complete-header")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.subtotal_label = (By.CLASS_NAME, "summary_subtotal_label")
        self.tax_label = (By.CLASS_NAME, "summary_tax_label")
        self.cancel_btn = (By.ID, "cancel")
    
    def fill_info(self, first, last, zipc):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(self.fristname)).clear()
        self.driver.find_element(*self.fristname).send_keys(first)
        self.driver.find_element(*self.lastname).clear()
        self.driver.find_element(*self.lastname).send_keys(last)
        self.driver.find_element(*self.zip).clear()
        self.driver.find_element(*self.zip).send_keys(zipc)
        self.driver.find_element(*self.continue_btn).click()

    def finish_checkout(self):
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.finish_btn)).click()
    
    def get_error(self):
        try:
            return WebDriverWait(self.driver,3).until(EC.visibility_of_element_located(self.error_msg)).text
        except:
            return ""
        
    def get_complete_msg(self):
        return WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(self.complete_msg)).text
    
    def get_totals(self):
        subtotal_text = self.driver.find_element(*self.subtotal_label).text
        tax_text =self.driver.find_element(*self.tax_label).text
        total_text = self.driver.find_element(*self.total_label).text
        def number(s):
            return float(re.sub(r"[^\d.]","",s))
        return number(subtotal_text), number(tax_text), number(total_text)
    
    def cancel_checkout(self):
        self.driver.find_element(*self.cancel_btn).click()
