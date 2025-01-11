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
    ACCOUNT_BUTTON = [By.CSS_SELECTOR, 'section[class*=BurgerConstructor] button[class*=primary]']
    PLACE_AN_ORDER_BUTTON = [By.CSS_SELECTOR, 'section[class*=BurgerConstructor] button[class*=primary]']
    FIELD_EMAIL_LOGIN = [By.CSS_SELECTOR, 'form[class*=Auth_form] input[type=text]']
    FIELD_PASSWORD_LOGIN = [By.CSS_SELECTOR, 'form[class*=Auth_form] input[type=password]']
    LOGIN_BUTTON = [By.CSS_SELECTOR, 'form[class*=Auth_form] button[class*=primary]']
    LOGIN_LINK = [By.CSS_SELECTOR, 'a[href*="/login"]']
    RECOVER_PASSWORD_LINK = [By.CSS_SELECTOR, 'div[class*=Auth_login] a[href*=forgot-password]']
    LOGIN_BUTTON_FORGET_PASSWORD = [By.CSS_SELECTOR, 'form[class*=Auth_form] button[class*=primary]']
    #Выход
    EXIT_BUTTON = [By.CSS_SELECTOR, 'main nav ul li:last-child button']
    #Конструктор
    CONSTRUCTOR_BUTTON = [By.CSS_SELECTOR, 'ul[class*=AppHeader_header__list] li:nth-child(1) a']
    LOGO_STELLAR_BURGERS = [By.CSS_SELECTOR, 'header nav div a']
    BREAD_BUTTON = [By.CSS_SELECTOR, 'section[class*=BurgerIngredients] div[class*=tab_tab]:nth-child(1)']
    SAUCES_BUTTON = [By.CSS_SELECTOR, 'section[class*=BurgerIngredients] div[class*=tab_tab]:nth-child(2)']
    FILLINGS_BUTTON = [By.CSS_SELECTOR, 'section[class*=BurgerIngredients] div[class*=tab_tab]:nth-child(3)']


