from abc import ABCMeta, abstractmethod
from typing import Any, Dict


class JsonHandler(metaclass=ABCMeta):
    path: str

    @abstractmethod
    def send_json_response(self, status_code: int, response_body: Dict[str, Any]):
        pass
