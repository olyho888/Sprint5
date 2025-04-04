from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Data


class TestLogout:

    def test_logout(self, driver):
        # дождаться появления логотипа на странице
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.HEADER_LOGO))
        # найти кнопку "Войти в аккаунт" и кликнуть по ней
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        # дождаться появления заголовка "Вход"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.BUTTON_ENTRANCE))
        # найти поле для ввода "Email" ввести данные
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Data.user["email"])
        # найти поле для ввода "Пароль" ввести данные
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Data.user["password"])
        # найти кнопку "Войти" и кликнуть по ней
        driver.find_element(*Locators.BUTTON_SIGN_IN).click()
        # найти ссылку "Личный Кабинет" и кликнуть по ней
        driver.find_element(*Locators.LINK_PERSONAL_ACCOUNT).click()
        # дождаться появления заголовка "Профиль"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.TITLE_PROFILE))
        # найти кнопку "Выход" и кликнуть по ней
        driver.find_element(*Locators.BUTTON_LOGOUT).click()
        # дождаться появления заголовка "Вход"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.BUTTON_ENTRANCE))
        assert 'login' in driver.current_url
