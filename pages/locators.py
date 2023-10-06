from selenium.webdriver.common.by import By


class BasePageLocators ():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    GOCART_LINK = (By.XPATH, "//*[text()='Посмотреть корзину']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    CART_ITEMS = (By.XPATH, "//*[@class='basket-items']")


class ProductPageLocators ():
    TO_CART_BUTTON = (By.XPATH, "//button[contains(@class, 'to-basket')]")
    ADDED_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    CART_PRICE = (By.XPATH, "//div[@id='messages']/div[3]//strong")
    GOODS_NAME = (By.XPATH, "//div[@class='row']//h1")
    GOODS_PRICE = (By.XPATH, "//div[@class='row']//p[@class='price_color']")

class LoginPageLocators ():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")








