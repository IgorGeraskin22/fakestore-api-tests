# 🧪 FakeStore API Tests

Проект автоматизированного тестирования для публичного REST API: [https://fakestoreapi.com](https://fakestoreapi.com)

## 📌 Цель

Демонстрация навыков написания API-автотестов с использованием Python, Pytest, Allure и CI/CD (GitHub Actions). Подходит для портфолио QA-инженера.

## ✅ Покрытие

Реализованы тесты на следующие бизнес-функции:

- 🔐 Аутентификация (`POST /auth/login`)
- 🛒 Работа с корзиной (`/carts`)
- 🛍️ Работа с товарами (`/products`)
- 📁 Категории товаров (`/products/categories`)
- 🔄 Обновление и удаление сущностей
- 🚫 Негативные кейсы: неверные данные, пустые поля, SQL-инъекция, неавторизованные запросы

## 🧱 Структура проекта

```bash
fakestore-api-tests/
├── README.md              # Описание проекта
├── pytest.ini             # Конфигурация Pytest
├── requirements.txt       # Зависимости проекта
├── start.py               # Быстрый запуск тестов (опционально)
│
├── tests/                 # Все автотесты
│   ├── conftest.py        # Фикстуры (в том числе токены, тест-данные)
│   ├── test_auth.py       # Тесты логина
│   ├── test_cart.py       # Тесты корзины
│   └── test_products.py   # Тесты товаров и категорий
│
├── utils/                 # Вспомогательные модули
│   ├── __init__.py
│   ├── api_client.py      # Универсальный клиент (GET, POST и т.д.)
│   └── auth_api.py        # Отдельный модуль логина
│
└── testdata/
    └── users.json         # Тестовые данные (валидные и невалидные пользователи)
```

## 🚀 Как запустить

1. Установите зависимости:

```bash
pip install -r requirements.txt
```

2. Запуск всех тестов:

```bash
pytest -v
```

3. Запуск с Allure:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

4. Параллельный запуск:

```bash
pytest -n 4 -v
```

## ⚙️ Технологии

- Python 3.8+
- Pytest
- Allure-pytest
- Pytest-xdist
- requests

## 🧪 Покрытие негативных кейсов

- Пустые логин/пароль
- SQL-инъекции
- Обновление/удаление несуществующих сущностей
- Ошибки авторизации
- Пустые payload'ы

## 📦 CI/CD (опционально)

Если проект опубликован на GitHub — можно подключить GitHub Actions для автозапуска тестов и отправки отчетов в Telegram.

---

© 2025. Проект подготовлен для демонстрации навыков QA Automation.
