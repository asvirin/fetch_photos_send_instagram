
# Парсинг фотографий компании SpaceX и телескопа Hubble и отправка их в Instagram

Программа позволяет парсить фотографии с запусков Space X и от телескопа Hubble и отправлять в Instagram без использования официального API.

# Как установить

Для парсинга фотографий компании Spase X достаточно вызвать функцию fetch_spacex без параметров, например fetch_spacex(). 
Для парсинга фотографий телескопа Hubble необходимо вызвать функцию fetch_hubble с параметром названия коллекции, например fetch_hubble(holiday_cards)

Параметры проекта находятся в специальном .env файле. Документация и примеры доступны на странице проекта [repl.it](https://repl.it/site/docs/repls/secret-keys).
В файле 4 переменных:
1) username — логин от Instagram;
2) password — пароль от Instagram;
3) dirfile — полный путь до дирректории, где будут сохранены фотографии и откуда они будут взяты для отправки в Instagram;
4) caption — стандартная подпись для фотографий.

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```sh
pip install -r requirements.txt
```
Для реализации проекта был использован бот для отправки фотографий [Instabot](https://github.com/instagrambot) 


# Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
