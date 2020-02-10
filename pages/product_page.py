from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        self.name = self.browser.find_element(*ProductPageLocators.NAME).text
        self.price = self.browser.find_element(*ProductPageLocators.PRICE).text
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        btn.click()
        self.solve_quiz_and_get_code()
        self.name_should_be_equal_to_alert_name()
        self.price_should_be_equal_to_basket_price()

    def name_should_be_equal_to_alert_name(self):
        success_name_alert = self.browser.find_element(*ProductPageLocators.SUCCESS_NAME_ALERT).text
        assert self.name == success_name_alert, 'Name in the alert is not equal to name'

    def price_should_be_equal_to_basket_price(self):
        basket_amount_alert = self.browser.find_element(*ProductPageLocators.BASKET_AMOUNT_ALERT).text
        assert self.price == basket_amount_alert, 'Price in the basket is not equal to price'
