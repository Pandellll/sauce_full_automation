from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def login_standard(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")

def test_add_single_product_to_cart_PC_001(driver):
    login_standard(driver)
    p = ProductPage(driver)
    p.add_to_cart("Sauce Labs Backpack")
    assert p.get_cart_count() == "1"

def test_add_multiple_products_to_cart_PC_002(driver):
    login_standard(driver)
    p = ProductPage(driver)
    p.add_to_cart("Sauce Labs Backpack")
    p.add_to_cart("Sauce Labs Bike Light")
    assert p.get_cart_count() == "2"

def test_remove_product_from_cart_PC_003(driver):
    login_standard(driver)
    p = ProductPage(driver)
    p.add_to_cart("Sauce Labs Backpack")
    p.open_cart()
    c = CartPage(driver)
    c.remove_item("Sauce Labs Backpack")
    assert c.count_items() == 0

def test_proceed_to_checkout_from_cart_PC_004(driver):
    login_standard(driver)
    p = ProductPage(driver)
    p.add_to_cart("Sauce Labs Backpack")
    p.open_cart()
    c = CartPage(driver)
    c.checkout()
    from selenium.webdriver.common.by import By
    assert driver.find_element(By.ID, "first-name")