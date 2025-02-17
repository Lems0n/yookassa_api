from .base import BaseAPIError


class YooKassaBadRequest(BaseAPIError):
    """Bad request error"""
    detail = "bad_request"


class YooKassaNotFound(BaseAPIError):
    """Not found error"""
    detail = "not_found"


class YooKassaForbidden(BaseAPIError):
    """Forbidden error"""
    detail = "forbidden"

    