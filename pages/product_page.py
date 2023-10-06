import time

import pytest

from .base_page import BasePage
from .locators import ProductPageLocators


class GoodsPage(BasePage):
    def add_to_cart(self):
        to_cart_button = self.browser.find_element(*ProductPageLocators.TO_CART_BUTTON)
        to_cart_button.click()
        #self.solve_quiz_and_get_code()

    def should_be_added_message(self):
        added_message = self.browser.find_element(*ProductPageLocators.ADDED_MESSAGE)
        goods_name = self.browser.find_element(*ProductPageLocators.GOODS_NAME)
        try:
            assert added_message.text == goods_name.text, f"Item {goods_name.text} is missing in the cart"
        except AssertionError:
            print(self.browser.current_url)
            raise AssertionError(f"Item {goods_name.text} is missing in the cart")

    def cart_and_price_should_be_equal(self):
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE)
        goods_price = self.browser.find_element(*ProductPageLocators.GOODS_PRICE)
        try:
            assert cart_price.text == goods_price.text, f"Cart price isn't equal to the item price"
        except AssertionError:
            print(self.browser.current_url)
            raise AssertionError(f"Cart price isn't equal to the item price")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_MESSAGE), \
            "Success message not disappeared"

