from dataclasses import dataclass
from typing import List

from app.domain.filter import Filter
from app.domain.property import Property


@dataclass
class YearFilter(Filter):
    """Year filter"""

    _years: List[str]

    def apply(self, property: Property) -> bool:
        return property.year in self._years


@dataclass
class CityFilter(Filter):
    """City filter"""

    _cities: List[str]

    def apply(self, property: Property) -> bool:
        return property.city in self._cities


@dataclass
class StatusFilter(Filter):
    """Status filter"""

    _statuses: List[str]

    def apply(self, property: Property) -> bool:
        return property.status in self._statuses
