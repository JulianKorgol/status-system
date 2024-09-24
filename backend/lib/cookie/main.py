def cookie_set(response, key, value, max_age, sec_level: str = "default", httponly: bool = False) -> bool:
    if response is None:
        return False

    if sec_level == "default":
        response.set_cookie(key=key, value=value, max_age=max_age, httponly=httponly)
    elif sec_level == "strict":
        response.set_cookie(key=key, value=value, max_age=max_age, httponly=httponly, samesite="Strict")
    elif sec_level == "lax":
        response.set_cookie(key=key, value=value, max_age=max_age, httponly=httponly, samesite="Lax")
    else:
        return False


def cookie_delete(response, key) -> bool:
    if response is None:
        return False

    response.delete_cookie(key=key)
    return True


def cookie_get(request, key) -> str | None:
    if request is None:
        return None

    return request.cookies.get(key)
