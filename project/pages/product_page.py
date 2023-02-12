from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_product_form()

    def should_be_product_url(self):
        assert "catalogue" in self.browser.current_url, "Product url is not correct"

    def should_be_product_form(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_FORM_ITEM), "Product item form is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_FORM_INFO), "Product info form is not presented"
        assert True

    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_CART_BUTTON)
        link.click()

    def cart_name_product_compare(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_CART_NAME).text
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_CART_NAME_IN_CART).text
        assert product_name in product_name_in_cart, "Names are diferrent"
        assert product_name_in_cart in product_name, "Names are diferrent"

    def cart_name_product_compare(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_CART_NAME).text
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_CART_NAME_IN_CART).text
        assert product_name in product_name_in_cart, "Names are diferrent"

    def text_price_cart(self):
        text = self.browser.find_element(*ProductPageLocators.PRODUCT_TEXT_PRICE_CART).text
        assert "Стоимость корзины теперь составляет" in text, "not valid text"

    def price_cart_and_product_compare(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_CART).text
        assert price in price_cart, "Prices cart and product are diferrent"

    def price_cart_and_without_nds_compare(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_cart_without_nds = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_WITHOUT_NDS).text
        assert price in price_cart_without_nds, "Prices cart and without nds are diferrent"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
