from dataclasses import dataclass
from typing import List

from app.domain.filter import Filter
from app.domain.property import Property
from app.domain.property_repository import PropertyRepository
from app.domain.property_service import PropertyService


@dataclass
class PropertyService(PropertyService):
    """Class for filter properties."""

    _repository: PropertyRepository

    def get_filtered(self, filters: List[Filter]) -> List[Property]:
        filtered = []
        for property in self._repository.get_all():
            for filter in filters:
                if not filter.apply(property):
                    break
            else:
                filtered.append(property)

        return filtered
