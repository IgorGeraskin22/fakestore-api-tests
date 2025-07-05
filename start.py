import os
import subprocess
import sys

ALLURE_CMD = r"C:\Tools\allure\bin\allure.bat"  # Указали путь вручную


def check_allure_installed():
    try:
        subprocess.run([ALLURE_CMD, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("❌ Allure не установлен или недоступен.")
        sys.exit(1)


def run_pytest():
    print("[1/3] Запуск тестов...")
    result = subprocess.run(
        ["pytest", "-n", "auto", "--alluredir=allure-results"],
        shell=True
    )
    if result.returncode != 0:
        print("❌ Некоторые тесты не прошли.")
    else:
        print("✅ Все тесты прошли успешно.")


def generate_allure_report():
    print("[2/3] Генерация Allure-отчёта...")
    result = subprocess.run(
        [ALLURE_CMD, "generate", "allure-results", "-o", "allure-report", "--clean"],
        shell=True
    )
    if result.returncode != 0:
        print("❌ Не удалось сгенерировать Allure-отчёт.")
        sys.exit(1)


def open_report():
    print("[3/3] Открытие отчёта в браузере...")
    result = subprocess.run([ALLURE_CMD, "open", "allure-report"], shell=True)
    if result.returncode != 0:
        print("❌ Не удалось открыть Allure-отчёт.")


if __name__ == "__main__":
    check_allure_installed()
    run_pytest()
    generate_allure_report()
    open_report()
