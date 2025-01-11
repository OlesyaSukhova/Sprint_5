from locators import Locators
from curl import *

class TestTabNavigation:
    # Успешный переход в раздел Соусы
    def test_successful_tab_by_button_sauces_on_constructor_page(self, driver):
        driver.get(main_site)

        # Нажимаем на кнопку Соусы
        driver.find_element(*Locators.SAUCES_BUTTON).click()

        # Проверяем, что таб с булками стал неактивным
        assert 'tab_tab_type_current' not in driver.find_element(*Locators.BREAD_BUTTON).get_attribute('class')

        # Проверяем, что таб с соусами стал активным
        assert 'tab_tab_type_current' in driver.find_element(*Locators.SAUCES_BUTTON).get_attribute('class')

    # Успешный переход в раздел Булки
    def test_successful_tab_by_button_bread_on_constructor_page(self, driver):
        driver.get(main_site)

        # Нажимаем на кнопку Соусы
        driver.find_element(*Locators.SAUCES_BUTTON).click()

        # Нажимаем на кнопку Булки
        driver.find_element(*Locators.BREAD_BUTTON).click()

        # Проверяем, что таб с соусами стал неактивным
        assert 'tab_tab_type_current' not in driver.find_element(*Locators.SAUCES_BUTTON).get_attribute('class')

        # Проверяем, что таб с булками стал активным
        assert 'tab_tab_type_current' in driver.find_element(*Locators.BREAD_BUTTON).get_attribute('class')

    # Успешный переход в раздел Начинки
    def test_successful_tab_by_button_fillings_on_constructor_page(self, driver):
        driver.get(main_site)

        # Нажимаем на кнопку Начинки
        driver.find_element(*Locators.FILLINGS_BUTTON).click()

        # Проверяем, что таб с булками стал неактивным
        assert 'tab_tab_type_current' not in driver.find_element(*Locators.BREAD_BUTTON).get_attribute('class')

        # Проверяем, что таб с начинками стал активным
        assert 'tab_tab_type_current' in driver.find_element(*Locators.FILLINGS_BUTTON).get_attribute('class')


