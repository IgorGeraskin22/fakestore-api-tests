# 🛒 Fakestore API Tests

Автоматизированные тесты на Python для REST API [Fake Store API](https://fakestoreapi.com), реализованные с использованием `pytest`, `requests` и `allure-pytest`. Проект создан как часть портфолио и демонстрирует навыки API-тестирования, работы с отчетами, структурирования кода и CI/CD.

---

## 🔍 Что покрыто

- ✅ Аутентификация (успешный и неуспешный логин)
- ✅ Получение товаров, проверка структуры и данных
- ✅ Работа с корзиной (создание, просмотр, валидация)
- 🧪 Отчёт в HTML (`reports/report.html`)
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

7. Просмотр HTML-отчета (если сформирован вручную):
   Открой файл `reports/report.html` в браузере.

---

## 📂 Структура проекта

```text
fakestore-api-tests/
├── .github/                 # GitHub Actions workflows
│   └── workflows/
│       └── tests.yml
├── .pytest_cache/          # кеш pytest
├── reports/                # Allure/HTML отчёты
│   └── report.html
├── tests/                  # Тесты
│   ├── testdata/           # Тестовые данные
│   ├── confest.py
│   ├── test_auth.py
│   ├── test_cart.py
│   └── test_products.py
├── utils/                  # API клиенты и вспомогательные модули
│   ├── __init__.py
│   ├── api_client.py
│   └── auth_api.py
├── .coverage               # отчёт покрытия
├── .gitignore
├── api_client.log          # лог запросов
├── pytest.ini              # конфигурация Pytest
├── requirements.txt        # зависимости
├── start.py                # точка входа (при необходимости)
└── README.md
```

---

## 📊 Отчёты

- Allure:
  ```bash
  pytest --alluredir=allure-results
  allure serve allure-results
  ```

- HTML:
  Открой файл `reports/report.html`

---

## 🧰 Используемые технологии

- 🐍 Python 3.8+
- ✅ Pytest
- 🌐 Requests
- 📋 Allure
- ☁️ GitHub Actions (CI/CD)

---

## ➕ Как добавить новый тест

1. Создай новый файл в `tests/` (например, `test_orders.py`)
2. Импортируй `send_request()` или готовый API-модуль
3. Используй аннотации `@allure.feature`, `@allure.story`

Пример:
```python
import allure
from utils.api_client import send_request

@allure.feature("Orders")
@allure.story("Create order without auth")
def test_create_order_unauthorized():
    response = send_request("POST", "/orders", json={})
    assert response.status_code == 401
```

---

## 🔄 CI/CD (GitHub Actions)

Тесты автоматически запускаются при каждом push. Отчёт можно расширить до публикации в Telegram или GitHub Pages.

Конфигурация:
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
📧 igor.geraskin@example.com  
💼 [hh.ru/твоя-ссылка](https://hh.ru)
