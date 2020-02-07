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
