from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_not_message_products_at_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.MESSAGE_PRODUCTS_AT_BASKET), "Products in basket message is presented"

    def should_be_not_basket_items_at_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "basket items presented"

    def should_be_basket_empty_message(self):
        text = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_EMPTY).text
        url = self.browser.current_url
        if 'http://selenium1py.pythonanywhere.com/ru' in url:
            assert 'Ваша корзина пуста' in text, "Basket empty message is presented"
        elif 'http://selenium1py.pythonanywhere.com/en' in url:
            assert 'Your basket is empty' in text, "Basket empty message is presented"
