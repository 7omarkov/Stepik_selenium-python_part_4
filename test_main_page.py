from selenium.webdriver.common.by import By
import pytest
from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    mp = MainPage(browser, link)
    mp.open()
    mp.go_to_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "--language=en", "test_main_page.py"])