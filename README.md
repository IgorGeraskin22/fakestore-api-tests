# 🛒 FakeStore API Autotests

Проект с автотестами для публичного [FakeStoreAPI](https://fakestoreapi.com)
---

## 📁 Структура проекта

```
fakestore-api-tests/
├── conftest.py                  # Глобальные фикстуры для pytest
├── pytest.ini                   # Конфигурация pytest
├── requirements.txt             # Зависимости проекта
├── README.md                    # Описание проекта
│
├── utils/
│   └── api_client.py            # Все обращения к API (GET, POST, PUT и т.д.)
│
├── testdata/
│   └── users.json               # Тестовые данные: логины и пароли
│
└── tests/
    ├── test_auth.py            # Тесты на авторизацию
    ├── test_products.py        # Тесты на товары
    └── test_cart.py            # (в разработке) Тесты на корзину
```

---

## 📦 Установки

### 1. Клонируй репозиторий

```bash
git clone https://github.com/yourname/fakestore-api-tests.git
cd fakestore-api-tests
```

### 2. Создай виртуальное окружение и активируй его

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Установи зависимости

```bash
pip install -r requirements.txt
```

---

## 🚀 Как запускать тесты

✅ Все тесты:

```bash
pytest -v
```

📄 Один конкретный файл:

```bash
pytest tests/test_products.py -v
```

📌 Один конкретный тест:

```bash
pytest tests/test_auth.py::test_successful_login -v
```

---

## 🔐 Авторизация

FakeStore API поддерживает простую авторизацию через endpoint:

```
POST /auth/login
```

Пример тела запроса:
```json
{
  "username": "mor_2314",
  "password": "83r5^_"
}
```

---

## 🧪 Покрытие

| Блок       | Методы                            | Статус     |
|------------|------------------------------------|------------|
| ✅ Авторизация | `POST /auth/login`                  | ✔ Протестировано |
| ✅ Товары       | `GET /products`, `GET /{id}`, `PUT` | ✔ Протестировано |
| 🛠 Корзина      | `GET /carts`, `POST /carts` и др.   | 🚧 В разработке |

---

## 📂 Пример testdata/users.json

```json
{
  "valid_user": {
    "username": "mor_2314",
    "password": "83r5^_"
  },
  "invalid_user": {
    "username": "invalid_user",
    "password": "wrong_pass"
  }
}
```

---

## ⚙️ Пример фикстуры `auth_token`

```python
@pytest.fixture
def auth_token(test_users):
    user = test_users["valid_user"]
    response = login_user(user["username"], user["password"])
    assert response.status_code == 200
    return response.json()["token"]
```

---

## ✅ Используемый стек

- Python 3.8+
- `pytest`
- `requests`
- `FakeStoreAPI` (https://fakestoreapi.com)

---

## 📌 Назначение проекта

🔹 Учебный проект для демонстрации навыков:
- API тестирования
- организации кода и тестов
- работы с фикстурами, данными, структурами
- создания тестовых данных через JSON

---

## 💼 Для кого

Этот проект можно добавить в портфолио Junior/Middle QA как пример реального API-тестирования. Хорошо подойдёт для:
- прикрепления на hh.ru
- прохождения тех. собеседований
- демонстрации знаний автотестов

---

## 👤 Автор

А. (QA-инженер, ручное + автоматизированное тестирование API/UI)
