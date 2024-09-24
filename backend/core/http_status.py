from enum import IntEnum


class HttpStatus(IntEnum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401  # Bad password => RFC 7235
    FORBIDDEN = 403
    NOT_FOUND = 404
    LOCKED = 423
