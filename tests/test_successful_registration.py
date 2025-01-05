from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from helpers import generate_random_email, generate_random_password, generate_random_invalid_password
from data import Credentials
from curl import *
driver = webdriver.Chrome()



class TestRegistration:
    #Успешная регистрация с валидными значениями
    def test_successful_registration (self, driver):
        driver.get(main_site)

        #Нажимаем на кнопку Личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        #Нажимаем на кнопку Зарегестрироваться
        driver.find_element(*Locators.REG_BUTTON).click()

        #Генерируем случайный email и пароль для регистрации
        email = generate_random_email()
        password = generate_random_password()

        #Заполняем поля Имя, Email и Пароль для регистрации
        driver.find_element(*Locators.FIELD_NAME).send_keys(Credentials.name)
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(password)

        #Нажимаем на кнопку Зарегестрироваться
        driver.find_element(*Locators.REG_2_BUTTON).click()

        #Проверяем, что мы успешно перешли на форму авторизации
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(login_form))

        # Закрываем браузер
        driver.quit()

    #Получаем ошибку, при вводе невалидного пароля
    def test_invalid_password(self, driver):
        driver.get(main_site)

        # Нажимаем на кнопку Личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        # Нажимаем на кнопку Зарегестрироваться
        driver.find_element(*Locators.REG_BUTTON).click()

        # Генерируем случайный email и невалидный пароль для регистрации
        email = generate_random_email()
        password = generate_random_invalid_password()

        # Заполняем поля Имя, Email и Пароль для регистрации
        driver.find_element(*Locators.FIELD_NAME).send_keys(Credentials.name)
        driver.find_element(*Locators.FIELD_EMAIL).send_keys(email)
        driver.find_element(*Locators.FIELD_PASSWORD).send_keys(password)

        # Нажимаем на кнопку Зарегестрироваться
        driver.find_element(*Locators.REG_2_BUTTON).click()

        WebDriverWait(driver, 5)
        assert driver.find_element(*Locators.PASSWORD_ERROR).text == 'Некорректный пароль'

        # Закрываем браузер
        driver.quit()










