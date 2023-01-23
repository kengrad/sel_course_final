import pytest
from project.pages.product_page import ProductPage
from project.pages.main_page import MainPage
from project.pages.base_page import BasePage
from project.pages.catalogue_page import CataloguePage
import time
from project.settings import *


@pytest.mark.parametrize('link', link_list)
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
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
