import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"
# UPLOAD_FOLDER = Path(f"uploads/images")
# UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
# Загружаем переменные окружения
load_dotenv(ENV_PATH)


from pathlib import Path

ROOT_DIR = Path(__file__).parents[2]
APP_DIR = ROOT_DIR.joinpath('app')
ENV_FILE_PATH = ROOT_DIR.joinpath('.env')


if __name__=="__main__":
    print(ROOT_DIR)
    print(APP_DIR)
    print(ENV_FILE_PATH)