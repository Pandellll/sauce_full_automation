from pages.login_page import LoginPage
from pages.product_page import ProductPage

def test_logout_from_sidebar_menu(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    p = ProductPage(driver)
    p.open_menu_and_logout()
    assert driver.current_url.rstrip('/').endswith("saucedemo.com") or driver.find_element("id", "login-button")

def test_access_product_page_after_logout(driver):
    driver.get("https://www.saucedemo.com/")
    driver.get("https://www.saucedemo.com/inventory.html")
    assert driver.find_element("id","login-button")