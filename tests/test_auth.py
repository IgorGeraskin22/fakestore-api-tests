import allure
from utils.api_client import post_login


@allure.feature("Авторизация")
@allure.story("Успешный логин")
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_login(test_users):
    user = test_users["valid_user"]
    with allure.step("Отправляем запрос с валидными логином и паролем"):
        response = post_login(user["username"], user["password"], timeout=5)
    with allure.step("Проверяем успешность входа и наличие токена"):
        assert response.status_code == 200
        assert "token" in response.json()


@allure.feature("Авторизация")
@allure.story("Пустые поля")
@allure.severity(allure.severity_level.NORMAL)
def test_login_empty_credentials(test_users):
    user = test_users["empty_user"]
    with allure.step("Отправляем запрос с пустыми логином и паролем"):
        response = post_login(user["username"], user["password"], timeout=5)
    with allure.step("Ожидаем статус-код 400 — ошибка валидации"):
        assert response.status_code == 400


@allure.feature("Авторизация")
@allure.story("Неверные учётные данные")
@allure.severity(allure.severity_level.NORMAL)
def test_failed_login_invalid_credentials(test_users):
    user = test_users["invalid_user"]
    with allure.step("Отправляем запрос с неверным логином и паролем"):
        response = post_login(user["username"], user["password"], timeout=5)
    with allure.step("Ожидаем статус-код 401 — Unauthorized"):
        assert response.status_code == 401


@allure.feature("Авторизация")
@allure.story("SQL-инъекция")
@allure.severity(allure.severity_level.NORMAL)
def test_login_sql_injection(test_users):
    user = test_users["sql_injection_user"]
    with allure.step("Отправляем попытку входа через SQL-инъекцию"):
        response = post_login(user["username"], user["password"], timeout=5)
    with allure.step("Ожидаем статус-код 401 — Unauthorized"):
        assert response.status_code == 401
