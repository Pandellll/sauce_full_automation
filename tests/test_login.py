import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage

def test_success_login_LA_001(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    product = ProductPage(driver)
    assert product.get_title() == "Products"

def test_wrong_password_LA_002(driver):
    login = LoginPage(driver)
    login.login("standard_user", "wrong_pass")
    assert "Epic sadface: Username and password do not match any user in this service" in login.get_error()

def test_empty_username_LA_003(driver):
    login = LoginPage(driver)
    login.login("", "secret_sauce")
    assert "Epic sadface: Username is required" in login.get_error()

def test_empty_password_LA_004(driver):
    login = LoginPage(driver)
    login.login("standard_user", "")
    assert "Password is required" in login.get_error()

def test_locked_user_LA_005(driver):
    login = LoginPage(driver)
    login.login("locked_out_user", "secret_sauce")
    assert "Sorry, this user has been locked out." in login.get_error()