from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains
import random  # для генерации случайных чисел
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Создаем экземпляр UserAgent
ua = UserAgent()

# Генерируем случайный пользовательский агент
random_user_agent = ua.random

# Настройки браузера
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={random_user_agent}")  # Устанавливаем случайный пользовательский агент
options.add_argument("--headless")  # Закомментировать, если нужен видимый браузер
# для меньшего шанса обнаружения
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
#options.add_argument('--proxy-server=IP:PORT') использование прокси

# Инициализация браузера с заданными настройками
driver = webdriver.Chrome(options=options)  
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") # 

# Эмуляция движения мышки
action = ActionChains(driver)
action.move_by_offset(random.randint(100, 400), random.randint(100, 400)).perform()

# Файлы для входа и результатов
input_file = "accounts_check.txt"
valid_file = "valid.txt"
invalid_file = "invalid.txt"

cnt = 0

try:
    # Читаем логины и пароли из файла
    with open(input_file, "r") as file:
        accounts = file.readlines()
    print(f"Количество аккаунтов на проверке: {len(accounts)}")
    # Заходим на сайт
    driver.get("https://funtime.su/")
    time.sleep(random.randint(3, 5))  

    button = driver.find_element(By.XPATH, "//div[@id='method_select']/p[text()='Навсегда']")
    button.click()
    time.sleep(random.randint(1, 3))
    buy_button = driver.find_element(By.ID, 'buy_button')
    buy_button.click()
    time.sleep(random.randint(1, 3))

    for account in accounts:
        cnt += 1
        nickname = account.strip()
        print(f'🔄 Проверка аккаунта {nickname}   {cnt}/{len(accounts)}')
        input_nick = driver.find_element(By.ID, 'input_nick')
        flag_1 = flag_2 = True
        input_nick.click()
        input_nick.clear()
        input_nick.send_keys(nickname)
        time.sleep(random.randint(1, 3))
        button = driver.find_element(By.CSS_SELECTOR, '[data-ind="method_button"]')
        button.click()
        time.sleep(random.randint(1, 3))

        # Обработка всплывающих окон
        try:
            # Проверка на "Аккаунт не найден!"
            error_message = driver.find_element(By.XPATH, "//div[@class='swal2-html-container' and contains(text(), 'Аккаунт не найден!')]")
            if error_message.is_displayed():
                with open(invalid_file, "a") as file:
                    file.write(f"{nickname}: не найден\n")
                print(f"❌ {nickname}: не найден")
                ok_button = driver.find_element(By.CSS_SELECTOR, '.swal2-confirm')
                ok_button.click()
                time.sleep(random.randint(1, 3)) 
                flag_1 = False
        except:
            pass

        try:
            # Проверка на "У вас уже стоит данная привилегия!"
            error_message = driver.find_element(By.XPATH, "//div[@class='swal2-html-container' and contains(text(), 'У вас уже стоит данная привилегия!')]")
            if error_message.is_displayed():
                with open(valid_file, "a") as file:
                    file.write(f"{nickname}: Уже имеет привилегию\n")
                print(f"✅ {nickname}: Привилегия уже активна")
                ok_button = driver.find_element(By.CSS_SELECTOR, 'button.swal2-confirm')
                ok_button.click()
                time.sleep(random.randint(1, 3)) 
                flag_2 = False
        except:
            pass


        if flag_1 and flag_2:
            print(f"❌ {nickname}: прошел проверку и доступна покупка")
            with open(invalid_file, "a") as file:
                    file.write(f"{nickname}: прошел проверку и доступна покупка\n")
       
    

finally:
    driver.quit()
    print("🏁 Проверка успешно завершена!")
