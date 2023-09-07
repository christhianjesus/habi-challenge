from abc import ABCMeta, abstractmethod
from typing import List
from app.domain.property import Property


class PropertyRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all(self) -> List[Property]:
        pass
