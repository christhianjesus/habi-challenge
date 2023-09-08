from abc import ABCMeta, abstractmethod
from typing import Dict, List

from app.domain.filter import Filter


class FilterService(metaclass=ABCMeta):
    @abstractmethod
    def make_filters(self, params: Dict[str, List[str]]) -> List[Filter]:
        pass
