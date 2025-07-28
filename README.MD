# SoundHub Recommendation API

## Описание

SoundHub Recommendation API - это API, предназначенное для рекомендации пользователю новых друзей на основе его предпочтений. 
API использует алгоритм ближайших соседей для рекомендации наиболее подходящих друзей по музыкальным жанрам.

## Развертывание

### Переменные окружения

Ниже представлен пример переменных окружения сервиса. 

Важно отметить, что в качестве хоста базы данных служит название сервиса БД из конфигурации Docker Compose основного проекта. 
Для локальной разработки и тестирования используется `localhost`

```dotenv
NEIGHBOURS_DEFAULT=20

POSTGRES_HOST=<host|db_service>
POSTGRES_PORT=5432
POSTGRES_USER=<user>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<db>

KAFKA_HOST=localhost
KAFKA_PORT=9092
KAFKA_CONSUMER_GROUP=group.user.recommendation
KAFKA_REQUEST_TOPIC=request.user.recommendation
KAFKA_RESPONSE_TOPIC=response.user.recommendation
KAFKA_ERROR_TOPIC=error
```

### Запуск
Проект разворачивается с помощью Docker и автоматизируется это через Makefile. Для того чтобы просмотреть все доступные команды Makefile, введите команду `make help`.

`make up` - Собрать и запустить приложение

`make down` - Остановить приложение

`make help` - Показать все доступные команды

* [Основное API](https://github.com/Pr0gger1/soundhub-api)
* [Мобильный фронтенд](https://github.com/Pr0gger1/soundhub-app)