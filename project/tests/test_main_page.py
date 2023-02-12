import pytest

from project.pages.main_page import MainPage
from project.pages.login_page import LoginPage
from project.pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com"


@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)
        page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_should_see_catalogue_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_catalogue_link()


def test_guest_can_go_to_catalogue(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_catalogue_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, link)
    page.should_be_not_message_products_at_basket()
    page.should_be_not_basket_items_at_basket()
    page.should_be_basket_empty_message()
