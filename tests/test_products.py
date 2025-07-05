import pytest
import allure
from utils.api_client import get_products, get_product


@allure.feature("Товары")
@allure.story("Получение всех товаров")
@allure.severity(allure.severity_level.NORMAL)
def test_get_all_products():
    with allure.step("Отправляем GET-запрос на получение всех товаров"):
        response = get_products()
    with allure.step("Проверяем статус-код и содержимое ответа"):
        assert response.status_code == 200
        products = response.json()
        assert isinstance(products, list)
        assert len(products) > 0


@allure.feature("Товары")
@allure.story("Получение товара по ID")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("product_id", [1, 2, 3])
def test_get_product_by_id(product_id):
    with allure.step(f"Отправляем GET-запрос на получение товара с ID {product_id}"):
        response = get_product(product_id)
    with allure.step("Проверяем, что товар успешно получен"):
        assert response.status_code == 200
        product = response.json()
        assert product["id"] == product_id
        assert "title" in product
