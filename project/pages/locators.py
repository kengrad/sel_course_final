from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CATALOGUE_LINK = (By.CSS_SELECTOR, "#browse > li > ul > li:nth-child(1) > a")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class CataloguePageLocators():
    PRODUCT_ITEM = (By.CSS_SELECTOR,
                    "#default > div.container-fluid.page > div > div > div > section > div > ol > li:nth-child(1) > article > h3 > a")
    CATALOGUE_FORM_SIDE = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div > div > aside")
    CATALOGUE_FORM = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div > div > div")


# content_inner > article > div.row > div.col-sm-6.product_main > h1
class ProductPageLocators():
    PRODUCT_FORM_ITEM = (By.CSS_SELECTOR, "#product_gallery > div > div > div")
    PRODUCT_FORM_INFO = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main")
    PRODUCT_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_ADD_TO_CART_NAME_IN_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_ADD_TO_CART_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRODUCT_TEXT_PRICE_CART = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div")
