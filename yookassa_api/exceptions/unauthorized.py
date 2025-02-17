from .base import BaseAPIError



class YooKassaInvalidCredentials(BaseAPIError):
    """Invalid credentials error"""
    detail = "invalid_credentials"

