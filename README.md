## Запуск сервера
```
uvicorn src.main:app --reload 
```

## Сборка контейнеров
```
docker compose up -d
```

## Генерация ключа для подписи токенов JWT
```
openssl rand -hex 32

```

## Сделать
- Вынести секретные данные в отдельный файл .secrets
