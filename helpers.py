from faker import Faker

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from curl import main_site
from data import Credentials
from locators import Locators

faker = Faker()

def generate_random_email():
    name = faker.first_name()
    surname = faker.last_name()
    group_number = faker.random.randint(1, 20)
    number = faker.random.randint(100, 999)
    return name + surname + str(group_number) + str(number) + '@mail.ru'

def generate_random_password():
    password = faker.password(length=6)
    return password

def generate_random_invalid_password():
    password = faker.password(length=5)
    return password


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