from abc import ABC, abstractmethod
from typing import List
from app.domain import Property


class PropertyRepository(ABC):
    @abstractmethod
    def getAll(self) -> List[Property]:
        pass
