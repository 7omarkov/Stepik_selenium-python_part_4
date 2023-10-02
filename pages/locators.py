from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators ():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class GoodsPageLocators ():
    TO_CART_BUTTON = (By.XPATH, "//button[contains(@class, 'to-basket')]")
    ADDED_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    CART_PRICE = (By.XPATH, "//div[@id='messages']/div[3]//strong")
    GOODS_NAME = (By.XPATH, "//div[@class='row']//h1")
    GOODS_PRICE = (By.XPATH, "//div[@class='row']//p[@class='price_color']")


class CartPageLocators ():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")