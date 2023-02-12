from project.pages.base_page import BasePage
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
import pytest
import random

a = random.randrange(0, 1111)
email = f"12332{a}@gmail.com"
password = "Kabaju081"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
link_new_year = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link_list = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
             pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                          marks=pytest.mark.xfail),
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
