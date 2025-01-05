import pytest
from selenium import webdriver
from locators import Locators
from data import Credentials
from curl import *
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture
def driver():
    return webdriver.Chrome()

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