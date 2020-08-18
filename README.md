# Watcher | Наблюдатель

### Зависимости:
* [python 3.6+](https://www.python.org/)
* pip install opencv-python
* pip install pynput
* pip install keyboard
* pip install pyTelegramBotAPI
* pip install pyinstaller

### Описание
Хотите знать, пользуются ли вашим компьютером, когда вас нет рядом? Watcher может решить эту задачу. После запуска приложения, курсор будет переведен на нулевые координаты (можно изменить, 12 строка), после этого, если курсор будет сдвинут, камера компьютера сделает 3 фото и отправит их в телеграм канал (нужно создать), после задержки в 5 сек., курсор будет перемещен обратно на 0 координату (можно изменить, 50 строка), это сделанно на случай, если кто-то случайно заденет мышь компьютера! 

Для работы, вам нужно создать бота в телеграм и записать его токен на 9 строке, а на 10 строке, ввести id канала, куда будут отправлены фото. Бота нужно добавить в качестве админа!

После того, как вы заполнили 9 и 10 строи, можно собрать .exe файл, выполнив команду:
* pyinstaller -F --onefile --nocosole main.py

Создайте ярлык программы и добавьте в автозагрузку: c:\Users\ЛОГИН УЧЕТНОЙ ЗАПИСИ\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup это позволит запускаться программе даже после перезагрузки системы.

* Комбинация клавишь **alt+a** (27 строка) переведет программу в режим ожидания и переместит курсор на координаты 500, 500 (для понимамия, что программа не активна)
* Комбинация клавишь **ctrl+alt** (20 строка) переведет программу в активный режим

