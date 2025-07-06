# 🛒 Fakestore API Tests

Автоматизированные тесты на Python для REST API [Fake Store API](https://fakestoreapi.com), реализованные с использованием `pytest`, `requests` и `allure-pytest`. Проект создан как часть портфолио и демонстрирует навыки API-тестирования, генерации отчетов, структурирования кода и CI/CD.

---

## 🔍 Что покрыто

- ✅ Аутентификация (успешный и неуспешный логин)
- ✅ Получение товаров, проверка структуры и данных
- ✅ Работа с корзиной (создание, просмотр, валидация)
- ✅ Структурированные отчёты с Allure
- ⚙️ Готов к CI/CD (GitHub Actions)

---

## ⚙️ Установка и запуск

1. Клонируй проект:
   ```bash
   git clone https://github.com/IgorGeraskin22/fakestore-api-tests.git
   cd fakestore-api-tests
   ```

2. Создай виртуальное окружение:
   ```bash
   python -m venv venv
   ```

3. Активируй окружение:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

4. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```

5. Запусти тесты:
   ```bash
   pytest -v
   ```

6. Генерация Allure отчёта:
   ```bash
   pytest --alluredir=allure-results
   allure serve allure-results
   ```

7. Локальный HTML-отчёт (альтернатива):
   Открыть `reports/report.html` в браузере.

---

## 📂 Структура проекта

```text
fakestore-api-tests/
├── .github/                 # GitHub Actions workflows
│   └── workflows/
│       └── tests.yml
├── reports/                # Allure/HTML отчёты
│   └── report.html
├── tests/
│   ├── testdata/
│   ├── confest.py
│   ├── test_auth.py
│   ├── test_cart.py
│   └── test_products.py
├── utils/
│   ├── __init__.py
│   ├── api_client.py
│   └── auth_api.py
├── start.py
├── requirements.txt
├── pytest.ini
├── README.md
```

---

## 📊 Allure отчёт

В отчёте отображаются:

- Общая статистика по тестам
- Разделение по функционалу (авторизация, корзина, товары)
- Сюжеты (Stories) и признаки (Features)
- Графики и тренды успешности

![Allure report overview](https://raw.githubusercontent.com/IgorGeraskin22/fakestore-api-tests/main/reports/allure_screenshot_example.png)

> 🔽 *Изображение выше — пример. В реальном README нужно положить скриншот `png` рядом с `README.md`, например: `reports/allure_screenshot_example.png`*

---

## 🧰 Используемые технологии

- 🐍 Python 3.8+
- ✅ Pytest
- 🌐 Requests
- 📋 Allure (allure-pytest)
- ☁️ GitHub Actions (CI/CD)

---

## ➕ Как добавить новый тест

1. Создай файл `test_<модуль>.py` в `tests/`
2. Импортируй клиент из `utils/api_client.py` или `auth_api.py`
3. Оформи тест с `@allure.feature` и `@allure.story`

Пример:
```python
import allure
from utils.api_client import send_request

@allure.feature("Orders")
@allure.story("Unauthorized order creation")
def test_create_order_unauthorized():
    response = send_request("POST", "/orders", json={})
    assert response.status_code == 401
```

---

## 🔄 CI/CD (GitHub Actions)

- Автозапуск тестов при push
- Генерация отчёта
- Возможна интеграция с Telegram и GitHub Pages

Файл:
```
.github/workflows/tests.yml
```

---

## 🔗 Ссылки

- 🌐 API Docs: [https://fakestoreapi.com](https://fakestoreapi.com)
- 💻 GitHub: [https://github.com/IgorGeraskin22/fakestore-api-tests](https://github.com/IgorGeraskin22/fakestore-api-tests)

---

## 👤 Автор

**Игорь Гераскин — QA Engineer**  
📧 alonigor16@gmail.com
💼 https://t.me/IgStrive

---
