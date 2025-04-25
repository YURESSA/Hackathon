import os

from backend.core import db
from backend.core.models.hackathon_model import HackathonCase
from backend.core.services.utilits import save_file

def create_hackathon_case(data, file):
    """Создание нового кейса хакатона"""
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return None, {"message": "Название и описание обязательны."}, 400

    if not file:
        return None, {"message": "Файл с подробным ТЗ обязателен."}, 400

    original_filename, file_url = save_file(file)
    if not file_url:
        return None, {"message": "Неверный формат файла. Разрешены только PDF и DOCX."}, 400

    # Сохраняем кейс в базе данных с оригинальным именем файла
    new_case = HackathonCase(title=title, description=description, file_url=file_url, original_filename=original_filename)
    db.session.add(new_case)
    db.session.commit()

    return new_case, None, 201


def update_hackathon_case(case_id, data, file):
    """Обновление существующего кейса хакатона"""
    case = HackathonCase.query.get(case_id)
    if not case:
        return None, {"message": "Кейс не найден."}, 404

    title = data.get('title')
    description = data.get('description')

    if title:
        case.title = title
    if description:
        case.description = description

    if file:
        file_url = save_file(file)
        if not file_url:
            return None, {"message": "Неверный формат файла. Разрешены только PDF и DOCX."}, 400
        case.file_url = file_url

    db.session.commit()
    return case, None, 200


def delete_hackathon_case(case_id):
    """Удаление кейса хакатона и связанного файла"""
    case = HackathonCase.query.get(case_id)
    if not case:
        return {"message": "Кейс не найден."}, 404

    file_path = case.file_url

    if file_path and os.path.exists(file_path):
        try:
            os.remove(file_path)
        except Exception as e:
            return {"message": f"Кейс удалён, но не удалось удалить файл: {str(e)}"}, 500

    db.session.delete(case)
    db.session.commit()
    return {"message": "Кейс и связанный файл успешно удалены"}, 200
