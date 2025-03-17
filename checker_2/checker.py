from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains
import random  # для генерации случайных чисел

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
valid_file = "valid.txt"
invalid_file = "invalid.txt"


try:
    # Читаем логины и пароли из файла
    with open(input_file, "r") as file:
        accounts = file.readlines()

    # заходим на сайт
    driver.get("https://funtime.su/")
    time.sleep(random.randint(5, 10))  

    button = driver.find_element(By.XPATH, "//div[@id='method_select']/p[text()='Навсегда']")
    button.click()
    time.sleep(random.randint(3, 5))
    buy_button = driver.find_element(By.ID, 'buy_button')
    buy_button.click()
    time.sleep(random.randint(3, 5))

    for account in accounts:
        
        nickname = account.strip()

        input_nick = driver.find_element(By.ID, 'input_nick')

        input_nick.click()
        input_nick.clear()
        input_nick.send_keys(nickname)
        time.sleep(random.randint(3, 5))
        button = driver.find_element(By.CSS_SELECTOR, '[data-ind="method_button"]')
        button.click()
        time.sleep(random.randint(3, 5))

        print(f'🔄 Проверка аккаунта {nickname}')



finally:
    driver.quit()
    print("🏁 Проверка успешно завершена!")