from locators import Locators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_successful_registration(self, driver, generate_email, generate_password):
        email = generate_email()
        password = generate_password()
        # дождаться появления логотипа на странице
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.HEADER_LOGO))
        # найти кнопку "Войти в аккаунт" и кликнуть по ней
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        # дождаться появления заголовка "Вход"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.BUTTON_ENTRANCE))
        # найти ссылку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(*Locators.LINK_REGISTER).click()
        # дождаться появления заголовка "Регистрация"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.TITLE_REGISTRATION))
        # найти поле для ввода "Имя" ввести данные
        driver.find_element(*Locators.NAME_INPUT).send_keys("Oksana")
        # найти поле для ввода "Email" ввести данные
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        # найти поле для ввода "Пароль" ввести данные
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        # найти кнопку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        # дождаться появления кнопки "Войти"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.BUTTON_SIGN_IN))
        element = driver.find_element(*Locators.BUTTON_ENTRANCE)
        assert element.text == 'Вход'

    def test_invalid_registration(self, driver, generate_email, generate_password):
        email = generate_email()
        password = generate_password(3)
        # дождаться появления логотипа на странице
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.HEADER_LOGO))
        # найти кнопку "Войти в аккаунт" и кликнуть по ней
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        # дождаться появления заголовка "Вход"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.BUTTON_ENTRANCE))
        # найти ссылку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(*Locators.LINK_REGISTER).click()
        # дождаться появления заголовка "Регистрация"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.TITLE_REGISTRATION))
        # найти поле для ввода "Имя" ввести данные
        driver.find_element(*Locators.NAME_INPUT).send_keys("Oksana")
        # найти поле для ввода "Email" ввести данные
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        # найти поле для ввода "Пароль" ввести данные
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        # найти кнопку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(*Locators.BUTTON_REGISTER).click()
        # найти сообщение об ошибке "Некорректный пароль"
        element = driver.find_element(*Locators.INCORRECT_PASSWORD)
        assert "input__error" in element.get_attribute("class")
