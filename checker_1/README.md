### Автоматическая проверка аккаунтов на валидность с использованием Python и Selenium
Cкрипт checker.py предназначен для автоматической проверки аккаунтов на валидность с сайта loliland.net. Он использует библиотеки selenium и fake_useragent для имитации реального пользователя и проверки аккаунтов из файла accounts_check.txt. <br>
 В зависимости от результата проверки, аккаунты записываются в разные файлы:<br>

1. Если аккаунт валиден и имеет баланс 0, он записывается в файл results.txt. 
2. Если аккаунт валиден и имеет баланс более 0, он записывается обратно в файл accounts_check.txt.<br>
При использовании установить
```bash
sudo apt update
sudo apt intsall python
sudo apt install python3 python3-pip
sudo apt intsall python
pip install selenium fake_useragent
```
Для запуска программы
```bash
python ./checker.py
```
