import pytest

from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()


mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
xfile = 7
params = [f'?promo=offer{i}' for i in range(10) if i != xfile]
links = [f'{mask}/{param}' for param in params]
xfile_link = pytest.param(f'{mask}/?promo=offer{xfile}',
                          marks=pytest.mark.xfail(reason='Product name not equal to alert name'))
links.append(xfile_link)


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.name_should_be_equal_to_alert_name()
    page.price_should_be_equal_to_basket_price()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link, timeout=None)  # None because some methods use explict wait
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link, timeout=None)  # None because some methods use explict wait
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link, timeout=None)  # None because some methods use explict wait
    page.open()
    page.add_to_cart()
    page.success_message_should_disappear()
