from enum import Enum


class HTTPResponseCode(Enum):
    OK = 200, 'OK'
    BAD_REQUEST = 400, 'Bad Request'
    NOT_FOUND = 404, 'Not Found'
    INTERNAL_SERVER_ERROR = 500, 'Internal Server Error'

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message


PROTOCOL = 'HTTP/1.1'
