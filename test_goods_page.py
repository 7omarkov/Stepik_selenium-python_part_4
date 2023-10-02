from selenium.webdriver.common.by import By
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.goods_page import GoodsPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = GoodsPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_be_added_message()
    time.sleep(1)
    page.cart_and_price_should_be_equal()
    time.sleep(10)


if __name__ == "__main__":
    pytest.main(["-s", "-v", "--tb=line", "--language=en", "test_main_page.py"])