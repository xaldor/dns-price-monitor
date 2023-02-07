from fastapi import HTTPException


class WebElementWasNotFound(Exception):
    pass


class InvalidUrl(HTTPException):
    pass
