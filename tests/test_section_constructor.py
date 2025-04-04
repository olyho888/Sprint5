from locators import Locators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestSectionConstructor:

    def test_section_sauces(self, driver):
        # дождаться появления логотипа на странице
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.HEADER_LOGO))
        # найти элемент "Соусы" и кликнуть по нему
        element = driver.find_element(*Locators.ELEMENT_SAUCES)
        element.click()
        # проверка что "tab_type_current" присутствует в атрибуте
        assert "tab_type_current" in element.get_attribute("class")

    def test_section_stuffing(self, driver):
        # дождаться появления логотипа на странице
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.HEADER_LOGO))
        # найти элемент "Начинки" и кликнуть по нему
        element = driver.find_element(*Locators.ELEMENT_STUFFING)
        element.click()
        # проверка что "tab_type_current" присутствует в атрибуте
        assert "tab_type_current" in element.get_attribute("class")

    def test_section_buns(self, driver):
        # дождаться появления логотипа на странице
        WebDriverWait(driver, 3).until(ec.presence_of_element_located(Locators.HEADER_LOGO))
        # найти элемент "Начинки" и кликнуть по нему
        driver.find_element(*Locators.ELEMENT_STUFFING).click()
        # найти элемент "Булки" и кликнуть по нему
        element = driver.find_element(*Locators.ELEMENT_BUNS)
        element.click()
        # проверка что "tab_type_current" присутствует в атрибуте
        assert "tab_type_current" in element.get_attribute("class")
