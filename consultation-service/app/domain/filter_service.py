from abc import ABCMeta, abstractmethod
from typing import List, Dict
from app.domain.filter import Filter


class FilterService(metaclass=ABCMeta):
    @abstractmethod
    def make_filters(self, params: Dict[str, str]) -> List[Filter]:
        pass
