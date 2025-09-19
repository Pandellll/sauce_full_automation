from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_multiple_sessions_with_same_account(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    second = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        second.get("https://www.saucedemo.com/")
        second.find_element("id","user-name").send_keys("standard_user")
        second.find_element("id","password").send_keys("secret_sauce")
        second.find_element("id","login-button").click()
        assert "inventory.html" in second.current_url
    finally:
        second.quit()