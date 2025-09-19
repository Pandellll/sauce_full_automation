from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def login_and_add(driver, product_name="Sauce Labs Backpack"):
    LoginPage(driver).login("standard_user", "secret_sauce")
    p = ProductPage(driver)
    p.add_to_cart(product_name)
    p.open_cart()
    CartPage(driver).checkout()

def test_successful_checkout_CF_001(driver):
    login_and_add(driver)
    ch = CheckoutPage(driver)
    ch.fill_info("Jane","Doe","12345")
    ch.finish_checkout()
    assert "THANK YOU FOR YOUR ORDER" in ch.get_complete_msg().upper()

def test_checkout_missing_required_field_CF_002(driver):
    login_and_add(driver)
    ch = CheckoutPage(driver)
    ch.fill_info("", "Doe", "12345")
    assert "Error: First Name is required" in ch.get_error()

def test_validate_total_price_calculation_CF_003(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    p = ProductPage(driver)
    p.add_to_cart("Sauce Labs Backpack")
    p.add_to_cart("Sauce Labs Bike Light")
    p.open_cart()
    from pages.checkout_page import CheckoutPage
    c = CartPage(driver)
    c.checkout()
    ch= CheckoutPage(driver)
    ch.fill_info("Jane", "Doe", "12345")
    subtotal, tax, total = ch.get_totals()
    assert abs((subtotal + tax) - total) < 0.01

def test_cancel_checkout_CF_004(driver):
    login_and_add(driver)
    ch = CheckoutPage(driver)
    ch.cancel_checkout()
    from pages.product_page import ProductPage
    assert ProductPage(driver).get_title() == "Your Cart"

def test_checkout_with_empty_cart_NE_001(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    driver.get("https://www.saucedemo.com/cart.html")
    from pages.cart_page import CartPage
    c = CartPage(driver)
    c.checkout()
    from selenium.webdriver.common.by import By
    assert driver.find_element(By.ID, "first-name")
    assert c.count_items() == 0

def test_zipcode_non_numeric_allows_continue_NE_003(driver):
    login_and_add(driver)
    ch =CheckoutPage(driver)
    ch.fill_info("Jane","Doe","ABCDE")
    assert "checkout-step-two" in driver.current_url or driver.find_element_by_id("finish")
