from selenium.webdriver.common.by import By
import pytest

from pages.basket_page import CartPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import GoodsPage
import time


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(email=str(time.time()) + "@fakemail.org",
                                     password="!fasdA123123")

    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = GoodsPage(browser, link)
        page.open()
        page.add_to_cart()
        page.should_be_added_message()
        page.cart_and_price_should_be_equal()

    def test_user_cant_see_success_message(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = GoodsPage(browser, link)
        page.open()
        page.should_not_be_success_message()






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

def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):

    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = GoodsPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.cart_should_be_empty()
    time.sleep(1)


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