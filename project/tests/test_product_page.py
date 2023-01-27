import pytest

from project.pages.login_page import LoginPage
from project.pages.product_page import ProductPage
from project.pages.main_page import MainPage
from project.pages.basket_page import BasketPage
from project.pages.catalogue_page import CataloguePage
import time
from project.settings import *


def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link_new_year)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    # time.sleep(15)
    product_page.cart_name_product_compare()
    product_page.text_price_cart()
    product_page.price_cart_and_product_compare()
    product_page.price_cart_and_without_nds_compare()


@pytest.mark.parametrize('link', link_list)
def test_guest_can_add_product_to_basket_link_list(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    # time.sleep(10)
    product_page.cart_name_product_compare()
    product_page.text_price_cart()
    product_page.price_cart_and_product_compare()
    product_page.price_cart_and_without_nds_compare()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_to_cart()
    # time.sleep(99)
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_to_cart()
    # time.sleep(99)
    product_page.should_success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_not_message_products_at_basket()
    basket_page.should_be_not_basket_items_at_basket()
    basket_page.should_be_basket_empty_message()
