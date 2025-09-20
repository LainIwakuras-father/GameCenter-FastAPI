import uuid
import aiofiles
from pathlib import Path
from base64 import b64decode
from config.logging import app_logger as logger


# функция для конвертирования с base64 в файл
async def convert_base64_to_file(base64: str) -> tuple[bytes, str]:
    # Декодируем base64
    if "," in base64:
        # Убираем префикс data:image/...;base64,
        base64_data = base64.split(",")[1]
        if "jpeg" in base64:
            file_format = "jpg"
            # Преобразуем строку в байты перед декодированием
    file_data = b64decode(base64_data.encode("utf-8"))

    return file_data, file_format


async def save_upload_media(file: bytes, file_format: str) -> Path:
    upload_to = "image"  # дл докер контейнера
    # Создаем директорию для картинки, если ее не
    # file_extension = os.path.splitext(file.filename)[1]
    file_extension = file_format
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    # относительный путь
    relative_path = Path(upload_to) / unique_filename
    # польный путь от static
    full_path = Path("static") / relative_path
    # Создаем директорию для картинки, если ее не существует
    full_path.parent.mkdir(parents=True, exist_ok=True)
    # Сохраняем изображение
    async with aiofiles.open(full_path, mode="wb") as buffer:
        await buffer.write(file)
    logger.info(f"Uploaded file saved at {full_path}")
    logger.info(f"обратится можно по адресу http://localhost:8000/{full_path}")
    return full_path


async def delete_image(file_path: str) -> None:
    """Удаляет файл изображения"""
    if file_path:
        full_path = Path("static") / file_path
        if full_path.exists():
            full_path.unlink()
            logger.info(f"Deleted file at {full_path}")
