from helpers import login_action
from locators import Locators
from curl import *


class TestLogin:
    #Успешный вход через кнопку "Войти в аккаунт" на главной странице
    def test_successful_login_by_button_login_to_account(self, driver):
        driver.get(main_site)

        #Нажимаем на кнопку "Войти в аккаунт"
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        #Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

    # Успешный вход через кнопку "Личный кабинет" на главной странице
    def test_successful_login_by_button_personal_account(self, driver):
        driver.get(main_site)

        # Нажимаем на кнопку Личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

    # Успешный вход через кнопку "Войти" на форме регистрации
    def test_successful_login_by_button_login_on_the_registration_form(self, driver):
        driver.get(register_form)

        #Нажимаем на ссылку "Войти" в форме регистрации
        driver.find_element(*Locators.LOGIN_LINK).click()

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

    #Успешный вход через кнопку "Войти" на форме восстановления пароля
    def test_successful_login_by_button_login_on_the_password_recovery_form(self, driver):
        driver.get(login_form)

        #Нажимаем на кнопку "Восстановить пароль" на форме авторизации
        driver.find_element(*Locators.RECOVER_PASSWORD_LINK).click()

        #Нажимаем на кнопку "Войти" на форме восстановления пароля
        driver.find_element(*Locators.LOGIN_LINK).click()

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)








