import time
from project.settings import *
import faker

from .base_page import BasePage
from .locators import LoginPageLocators





class LoginPage(BasePage):

    def new_reg(self,browser):
        f = faker.Faker()
        email = f.email()
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.input_repeat_password(password)
        self.click_confirm_registration_button()

    def input_email(self, email):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

    def input_password(self, password):
        pass_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        pass_input.send_keys(password)

    def input_repeat_password(self, password):
        repeat_pass_input = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_INPUT)
        repeat_pass_input.send_keys(password)

    def click_confirm_registration_button(self):
        confirm_registration_button = self.browser.find_element(*LoginPageLocators.CONFIRM_REGISTRATION_BUTTON)
        confirm_registration_button.click()
