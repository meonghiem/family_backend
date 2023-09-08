from typing import Any
from fastapi import HTTPException, status




class PermissionDenied(HTTPException):
    def __init__(self,message = "Permission denied"):
        self.message = message
        self.status_code = status.HTTP_403_FORBIDDEN
        super().__init__(detail = self.message, status_code = self.status_code)

class NotFound(HTTPException):
    def __init__(self, message = "Not found"):
        self.message = message
        self.status_code = status.HTTP_404_NOT_FOUND
        super().__init__(detail = self.message, status_code = self.status_code)
        
class BadRequest(HTTPException):
    def __init__(self, message = "Bad request"):
        self.message = message
        self.status_code = status.HTTP_400_BAD_REQUEST
        super().__init__(detail = self.message, status_code = self.status_code)
        
# class NotAuthenticated(HTTPException):
#     def __init__(self, message = "Not found"):
#         self.message = message
#         self.status_code = status.HTTP_404_NOT_FOUND
#         super().__init__(detail = self.message, status_code = self.status_code)