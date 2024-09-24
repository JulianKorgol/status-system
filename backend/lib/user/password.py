from hashlib import pbkdf2_hmac


def hash_password(password: str, salt: str) -> str:
    return pbkdf2_hmac('sha512', password.encode('utf-8'), salt.encode('utf-8'), 300000).hex()


def check_user_password(password: str, salt: str, password_hash: str) -> bool:
    return password_hash == hash_password(password, salt)
