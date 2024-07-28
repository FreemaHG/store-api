## Локальный запуск сервера
```
uvicorn src.main:app --reload 
```

## Сборка и запуск контейнеров
```
docker compose up -d --build
```

Фронт - https://github.com/FreemaHG/store-client.git

## Генерация ключа для подписи токенов JWT
```
openssl rand -hex 32

```

## Сделать
- Вынести секретные данные в отдельный файл .secrets


### Админка
- http://127.0.0.1:8000/admin/login - авторизация
- http://127.0.0.1:8000/admin/ - админка

### Документация
http://localhost:8000/docs/