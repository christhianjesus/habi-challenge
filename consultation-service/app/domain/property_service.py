from abc import ABCMeta, abstractmethod
from typing import List

from app.domain.filter import Filter
from app.domain.property import Property


class PropertyService(metaclass=ABCMeta):
    @abstractmethod
    def get_filtered(self, filters: List[Filter]) -> List[Property]:
        pass
