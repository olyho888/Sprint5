from selenium import webdriver
import pytest
import random
import string


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture
def generate_email():
    def create_email(username="OksanaLyho"):
        digits = random.randint(100, 999)
        if len(username) == 0:
            username = "OksanaLyho"
        email = f"{username}20{digits}@yandex.ru"
        return email
    return create_email

@pytest.fixture
def generate_password():
    def create_password(length=6):
        characters = string.digits
        password = ''
        for i in range(length):
            password += random.choice(characters)
        return password
    return create_password
