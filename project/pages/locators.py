from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CATALOGUE_LINK = (By.CSS_SELECTOR, "#browse > li > ul > li:nth-child(1) > a")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class CataloguePageLocators():
    CATALOGUE_FORM_SIDE = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div > div > aside")
    CATALOGUE_FORM = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div > div > div")

