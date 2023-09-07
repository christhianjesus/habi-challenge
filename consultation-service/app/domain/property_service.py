from abc import ABC, abstractmethod
from typing import List
from app.domain.property import Property
from app.domain.filter import Filter


class PropertyService(ABC):
    @abstractmethod
    def get_filtered(self, filters: List[Filter]) -> List[Property]:
        pass
