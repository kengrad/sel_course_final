from .base_page import BasePage
from .locators import MainPageLocators, BasketPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_catalogue_page(self):
        link = self.browser.find_element(*MainPageLocators.CATALOGUE_LINK)
        link.click()

    def should_be_catalogue_link(self):
        assert self.is_element_present(*MainPageLocators.CATALOGUE_LINK), "Catalogue link is not presented"

