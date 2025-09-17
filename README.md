# запуск в  локалке
```bash
cd/GameCenter-FastAPI 
uv run app/main.py
проставить в файле ./app/db.py  в "genarate_schemas" значение True
```

# запуск в Docker
```bash
cd/GameCenter-FastAPI 
docker compose up -d 
docker-compose exec web uv run aerich upgrade
```

## Диаграмма Базы данных
![alt text](docs/DB.jpg)

