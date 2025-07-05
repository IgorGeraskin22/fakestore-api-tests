import allure
from utils.api_client import create_cart, get_cart, delete_cart


@allure.feature("Корзина")
@allure.story("Создание корзины")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_cart():
    user_id = 1
    cart_payload = {
        "userId": user_id,
        "date": "2025-07-05",
        "products": [{"productId": 1, "quantity": 1}]
    }

    with allure.step(f"Отправляем POST-запрос на создание корзины для user_id={user_id}"):
        response = create_cart(cart_payload)
    with allure.step("Проверяем, что корзина создана"):
        assert response.status_code == 200
        assert "id" in response.json()


@allure.feature("Корзина")
@allure.story("Получение корзины")
@allure.severity(allure.severity_level.NORMAL)
def test_get_cart():
    cart_id = 1
    with allure.step(f"Отправляем GET-запрос на получение корзины с ID {cart_id}"):
        response = get_cart(cart_id)
    with allure.step("Проверяем, что корзина получена успешно"):
        assert response.status_code == 200
        assert response.json().get("id") == cart_id


@allure.feature("Корзина")
@allure.story("Удаление корзины")
@allure.severity(allure.severity_level.MINOR)
def test_delete_cart():
    cart_id = 7  # Убедитесь, что корзина с этим ID существует
    with allure.step(f"Отправляем DELETE-запрос на удаление корзины с ID {cart_id}"):
        response = delete_cart(cart_id)
    with allure.step("Проверяем, что корзина удалена и вернулся объект с ID"):
        assert response.status_code == 200
        response_data = response.json()
        assert response_data.get("id") == cart_id
