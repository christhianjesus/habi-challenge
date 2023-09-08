from abc import ABCMeta, abstractmethod

from app.domain.property import Property


class Filter(metaclass=ABCMeta):
    @abstractmethod
    def apply(self, property: Property) -> bool:
        pass
