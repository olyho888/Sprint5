from locators import Locators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration(Locators):

    def test_successful_registration(self, driver, generate_email, generate_password):
        email = generate_email()
        password = generate_password()
        # дождаться появления логотипа на странице
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.HEADER_LOGO))
        # найти кнопку "Войти в аккаунт" и кликнуть по ней
        driver.find_element(*self.LOGIN_TO_ACCOUNT).click()
        # дождаться появления заголовка "Вход"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.BUTTON_ENTRANCE))
        # найти ссылку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(*self.LINK_REGISTER).click()
        # дождаться появления заголовка "Регистрация"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.TITLE_REGISTRATION))
        # найти поле для ввода "Имя" ввести данные
        driver.find_element(*self.NAME_INPUT).send_keys("Oksana")
        # найти поле для ввода "Email" ввести данные
        driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        # найти поле для ввода "Пароль" ввести данные
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        # найти кнопку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(*self.BUTTON_REGISTER).click()
        # дождаться появления кнопки "Войти"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.BUTTON_SIGN_IN))
        element = driver.find_element(*self.BUTTON_ENTRANCE)
        assert element.text == 'Вход'

    def test_invalid_registration(self, driver, generate_email, generate_password):
        email = generate_email()
        password = generate_password(3)
        # дождаться появления логотипа на странице
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.HEADER_LOGO))
        # найти кнопку "Войти в аккаунт" и кликнуть по ней
        driver.find_element(*self.LOGIN_TO_ACCOUNT).click()
        # дождаться появления заголовка "Вход"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.BUTTON_ENTRANCE))
        # найти ссылку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(*self.LINK_REGISTER).click()
        # дождаться появления заголовка "Регистрация"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.TITLE_REGISTRATION))
        # найти поле для ввода "Имя" ввести данные
        driver.find_element(*self.NAME_INPUT).send_keys("Oksana")
        # найти поле для ввода "Email" ввести данные
        driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        # найти поле для ввода "Пароль" ввести данные
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        # найти кнопку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(*self.BUTTON_REGISTER).click()
        # найти сообщение об ошибке "Некорректный пароль"
        element = driver.find_element(*self.INCORRECT_PASSWORD)
        assert "input__error" in element.get_attribute("class")
