from pages.login_page import LoginPage
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By

def login_standart(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")

def get_product_names(driver):
    elems = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    return [e.text.strip() for e in elems]

def get_product_prices(driver):
    elems =driver.find_elements(By.CLASS_NAME, "invetory_item_price")
    return [float(e.text.strip().replace("$","")) for e in elems]

def test_sort_name_a_to_z_SF_001(driver):
    login_standart(driver)
    p = ProductPage(driver)
    p.select("Name (A to Z)")
    names = get_product_names(driver)
    assert names == sorted(names)

def test_sort_price_low_to_high_SF_002(driver):
    login_standart(driver)
    p = ProductPage(driver)
    p.select("Price (low to high)")
    prices = get_product_prices(driver)
    assert prices == sorted(prices)

def test_sort_price_high_to_low_SF_003(driver):
    login_standart(driver)
    p = ProductPage(driver)
    p.select("Price (high to low)")
    prices = get_product_prices(driver)
    assert prices == sorted(prices, reverse=True)