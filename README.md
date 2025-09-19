## запуск в  локалке
```bash
cd/GameCenter-FastAPI 
uv run app/main.py
проставить в файле ./app/db.py  в "genarate_schemas" значение True
```

## запуск в Docker
1. перейти в папку
```bash
cd /GameCenter-FastAPI 
```
2. запустить docker-compose.yml
```bash
docker compose up -d 
```
3. запустить миграции
```bash
docker-compose exec web uv run aerich upgrade
```
4. создать суперпользователя
```bash 
docker-compose exec web uv run app/create_superuser.py
```
5. создать 10 станций
```bash
docker-compose exec web uv run app/create_stations.py
```
6. создать 10 заданий 
```bash
docker-compose exec web uv run app/create_tasks.py
```
7. создать 40 кураторов  
```bash
docker-compose exec web uv run app/create_users.py
```
## Документация и Админка

- Документация http://localhost:8000/docs
- Админка http://localhost:8000/admin

## Диаграмма Базы данных
![alt text](docs/DB.jpg)

