from dataclasses import dataclass

from app.domain.filter import Filter
from app.domain.property import Property


@dataclass
class YearFilter(Filter):
    """Year filter"""

    _year: str

    def apply(self, property: Property) -> bool:
        return property.year == self._year


@dataclass
class CityFilter(Filter):
    """City filter"""

    _city: str

    def apply(self, property: Property) -> bool:
        return property.city == self._city


@dataclass
class StatusFilter(Filter):
    """Status filter"""

    _status: str

    def apply(self, property: Property) -> bool:
        return property.status == self._status
