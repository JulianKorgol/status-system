from lib.db.model import UserModel


def check_if_user_is_active(user: UserModel) -> bool:
    return user.status == 1
