from http import HTTPStatus

from flask_jwt_extended import get_jwt_identity

from backend.core.messages import AuthMessages
from backend.core.services.auth_service import *


def parse_user_data(data, default_role):
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    full_name = data.get("full_name")
    phone = data.get("phone")
    role_name = data.get("role_name", default_role)
    return username, email, password, full_name, phone, role_name


def register_user(data):
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    full_name = data.get("full_name")
    phone = data.get("phone")
    university = data.get("university")
    study_info = data.get("study_info")
    system_role_name = data.get("role_name", "user")
    project_role = data.get("project_role", None)

    new_user = create_user(
        username=username,
        email=email,
        password=password,
        full_name=full_name,
        phone=phone,
        university=university,
        study_info=study_info,
        system_role_name=system_role_name,
        project_role=project_role
    )

    if new_user:
        return {"message": "Пользователь успешно зарегистрирован."}, HTTPStatus.CREATED
    else:
        return {
            "message": "Пользователь с таким email или username уже существует, либо роль некорректна."}, HTTPStatus.BAD_REQUEST


def login_user(role, data):
    username = data.get("username")
    password = data.get("password")
    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password) or (
            user.system_role and user.system_role.role_name.lower() != role.lower()):
        return None
    return authenticate_user(username, password)


def get_profile():
    current_username = get_jwt_identity()
    user = User.query.filter_by(username=current_username).first()
    if not user:
        return None, {"message": AuthMessages.USER_NOT_FOUND}, HTTPStatus.NOT_FOUND
    return user, None, None


def update_user_profile(user, data):
    user.username = data.get("username", user.username)
    user.full_name = data.get("full_name", user.full_name)
    user.university = data.get("university", user.university)
    user.study_info = data.get("study_info", user.study_info)
    user.email = data.get("email", user.email)
    user.phone = data.get("phone", user.phone)

    # Обновление пароля, если он передан
    new_password = data.get("password")
    if new_password:
        user.set_password(new_password)

    db.session.commit()
    return {"message": "Профиль успешно обновлен."}


def change_profile_password(data):
    current_username = get_jwt_identity()
    if change_password(current_username, data.get("old_password"), data.get("new_password")):
        return {"message": AuthMessages.PASSWORD_CHANGED}, HTTPStatus.OK
    return {"message": AuthMessages.PASSWORD_INVALID_OLD}, HTTPStatus.BAD_REQUEST


def delete_profile():
    current_username = get_jwt_identity()
    if delete_user(current_username):
        return {"message": AuthMessages.USER_DELETED_SELF}, HTTPStatus.OK
    return {"message": AuthMessages.USER_NOT_FOUND}, HTTPStatus.NOT_FOUND


def get_user_info_response(user):
    if not user:
        return {"message": AuthMessages.USER_NOT_FOUND}, HTTPStatus.NOT_FOUND
    return user.to_dict(), HTTPStatus.OK
