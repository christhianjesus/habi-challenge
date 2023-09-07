from abc import ABCMeta, abstractmethod
from typing import List
from app.domain.filter import Filter


class FilterService(metaclass=ABCMeta):
    @abstractmethod
    def make_filters(self, params: dict) -> List[Filter]:
        pass
