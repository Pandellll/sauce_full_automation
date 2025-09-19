from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")
        self.error_msg = (By.CSS_SELECTOR, "h3[data-test='error']")
    
    def login(self, user, pwd):
        username_field = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.username)
        )
        username_field.clear()
        username_field.send_keys(user)

        password_field = self.driver.find_element(*self.password)
        password_field.clear()
        password_field.send_keys(pwd)

        self.driver.find_element(*self.login_btn).click()

    def get_error(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.error_msg)
            ).text
        except:
            return ""