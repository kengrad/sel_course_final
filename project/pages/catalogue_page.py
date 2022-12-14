from .base_page import BasePage
from .locators import CataloguePageLocators


class CataloguePage(BasePage):
    def should_be_catalogue_page(self):
        self.should_be_catalogue_form()
        self.should_be_catalogue_url()

    def should_be_catalogue_url(self):
        assert "catalogue" in self.browser.current_url, "Catalogue url is not correct"

    def should_be_catalogue_form(self):
        assert self.is_element_present(*CataloguePageLocators.CATALOGUE_FORM_SIDE), "Catalogue form side is not presented"
        assert self.is_element_present(*CataloguePageLocators.CATALOGUE_FORM), "Catalogue form  is not presented"
        assert True

    def go_to_product_item(self):
        link = self.browser.find_element(*CataloguePageLocators.PRODUCT_ITEM)
        link.click()
