from logging import root

from selenium.webdriver.common.by import By

class Locators:
    #Регистрация
    PERSONAL_ACCOUNT = [By.LINK_TEXT, "Личный Кабинет"]
    REG_BUTTON = [By.LINK_TEXT, "Зарегистрироваться"]
    FIELD_NAME = [By.CSS_SELECTOR, "form fieldset:nth-child(1) input"]
    FIELD_EMAIL = [By.CSS_SELECTOR, "form fieldset:nth-child(2) input"]
    FIELD_PASSWORD = [By.CSS_SELECTOR, "input[type=password]"]
    REG_2_BUTTON = [By.CSS_SELECTOR, "form button"]
    PASSWORD_ERROR = [By.CSS_SELECTOR, ".input__error"]
    #Вход
    ACCOUNT_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button']
    PLACE_AN_ORDER_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button']
    FIELD_EMAIL_LOGIN = [By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input']
    FIELD_PASSWORD_LOGIN = [By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input']
    LOGIN_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/div/div/p/a']
    RECOVER_PASSWORD = [By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a']
    LOGIN_BUTTON_FORGET_PASSWORD = [By.XPATH, '//*[@id="root"]/div/main/div/div/p/a']
    #Выход
    EXIT_BUTTON= [By.CSS_SELECTOR, 'main nav ul li:last-child button']
    #Конструктор
    CONSTRUCTOR_BUTTON = [By.LINK_TEXT, 'Конструктор']
    MAKE_BURGER_LINK = [By.LINK_TEXT, 'Соберите бургер']
    LOGO_STELLAR_BURGERS = [By.CSS_SELECTOR, 'header nav div a']
    SAUCES_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span']
    SPICY_SAUCE = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[1]/p']
    BREAD_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span']
    FLU_BREAD = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/p']
    FILLINGS_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span']
    MEAT_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[1]/p']


