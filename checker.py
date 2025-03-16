from selenium import webdriver  # управление браузером
from selenium.webdriver.common.by import By  # поиск элементов HTML 
from selenium.webdriver.common.keys import Keys  # работа с клавишами клавиатуры
import time  # для паузы в действиях

# Данные для входа
login = "Check_account"
password = "Yoghurt8"

# Настройки браузера
options = webdriver.ChromeOptions()
#options.add_argument("--headless")  # Закомментировать, если нужен видимый браузер

driver = webdriver.Chrome(options=options)  # инициализация браузера с заданными настройками

try:
    # Открываем сайт
    driver.get("https://loliland.net/start")
    time.sleep(5)  # Ждем загрузки страницы

    # Находим поле логина (по placeholder)
    login_field = driver.find_element(By.XPATH, "//input[@placeholder='Логин']")
    login_field.send_keys(login)

    # Находим поле пароля (по placeholder)
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Пароль']")
    password_field.send_keys(password)

    # Ищем кнопку входа (она внутри <div class="btn-drop">) и кликаем
    login_button = driver.find_element(By.CLASS_NAME, "btn-drop")
    login_button.click()

    time.sleep(3)  # Ждем входа

    # Проверяем успешный вход по наличию элемента с классом 'profile_div'
    try:
        profile_div = driver.find_element(By.CLASS_NAME, "profile_div")
        print(f"✅ Успешный вход! {login}:{password}")
    except:
        print(f"❌ Ошибка входа! {login}:{password}")

finally:
    driver.quit()  # Закрываем браузер
