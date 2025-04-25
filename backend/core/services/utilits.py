import os
import uuid

from backend.core.config import Config

UPLOAD_FOLDER = Config.UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'pdf', 'docx'}


def allowed_file(filename):
    """Проверка, разрешен ли файл по его расширению"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file(file):
    """Сохранение файла на сервере"""
    if not file:
        return None

    # Получаем оригинальное имя файла и расширение
    original_filename = file.filename
    ext = original_filename.rsplit('.', 1)[-1].lower()

    # Проверяем, что расширение файла разрешено
    if ext not in ALLOWED_EXTENSIONS:
        return None
    # Генерируем уникальное имя для файла
    unique_filename = f"{uuid.uuid4().hex}.{ext}"

    # Сохраняем файл в нужную директорию
    file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
    file.save(file_path)

    # Возвращаем оригинальное имя файла для использования в базе данных
    return original_filename, unique_filename
