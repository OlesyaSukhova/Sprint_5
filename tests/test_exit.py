from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from curl import main_site, login_form
from helpers import login_action
from locators import Locators


class TestExit:
    # Успешный выход из аккаунта
    def test_successful_tab_by_button_exit(self, driver):
        driver.get(main_site)

        # Нажимаем на кнопку Личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        # Авторизируемся и проверяем, что попали на сайт
        login_action(driver)

        # Еще раз нажимаем на кнопку Личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        # Нажимаем на кнопку "Выход"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.EXIT_BUTTON).click()

        # Проверяем, что попали на страницу авторизации
        assert WebDriverWait(driver, 3).until(expected_conditions.url_to_be(login_form))