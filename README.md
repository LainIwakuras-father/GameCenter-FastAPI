## запуск в  локалке
```bash
cd/GameCenter-FastAPI 
uv run app/main.py
проставить в файле ./app/db.py  в "genarate_schemas" значение True
```

## запуск в Docker
- 1.перейти в папку
```bash
cd /GameCenter-FastAPI 
```
- 2.запустить docker-compose.yml
```bash
docker compose up -d 
```
- 3.запустить миграции
```bash
docker-compose exec web uv run aerich upgrade
```
- 4.создать суперпользователя
```bash 
docker-compose exec web uv run app/create_superuser.py
```


## Диаграмма Базы данных
![alt text](docs/DB.jpg)

