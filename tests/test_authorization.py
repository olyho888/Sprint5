from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Data


class TestAuthorization(Locators):

    def test_authorization_account_from_home_page(self, driver):
        # дождаться появления логотипа на странице
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.HEADER_LOGO))
        # найти кнопку "Войти в аккаунт" и кликнуть по ней
        driver.find_element(*self.LOGIN_TO_ACCOUNT).click()
        # дождаться появления заголовка "Вход"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.BUTTON_ENTRANCE))
        # найти поле для ввода "Email" ввести данные
        driver.find_element(*self.EMAIL_INPUT).send_keys(Data.user["email"])
        # найти поле для ввода "Пароль" ввести данные
        driver.find_element(*self.PASSWORD_INPUT).send_keys(Data.user["password"])
        # найти кнопку "Войти" и кликнуть по ней
        driver.find_element(*self.BUTTON_SIGN_IN).click()
        # найти ссылку "Личный Кабинет" и кликнуть по ней
        driver.find_element(*self.LINK_PERSONAL_ACCOUNT).click()
        # дождаться появления заголовка "Профиль"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.TITLE_PROFILE))
        assert 'profile' in driver.current_url

    def test_authorization_via_personal_account(self, driver):
        # дождаться появления логотипа на странице
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.HEADER_LOGO))
        # найти ссылку "Личный Кабинет" и кликнуть по ней
        driver.find_element(*self.LINK_PERSONAL_ACCOUNT).click()
        # дождаться появления заголовка "Вход"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.BUTTON_ENTRANCE))
        # найти поле для ввода "Email" ввести данные
        driver.find_element(*self.EMAIL_INPUT).send_keys(Data.user["email"])
        # найти поле для ввода "Пароль" ввести данные
        driver.find_element(*self.PASSWORD_INPUT).send_keys(Data.user["password"])
        # найти кнопку "Войти" и кликнуть по ней
        driver.find_element(*self.BUTTON_SIGN_IN).click()
        # найти ссылку "Личный Кабинет" и кликнуть по ней
        driver.find_element(*self.LINK_PERSONAL_ACCOUNT).click()
        # дождаться появления заголовка "Профиль"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.TITLE_PROFILE))
        assert 'profile' in driver.current_url

    def test_authorization_via_registration_form(self,driver):
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
        # найти заголовок "Войти" и кликнуть по нему
        driver.find_element(*self.TITLE_SIGN_IN).click()
        # дождаться появления заголовка "Вход"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.BUTTON_ENTRANCE))
        # найти поле для ввода "Email" ввести данные
        driver.find_element(*self.EMAIL_INPUT).send_keys(Data.user["email"])
        # найти поле для ввода "Пароль" ввести данные
        driver.find_element(*self.PASSWORD_INPUT).send_keys(Data.user["password"])
        # найти кнопку "Войти" и кликнуть по ней
        driver.find_element(*self.BUTTON_SIGN_IN).click()
        # найти ссылку "Личный Кабинет" и кликнуть по ней
        driver.find_element(*self.LINK_PERSONAL_ACCOUNT).click()
        # дождаться появления заголовка "Профиль"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.TITLE_PROFILE))
        assert 'profile' in driver.current_url

    def test_authorization_via_password_recovery(self,driver):
        # дождаться появления логотипа на странице
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.HEADER_LOGO))
        # найти ссылку "Личный Кабинет" и кликнуть по ней
        driver.find_element(*self.LINK_PERSONAL_ACCOUNT).click()
        # дождаться появления заголовка "Вход"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.BUTTON_ENTRANCE))
        # найти ссылку "Восстановить пароль" и кликнуть по ней
        driver.find_element(*self.LINK_PASSWORD_RECOVERY).click()
        # дождаться появления заголовка "Восстановление пароля"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.TITLE_PASSWORD_RECOVERY))
        # найти заголовок "Войти" и кликнуть по ней
        driver.find_element(*self.TITLE_SIGN_IN).click()
        # дождаться появления заголовка "Вход"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.BUTTON_ENTRANCE))
        # найти поле для ввода "Email" ввести данные
        driver.find_element(*self.EMAIL_INPUT).send_keys(Data.user["email"])
        # найти поле для ввода "Пароль" ввести данные
        driver.find_element(*self.PASSWORD_INPUT).send_keys(Data.user["password"])
        # найти кнопку "Войти" и кликнуть по ней
        driver.find_element(*self.BUTTON_SIGN_IN).click()
        # найти ссылку "Личный Кабинет" и кликнуть по ней
        driver.find_element(*self.LINK_PERSONAL_ACCOUNT).click()
        # дождаться появления заголовка "Профиль"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(self.TITLE_PROFILE))
        assert 'profile' in driver.current_url
