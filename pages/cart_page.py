from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def cart_should_be_empty(self):
        cart_items = self.browser.find_elements(*CartPageLocators.CART_ITEMS)
        print(cart_items)
        assert len(cart_items) == 0, "The cart it not empty"
