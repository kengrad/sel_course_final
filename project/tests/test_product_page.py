from project.pages.product_page import ProductPage
from project.pages.main_page import MainPage
from project.pages.base_page import BasePage
from project.pages.catalogue_page import CataloguePage
import time




def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.cart_name_product_compare()
    product_page.text_price_cart()
