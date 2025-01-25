from .base import BaseAPIError


class YookassaBadRequest(BaseAPIError):
    """Bad request error"""
    detail = "bad_request"


class YookassaNotFound(BaseAPIError):
    """Not found error"""
    detail = "not_found"


class YookassaForbidden(BaseAPIError):
    """Forbidden error"""
    detail = "forbidden"

    