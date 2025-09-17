import os
import aiofiles
from fastapi import UploadFile
from config.logging import app_logger as logger

async def save_upload_media(file: UploadFile):

    upload_folder = f"docs/image" #дл докер контейнера
    # Создаем директорию для картинки, если ее не
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    full_path = os.path.join(upload_folder, file.filename)
    # Сохраняем изображение
    async with aiofiles.open(full_path, mode="wb") as buffer:
        await buffer.write(file.file.read())
    logger.info(f"Uploaded file saved at {full_path}")

    return file.filename



async def delete_image(file_path: str):
    """Удаляет файл изображения"""
    if file_path and os.path.exists(file_path):
        os.remove(file_path)