from abc import ABC, abstractmethod
from typing import List
from app.domain import Property, Filter


class PropertyService(ABC):
    @abstractmethod
    def getFiltered(self, filters: List[Filter]) -> List[Property]:
        pass
