from selenium.webdriver.common.by import By


class Locators:

    HEADER_LOGO = (By.XPATH, "//div[contains(@class, 'header__logo')]/a") # логотип страницы
    LOGIN_TO_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']") #кнопка "Войти в аккаунт"
    BUTTON_ENTRANCE = (By.XPATH, "//div[contains(@class, 'Auth_login')]/h2") # заголовок "Вход"
    LINK_REGISTER = (By.XPATH, "//a[text()='Зарегистрироваться']") # ссылка "Зарегистрироваться"
    TITLE_REGISTRATION = (By.XPATH, "//h2[text()='Регистрация']") # заголовок "Регистрация"
    NAME_INPUT = (By.XPATH,"//label[text()='Имя']/following-sibling::input") # поле для ввода "Имя"
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input") # поле для ввода "Email"
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") # поле для ввода "Пароля"
    BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']") # кнопка "Зарегистрироваться"
    INCORRECT_PASSWORD = (By.XPATH, "//fieldset[3]//p[text()='Некорректный пароль']") # сообщение "Некорректный пароль"
    BUTTON_SIGN_IN = (By.XPATH, "//form/button[text()='Войти']") # кнопка "Войти"
    LINK_PERSONAL_ACCOUNT = (By.XPATH, "//a[contains(@class, 'header__link')]/p[text()='Личный Кабинет']")# ссылка "Личный кабинет"
    TITLE_PROFILE = (By.XPATH, "//a[text()='Профиль']") # заголовок "Профиль"
    LINK_PASSWORD_RECOVERY = (By.XPATH, "//p[2]/a[text()='Восстановить пароль']") # линк "Восстановление пароля"
    TITLE_PASSWORD_RECOVERY = (By.XPATH, "//h2[text()='Восстановление пароля']") # заголовок "Восстановление пароля"
    TITLE_SIGN_IN = (By.XPATH, "//p/a[text()='Войти']") # заголовок "Войти"
    LINK_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']/parent::a") # ссылка "Конструктор"
    ELEMENT_ASSEMBLE_BURGER =(By.XPATH, "//h1[text()='Соберите бургер']") # элемент "Собери бургер"
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']") # кнопка "Выход"
    ELEMENT_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div") # элемент "Булки"
    ELEMENT_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::div") # элемент "Соусы"
    ELEMENT_STUFFING = (By.XPATH, "//span[text()='Начинки']/parent::div") # элемент "Начинки"
