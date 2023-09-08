from dataclasses import dataclass
from typing import List

from app.domain.filter import Filter
from app.domain.property import Property
from app.domain.property_repository import PropertyRepository
from app.domain.property_service import PropertyService
from app.domain.status_kind import ON_SALE_STATUS, PRESALE_STATUS, SOLD_STATUS

_VALID_STATUSES = (PRESALE_STATUS, ON_SALE_STATUS, SOLD_STATUS)


@dataclass
class PropertyService(PropertyService):
    """Class for filter properties."""

    _repository: PropertyRepository

    def get_filtered(self, filters: List[Filter]) -> List[Property]:
        filtered = []
        for property in self._repository.get_all():
            if property.status not in _VALID_STATUSES:
                continue
            for filter in filters:
                if not filter.apply(property):
                    break
            else:
                filtered.append(property)

        return filtered
