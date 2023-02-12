from project.pages.main_page import MainPage
from project.pages.catalogue_page import CataloguePage

link = "http://selenium1py.pythonanywhere.com"


def test_guest_should_see_catalogue(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_catalogue_page()
    page = CataloguePage(browser, browser.current_url)
    page.should_be_catalogue_page()
