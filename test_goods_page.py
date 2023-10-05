from selenium.webdriver.common.by import By
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.goods_page import GoodsPage
import time


@pytest.mark.parametrize("offer_id",[0,1,2,3,4,5,6,
                                     pytest.param(7, marks=pytest.mark.xfail)
                                    ,8,9])
def test_guest_can_add_product_to_basket(browser, offer_id):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_id}"
    page = GoodsPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_be_added_message()
    time.sleep(1)
    page.cart_and_price_should_be_equal()
    time.sleep(1)
@pytest.mark.xfail()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = GoodsPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = GoodsPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    mp = MainPage(browser, link)
    mp.open()
    mp.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = GoodsPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = GoodsPage(browser, link)
    page.open()
    page.add_to_cart()
    page.success_message_is_disappeared()

    pass


if __name__ == "__main__":
    pytest.main(["-s", "-v", "--tb=line", "--language=en", "test_main_page.py"])