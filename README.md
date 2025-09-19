# SauceDemo Automation Testing

This repository contains automated test cases for [SauceDemo](https://www.saucedemo.com/) using **Selenium**, **Pytest**, and **Page Object Model (POM)** design pattern.

---

## Features
- Login tests (valid & invalid)
- Product sorting tests
- Cart functionality tests
- Checkout flow tests
- Edge case scenarios

---

## Tech Stack
- Python 3.13.3
- Selenium 4.35.0
- Pytest 8.4.1

---

## Project Structure

sauce_full_testing/
│
├── pages/ # Page Object Model (POM) classes
│ ├── login_page.py
│ ├── product_page.py
│ ├── checkout_page.py
│ └── cart_page.py
│
├── tests/ # Test cases
│ ├── test_login.py
│ ├── test_sorting.py
│ ├── test_checkout.py
│ ├── test_cart.py
│ ├── test_logout.py
│ └── test_edge.oy
│
├── venv/
│ ├── .gitignore
├── requirements.txt
└── conftest.py

---

## How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/Pandellll/sauce_full_automation.git
   cd sauce_full_testing
   ```

2. Create virtual environment & install dependencies:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run tests:
   ```bash
   pytest -v

---

## Author
Irfan Fadhil (Pandellll)
