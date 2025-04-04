from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestGoToPersonalAccount:

    def test_go_to_personal_account_without_authorization(self, driver):
        # дождаться появления логотипа на странице
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.HEADER_LOGO))
        # найти ссылку "Личный Кабинет" и кликнуть по ней
        driver.find_element(*Locators.LINK_PERSONAL_ACCOUNT).click()
        # дождаться появления заголовка "Вход"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.BUTTON_ENTRANCE))
        assert 'login' in driver.current_url
