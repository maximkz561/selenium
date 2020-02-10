from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

    EMAIL_ENTER_FORM = (By.ID, 'id_login-username')
    PASSWORD_ENTER_FORM = (By.ID, 'id_login-password')
    EMAIL_ENTER_REGISTRATION = (By.ID, 'id_registration-email')
    PASSWORD_ENTER_REGISTRATION = (By.ID, 'id_registration-password1')
    PASSWORD_ENTER_REGISTRATION_REPEAT = (By.ID, 'id_registration-password2')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_NAME_ALERT = (By.CSS_SELECTOR, '.alert-success:nth-child(1) strong')
    BASKET_AMOUNT_ALERT = (By.CSS_SELECTOR, '.alert-info strong')
