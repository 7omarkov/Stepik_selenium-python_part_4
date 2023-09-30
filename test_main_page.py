from selenium.webdriver.common.by import By
import pytest
from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    myvar = browser[1]
    browser = browser[0]
    print(myvar)
    mp = MainPage(browser, link)
    mp.open()
    mp.go_to_login_page()

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "--language=en", "test_main_page.py"])