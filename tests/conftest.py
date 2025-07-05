import pytest
import json
import os
from utils.api_client import post_login
from requests.exceptions import RequestException

# ✅ Загружаем пользователей один раз на всю сессию
@pytest.fixture(scope="session")
def test_users():
    """
    Загружает пользователей из файла testdata/users.json.
    Используется один раз за всю сессию тестов.
    """
    path = os.path.join(os.path.dirname(__file__), "testdata", "users.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ✅ Получаем токен авторизации один раз за сессию
@pytest.fixture(scope="session")
def auth_token(test_users):
    """
    Авторизует пользователя valid_user и возвращает токен.
    Кешируется на всю сессию, чтобы не повторять login во всех тестах.
    """
    user = test_users["valid_user"]

    try:
        response = post_login(user["username"], user["password"])
        response.raise_for_status()
    except RequestException as e:
        pytest.exit(f"\n[!] Ошибка при авторизации: {e}")

    try:
        token = response.json().get("token")
        if not token:
            pytest.exit("[!] Не удалось получить токен из ответа login")
        return token
    except json.JSONDecodeError:
        pytest.exit("[!] Невалидный JSON в ответе на login")


# ✅ Используется для негативных сценариев с неправильным токеном
@pytest.fixture
def invalid_token():
    """
    Возвращает заведомо некорректный JWT-токен.
    Используется в тестах на отказ в авторизации.
    """
    return "invalid.token.value"
