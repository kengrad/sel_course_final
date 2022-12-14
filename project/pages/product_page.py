from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators
import selenium.webdriver.common


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_product_form()

    def should_be_product_url(self):
        assert "the-shellcoders-handbook_209/?promo=newYear" in self.browser.current_url, "Product url is not correct"

    def should_be_product_form(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_FORM_ITEM), "Product item form is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_FORM_INFO), "Product info form is not presented"
        assert True

    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_CART_BUTTON)
        link.click()

    def cart_name_product_compare(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_CART_NAME).text
        product_name_in_cart = self.browser.find_element(
            *ProductPageLocators.PRODUCT_ADD_TO_CART_NAME_IN_CART).text
        assert product_name in product_name_in_cart, "Names are diferrent"

    def text_price_cart(self):
        text = self.browser.find_element(
            *ProductPageLocators.PRODUCT_TEXT_PRICE_CART).text
        assert "Стоимость корзины теперь составляет" in text, "not valid text"
