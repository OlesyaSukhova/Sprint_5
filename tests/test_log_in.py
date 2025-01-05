from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from helpers import generate_random_email, generate_random_password, generate_random_invalid_password
from data import Credentials
from curl import *
driver = webdriver.Chrome()

def login_action(driver):
    # Вводим email и пароль в поля ввода
    driver.find_element(*Locators.FIELD_EMAIL_LOGIN).send_keys(Credentials.email)
    driver.find_element(*Locators.FIELD_PASSWORD_LOGIN).send_keys(Credentials.password)

    # Нажимаем на кнопку "Войти"
    driver.find_element(*Locators.REG_2_BUTTON).click()

    # Проверяем, что мы успешно вошли на сайт
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(main_site))

    # Проверяем наличие кнопки "Оформить заказ"
    element = driver.find_element(*Locators.PLACE_AN_ORDER_BUTTON)
    assert 'Оформить заказ' in element.text


class TestLogin:
    #Успешный вход через кнопку "Войти в аккаунт" на главной странице
    def test_successful_login_by_button_login_to_account(self, driver):
        driver.get(main_site)

        #Нажимаем на кнопку "Войти в аккаунт"
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        #Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

        #Закрываем браузер
        driver.quit()

    # Успешный вход через кнопку "Личный кабинет" на главной странице
    def test_successful_login_by_button_personal_account(self, driver):
        driver.get(main_site)

        # Нажимаем на кнопку Личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

        # Закрываем браузер
        driver.quit()

    # Успешный вход через кнопку "Войти" на форме регистрации
    def test_successful_login_by_button_login_on_the_registration_form(self, driver):
        driver.get(register_form)

        #Нажимаем на кнопку "Войти" в форме регистрации
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

        # Закрываем браузер
        driver.quit()

    #Успешный вход через кнопку "Войти" на форме восстановления пароля
    def test_successful_login_by_button_login_on_the_password_recovery_form(self, driver):
        driver.get(login_form)

        #Нажимаем на кнопку "Восстановить пароль" на форме авторизации
        driver.find_element(*Locators.RECOVER_PASSWORD).click()

        #Нажимаем на кнопку "Войти" на форме восстановления пароля
        driver.find_element(*Locators.LOGIN_BUTTON_FORGET_PASSWORD).click()

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

        # Закрываем браузер
        driver.quit()







