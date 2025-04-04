Автотесты для сервиса Stellar Burgers(https://stellarburgers.nomoreparties.site/)

Основа для написания автотестов — фреймворк pytest и Selenium
Автотесты запускаются в браузере Chrome

class TestRegistration содержит тесты
test_successful_registration - тест на успешную регистрацию
test_invalid_registration - тест на неуспешную регистрацию

class TestAuthorization содержит тесты
test_authorization_account_from_home_page - тест на вход через "Войти в аккаунт" с домашней страницы
test_authorization_via_personal_account - тест на вход в аккаунт через "Личный кабинет"
test_authorization_via_registration_form - тест на вход через кнопку в форме регистрации
test_authorization_via_password_recovery - тест на вход через кнопку в форме восстановления пароля

class TestGoToPersonalAccount содержит тест
test_go_to_personal_account_without_authorization - тест на переход в "Личный кабинет" без авторизации

class TestGoToConstructor содержит тесты
test_go_to_constructor_from_personal_account - тест на переход в "Конструктор" из "Личный кабинет" по клику на "Конструктор"
test_go_to_constructor_from_logotype - тест на переход в "Конструктор" из "Личный кабинет" по клику на "логотип Stellar Burgers"

class TestLogout содержит тест
test_logout - тест на выход из "Личный кабинет" по клику на кнопку "Выход"

class TestSectionConstructor содержит тесты
test_section_sauces - тест на переход к разделу "Соусы"
test_section_stuffing - тест на переход к разделу "Начинки"
test_section_buns - тест на переход к разделу "Булки"
