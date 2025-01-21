from .base import BaseAPIError



class YookassaInvalidCredentials(BaseAPIError):
    """Invalid credentials error"""
    detail = "invalid_credentials"

