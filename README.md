# Сайт с аккордами
Сайт для просмотра / добавления / редактирования разборов песен с аккордами. Есть возможность регистрации и логина. Добавление и редактирование песен доступно только залогиненым пользователям. При редактировании разбора достаточно указать аккорд, и сайт автоматически подгрузит подсказку, как этот аккорд зажимается на гитаре

## Локальный запуск
1. Устанавливаем зависимости
```shell
npm install
python3 -m pip install -r requirements.txt
```
2. Запускаем бэк
```shell
./manage.py runserver
```
3. Запускаем фронт
```shell
npm start
```
На http://localhost:3000/ откроется сайт

## Скриншоты
Главная страница
![main_page](https://github.com/Moysenko/ABBYY_Interfaces/blob/master/screenshots/main.png)

Регистрация
![sign_up](https://github.com/Moysenko/ABBYY_Interfaces/blob/master/screenshots/sign_up.png)

Вход
![log_in](https://github.com/Moysenko/ABBYY_Interfaces/blob/master/screenshots/log_in.png)

Добавление разбора песни
![add_song](https://github.com/Moysenko/ABBYY_Interfaces/blob/master/screenshots/add_song.png)

Просмотр разбора песни
![song_with_chords](https://github.com/Moysenko/ABBYY_Interfaces/blob/master/screenshots/song_with_chords.png)
