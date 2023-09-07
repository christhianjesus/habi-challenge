from abc import ABC, abstractmethod
from typing import List
from app.domain.property import Property


class PropertyRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Property]:
        pass
