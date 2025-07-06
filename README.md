# 🛒 Fakestore API Tests

Автоматизированные API-тесты на Python для публичного REST API [Fake Store API](https://fakestoreapi.com).

---

## ✅ Что покрыто

- 🔐 Авторизация: позитивные и негативные кейсы
- 📦 Товары: получение списка и деталей товаров
- 🛒 Корзина: добавление, проверка содержимого
- 🧪 Отчёт Allure
- ⚙️ Интеграция с GitHub Actions (CI)

---

## ⚙️ Установка и запуск

1. Клонируй проект:
   ```bash
   git clone https://github.com/IgorGeraskin22/fakestore-api-tests.git
   cd fakestore-api-tests
   ```

2. Создай и активируй виртуальное окружение:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate      # для Windows
   # или
   source venv/bin/activate    # для Linux/macOS
   ```

3. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Запусти тесты:
   ```bash
   pytest -v
   ```

5. Сгенерируй Allure-отчёт:
   ```bash
   pytest --alluredir=allure-results
   allure serve allure-results
   ```

---

## 📊 Allure-отчёт

🧪 **Allure Report (GitHub Pages)**  
👉 [Открыть полный отчёт Allure в новой вкладке](https://igorgeraskin22.github.io/fakestore-api-tests/)

📌 Отчёт показывает:
- Общее количество тестов и их статус
- Группировку по Feature / Story
- Подробные шаги, логи и графики прогонов

---

## 📂 Структура проекта (с комментариями)

```text
fakestore-api-tests/
├── .github/                       # Настройки CI/CD GitHub Actions
│   └── workflows/
│       └── tests.yml              # CI: прогон тестов при push
├── .pytest_cache/                # Кэш pytest (автоматически создаётся)
├── reports/                      # Отчёты и вспомогательные файлы
│   └── report.html               # Сохранённый HTML-отчёт
├── tests/                        # Все тесты
│   ├── testdata/                 # Тестовые данные (если будут использоваться)
│   ├── confest.py                # Общие фикстуры и настройки pytest
│   ├── test_auth.py              # Тесты авторизации
│   ├── test_cart.py              # Тесты корзины
│   └── test_products.py          # Тесты товаров
├── utils/                        # Вспомогательные модули и API-клиенты
│   ├── __init__.py               # Делает папку пакетом Python
│   ├── api_client.py             # Универсальный HTTP-клиент
│   └── auth_api.py               # Методы для авторизации
├── start.py                      # Точка входа (опционально)
├── api_client.log                # Лог запросов и ответов
├── pytest.ini                    # Конфигурация Pytest
├── requirements.txt              # Зависимости проекта
├── .gitignore                    # Игнорируемые файлы для Git
├── .coverage                     # Отчёт покрытия кода (если используется)
└── README.md                     # Документация проекта
```

---

## 🧰 Используемые технологии

- 🐍 Python 3.8+
- 🧪 Pytest
- 🌐 Requests
- 📋 Allure (allure-pytest)
- ☁️ GitHub Actions

---

## 🧪 Как добавить новый тест

1. Создай файл `test_<модуль>.py` в папке `tests/`
2. Используй `send_request()` или API-модуль из `utils/`
3. Добавь аннотации для Allure

Пример:
```python
import allure
from utils.api_client import send_request

@allure.feature("Orders")
@allure.story("Unauthorized access")
def test_create_order_unauthorized():
    response = send_request("POST", "/orders", json={})
    assert response.status_code == 401
```

---

## 🔄 CI/CD

- Автоматический прогон тестов при `push` и `pull request`
- Конфигурация: `.github/workflows/tests.yml`
- Публикацией Allure-отчёта в GitHub Pages
- Можно расширить:
  - отправкой отчётов в Telegram или Slack

---

## 🔗 Полезные ссылки

- 🌐 Fake Store API: [https://fakestoreapi.com](https://fakestoreapi.com)
- 💻 Репозиторий: [https://github.com/IgorGeraskin22/fakestore-api-tests](https://github.com/IgorGeraskin22/fakestore-api-tests)
- 📊 Allure Report: [https://igorgeraskin22.github.io/fakestore-api-tests/](https://igorgeraskin22.github.io/fakestore-api-tests/)

---

## 👤 Автор
**Игорь Гераскин — QA Engineer**  
📧 ign.mln20@gmail.com
💼 https://t.me/IgStrive
