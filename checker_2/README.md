### Автоматическая проверка аккаунтов на валидность с использованием Python и Selenium
Cкрипт checker.py предназначен для автоматической проверки наличия некоторых параметров на сайте funtime.su Он использует библиотеки selenium и fake_useragent для имитации реального пользователя и проверки никнеймов из файла accounts_check.txt. <br>
В зависимости от результата проверки, аккаунты записываются в разные файлы:<br>

1. Если никнейм валиден и имеет привилегию, он записывается в файл valid.txt. 
2. Если никнейм валиден и доступна покупка на привилегию или не существует, он записывается в файл invalid.txt.<br>
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
