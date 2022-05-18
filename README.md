# blog_api 

## Тестовое задание на позицию Junior Backend разрабочика.

BlogAPI это RESTful API, позволяющий создавать и редактировать посты, подписываться на тех, кто вам интересен,
а так же получать последние посты из ваших подписок на почту.
В основе проекта лежат Django и Django REST Framework.

## Особенности

- Создавайте свои посты и делитесь ими с другими.
- Авторизация происходит по токену, который необходимо обновлять каждые 24 часа.
- Вы можете подписываться на других людей, и их посты будут отображаться у вас в ленте(feed).
- Раз в сутки вам на почту приходит письмо с самыми свежими постами от авторов, на которых вы подписаны.
- Вы можете помечать посты как прочитанные и они больше не будут отображаться в вашей ленте.

## Технологии

- [Django](https://github.com/django/django) - фреймворк, который включает в себя все необходимое для быстрой разработки
  различных веб-сервисовю
- [Django REST Framework](https://www.django-rest-framework.org/) - фреймворк, расширяющий возможности Django и
  позволяющий быстро писать RESTful API для Django-проектов.
- [djoser](https://github.com/sunscrapers/djoser) - библиотека, облегчающая работу с JWT-токенами.
- [celery](https://docs.celeryq.dev/en/stable/index.html#) - Celery is a simple, flexible, and reliable distributed system
to process vast amounts of messages, while providing operations with the tools required to maintain such a system.
- [redis](https://redis.io/) - NoSQL база данных, хранящая данные в формате "ключ: значение".
- [postgresql](https://www.postgresql.org/) - СУБД с открытым исходным кодом. Одна из наиболее популярных для Python приложений.

Конечно же Blog API это ПО с открытым исходным кодом
и [публичным репозиторием](https://github.com/ValentinDevPy/blog_api)
на GitHub.

## Начало работы

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ValentinDevPy/blog_api
```

```
cd api_final_yatube
```

Запустить сборку и запуск проекта при помощи docker-compose:

```
docker-compose up
```

API будет доступен по адресу:

```sh
http://0.0.0.0:8000/api/v1/
```

При создании образа приложения, в базу данных запишутся тестовые данные, они включают в себя 100 пользователей,
1000 записей, и подписку первого пользователя на 10 других.

В файл .env для удобства вынесены некоторые переменные:

POSTS_ON_FEED_PAGE - количество постов на странице feed.
HOUR_OF_SENDING и MINUTE_OF_SENDING - указание времени, в которое должна происходить отправка писем.
NUMBER_OF_POSTS_IN_EMAIL - количество последних по времени постов, которые будут высланы человеку.
Прочитанные посты не отправляются.


## Примеры работы с API

Для начала работы с апи вам необходимо будет получить JWT-токен.
Для этого необходимо передать POST запрос с таким телом:

```
{
  "username": "admin",
  "password": "pass"
}
```
На эндпоинт:

```sh
http://0.0.0.0:8000/api/v1/jwt/create/
```

Все дальнейшие действия необходимо проделывать, передавая access JWT-токен.



Получение списка всех постов и создание нового происходит на эндпоинте:

```sh
http://0.0.0.0:8000/api/v1/posts/
```

Пример ответа при GET запросе:
```
{
{
    "count": 1000,
    "next": "http://0.0.0.0:8000/api/v1/posts/?page=2",
    "previous": null,
    "results": [
        {   
            "id": 53,
            "author": "bdobbie21",
            "header": "complexity",
            "text": "De-engineered foreground methodology",
            "pub_date": "2022-05-18T14:26:32.786782+03:00"
        },
        
        ...
        
        {
            "id": 685,
            "author": "gwrathall1j",
            "header": "Optional",
            "text": "Sharable foreground service-desk",
            "pub_date": "2022-05-18T14:26:32.778339+03:00"
        }
    ]
}

```

Получение списка постов каждого пользователя происходит на эндпоинте:

```sh
http://0.0.0.0:8000/api/v1/blog/{user_id}/
```

Пример ответа:
```
{
    "count": 9,
    "next": null,
    "previous": null,
    "results": [
        {
            "author": "admin",
            "header": "motivating",
            "text": "Public-key multi-state contingency",
            "pub_date": "2022-05-18T14:26:32.774731+03:00"
        },
        
        ...
        
        {
            "author": "admin",
            "header": "explicit",
            "text": "Assimilated real-time process improvement",
            "pub_date": "2022-05-18T14:26:32.755461+03:00"
        }
        
    ]
}
```

Для подписки на пользователя необходимо отправить POST запрос с телом:
```
{
  "author": {author_id}
}
```

На эндпоинт:

```sh
http://0.0.0.0:8000/api/v1/follow/
```
На этом же эндпоинте можно получить список всех своих подписок (метод 'GET').



Для пометки поста как прочтенного, существует отдельный эндпоинт. Необходимо отправить POST
запрос с телом:

```
{
  "post": {post_id}
}
```
На эндпоинт:

```sh
http://0.0.0.0:8000/api/v1/groups/
```



На основании подписок на пользователей генерируется лента(feed). Количество постов в этой ленте задается в
переменной окружения "POSTS_ON_FEED_PAGE". Лента доступна на эндпоите:
```sh
http://0.0.0.0:8000/api/v1/feed/
```

Пример ответа:
```
{
    "count": 87,
    "next": "http://0.0.0.0:8000/api/v1/feed/?page=2",
    "previous": null,
    "results": [
        {
            "id": 974,
            "author": "gbrodway18",
            "header": "static",
            "text": "Front-line fresh-thinking interface"
        },
        {
            "id": 948,
            "author": "anolan2b",
            "header": "mobile",
            "text": "Digitized system-worthy website"
        },
    ]
}
```

Создание, обновление и верификация токена происходит на следущих эндпоинтах:

```sh
http://127.0.0.1:8000/api/v1/jwt/create/
http://127.0.0.1:8000/api/v1/jwt/refresh/
http://127.0.0.1:8000/api/v1/jwt/verify/
```

## Лицензия

**MIT**

**Free Software, Hell Yeah!**