import os
import uuid
import aiofiles
from pathlib import Path
from fastapi import  UploadFile
from config.logging import app_logger as logger


async def save_upload_media(file: UploadFile):
    upload_to = "image"  # дл докер контейнера
    # Создаем директорию для картинки, если ее не
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    #относительный путь
    relative_path = Path(upload_to) / unique_filename
    #польный путь 
    full_path = Path("static") / relative_path
    # Создаем директорию для картинки, если ее не существует
    full_path.parent.mkdir(parents=True, exist_ok=True)
    # Сохраняем изображение
    async with aiofiles.open(full_path, mode="wb") as buffer:
        await buffer.write(file.file.read())
    logger.info(f"Uploaded file saved at {full_path}")
    logger.info(f"обратится можно по адресу http://localhost:8000/{full_path.relative_to('static')}")
    return full_path.relative_to("static")


async def delete_image(file_path: str):
    """Удаляет файл изображения"""
    if file_path:
        full_path = Path("static") / file_path
        if full_path.exists():
            full_path.unlink()
            logger.info(f"Deleted file at {full_path}")
