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
    # Нажимаем на кнопку Личный кабинет
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

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

    # Нажимаем на кнопку Личный кабинет
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

class TestNavigation:
    # Успешный переход в Личный кабинет
    def test_successful_tab_by_button_personal_account(self, driver):
        driver.get(main_site)

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

        # Проверяем, что попали в Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(account_profile))

        #Проверяем, что в Личном кабинете есть кнопка "Выход"
        assert driver.find_element(*Locators.EXIT_BUTTON).text == 'Выход'

        # Закрываем браузер
        driver.quit()

    # Успешный выход из аккаунта
    def test_successful_tab_by_button_exit(self, driver):
        driver.get(main_site)

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

        #Нажимаем на кнопку "Выход"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.EXIT_BUTTON).click()

        # Проверяем, что попали на страницу авторизации
        assert WebDriverWait(driver, 3).until(expected_conditions.url_to_be(login_form))

        # Закрываем браузер
        driver.quit()

    # Успешный переход по клику на Конструктор
    def test_successful_tab_by_button_constractor_in_personal_account(self, driver):
        driver.get(main_site)

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

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

        # Нажимаем на лого Stellar Burgers
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_STELLAR_BURGERS))
        driver.find_element(*Locators.LOGO_STELLAR_BURGERS).click()

        # Проверяем наличие кнопки "Оформить заказ"
        element = driver.find_element(*Locators.PLACE_AN_ORDER_BUTTON)
        assert 'Оформить заказ' in element.text

    # Успешный переход в раздел Соусы
    def test_successful_tab_by_button_sauces_on_constructor_page(self, driver):
        driver.get(main_site)

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

        # Нажимаем на кнопку "Конструктор"
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        # Нажимаем на кнопку Соусы
        driver.find_element(*Locators.SAUCES_BUTTON).click()

        # Проверяем, что на странице есть Соус Spicy-X
        element = driver.find_element(*Locators.SPICY_SAUCE)
        assert 'Соус Spicy-X' in element.text

    # Успешный переход в раздел Булки
    def test_successful_tab_by_button_bread_on_constructor_page(self, driver):
        driver.get(main_site)

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

        # Нажимаем на кнопку "Конструктор"
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        # Нажимаем на кнопку Соусы
        driver.find_element(*Locators.SAUCES_BUTTON).click()

        # Нажимаем на кнопку Булки
        driver.find_element(*Locators.BREAD_BUTTON).click()

        # Проверяем, что на странице есть Флюоресцентная булка R2-D3
        element = driver.find_element(*Locators.FLU_BREAD)
        assert 'Флюоресцентная булка R2-D3' in element.text

    # Успешный переход в раздел Начинки
    def test_successful_tab_by_button_fillings_on_constructor_page(self, driver):
        driver.get(main_site)

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

        # Нажимаем на кнопку "Конструктор"
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        # Нажимаем на кнопку Начинки
        driver.find_element(*Locators.FILLINGS_BUTTON).click()

        # Проверяем, что на странице есть Мясо бессмертных моллюсков Protostomia
        element = driver.find_element(*Locators.MEAT_BUTTON)
        assert 'Мясо бессмертных моллюсков Protostomia' in element.text

