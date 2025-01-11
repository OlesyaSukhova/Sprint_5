from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers import login_action
from locators import Locators
from curl import *


class TestMainMenuNavigation:
    # Успешный переход в Личный кабинет
    def test_successful_tab_by_button_personal_account(self, driver):
        driver.get(main_site)

        # Нажимаем на кнопку Личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

        # Еще раз нажимаем на кнопку Личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        # Проверяем, что попали в Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(account_profile))

        #Проверяем, что в Личном кабинете есть кнопка "Выход"
        assert driver.find_element(*Locators.EXIT_BUTTON).text == 'Выход'

    # Успешный переход по клику на Конструктор
    def test_successful_tab_by_button_constractor_in_personal_account(self, driver):
        driver.get(main_site)

        # Нажимаем на кнопку Личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

        # Нажимаем на кнопку "Конструктор"
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        # Проверяем наличие кнопки "Оформить заказ"
        element = driver.find_element(*Locators.PLACE_AN_ORDER_BUTTON)
        assert 'Оформить заказ' in element.text

    # Успешный переход по клику на лого Stellar Burgers
    def test_successful_tab_by_button_logo_stellar_burgers_in_personal_account(self, driver):
        driver.get(main_site)

        # Нажимаем на кнопку Личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

        # Нажимаем на лого Stellar Burgers
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_STELLAR_BURGERS))
        driver.find_element(*Locators.LOGO_STELLAR_BURGERS).click()

        # Проверяем наличие кнопки "Оформить заказ"
        element = driver.find_element(*Locators.PLACE_AN_ORDER_BUTTON)
        assert 'Оформить заказ' in element.text

