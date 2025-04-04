from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestGoToConstructor:

    def test_go_to_constructor_from_personal_account(self, driver):
        # дождаться появления логотипа на странице
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.HEADER_LOGO))
        # найти ссылку "Личный Кабинет" и кликнуть по ней
        driver.find_element(*Locators.LINK_PERSONAL_ACCOUNT).click()
        # дождаться появления заголовка "Вход"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.BUTTON_ENTRANCE))
        # найти ссылку "Конструктор" и кликнуть по ней
        driver.find_element(*Locators.LINK_CONSTRUCTOR).click()
        # дождаться появления элемента "Соберите бургер"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.ELEMENT_ASSEMBLE_BURGER))
        element = driver.find_element(*Locators.LINK_CONSTRUCTOR)
        assert 'link_active' in element.get_attribute('class')

    def test_go_to_constructor_from_logotype(self, driver):
        # дождаться появления логотипа на странице
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.HEADER_LOGO))
        # найти ссылку "Личный Кабинет" и кликнуть по ней
        driver.find_element(*Locators.LINK_PERSONAL_ACCOUNT).click()
        # дождаться появления заголовка "Вход"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.BUTTON_ENTRANCE))
        # найти логотип и кликнуть на него
        driver.find_element(*Locators.HEADER_LOGO).click()
        # дождаться появления элемента "Соберите бургер"
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.ELEMENT_ASSEMBLE_BURGER))
        element = driver.find_element(*Locators.LINK_CONSTRUCTOR)
        assert 'link_active' in element.get_attribute('class')
