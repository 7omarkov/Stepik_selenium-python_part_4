from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = self.browser.current_url
        assert "login" in login_url


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login link is not presented"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM ), "Login link is not presented"

    def register_new_user(self, email, password):
        email_box = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_box.send_keys(email)
        password_box_1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password_box_1.send_keys(password)
        password_box_2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        password_box_2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
