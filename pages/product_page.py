from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), 'No add to cart button'

    def add_to_cart(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        btn.click()

    def name_should_be_equal_to_alert_name(self):
        name = self.browser.find_element(*ProductPageLocators.NAME).text
        success_name_alert = self.browser.find_element(*ProductPageLocators.SUCCESS_NAME_ALERT).text
        assert name == success_name_alert, 'Name in the alert is not equal to name'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_NAME_ALERT)

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_NAME_ALERT), 'success alert doesnt disappear'

    def price_should_be_equal_to_basket_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        basket_amount_alert = self.browser.find_element(*ProductPageLocators.BASKET_AMOUNT_ALERT).text
        assert price == basket_amount_alert, 'Price in the basket is not equal to price'
