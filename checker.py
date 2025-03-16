from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Данные для входа
login = "Check_account"
password = "Yoghurt8"

# Открываем браузер без options
driver = webdriver.Chrome()

# Открываем сайт
driver.get("https://loliland.net/start")
time.sleep(2)  # Ждем загрузки страницы

# Вводим логин
login_field = driver.find_element(By.XPATH, "//input[@placeholder='Логин']")
login_field.send_keys(login)

# Вводим пароль
password_field = driver.find_element(By.XPATH, "//input[@placeholder='Пароль']")
password_field.send_keys(password)

# Нажимаем кнопку "Войти"
login_button = driver.find_element(By.CLASS_NAME, "btn-drop")
login_button.click()

# Ждем входа
time.sleep(3)

# Проверяем, успешно ли вошли
if "dashboard" in driver.current_url or "profile" in driver.page_source:
    print("✅ Успешный вход!")
else:
    print("❌ Ошибка входа, проверьте логин и пароль")

# Закрываем браузер
driver.quit()
