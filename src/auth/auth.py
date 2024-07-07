from abc import ABC, abstractmethod
from typing import Dict, Union
from datetime import datetime


class JWTInterface(ABC):
    @abstractmethod
    def create_access_token(self, data: Dict[str, Union[str, int]]) -> str:
        pass

    @abstractmethod
    def create_refresh_token(self, data: Dict[str, Union[str, int]]) -> str:
        pass

    @abstractmethod
    def decode_access_token(self, token: str) -> Dict[str, Union[str, int]]:
        pass

    @abstractmethod
    def get_token_expiry(self, token: str) -> datetime:
        pass
