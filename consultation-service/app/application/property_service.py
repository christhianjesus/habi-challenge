from typing import List
from dataclasses import dataclass
from app.domain.property import Property
from app.domain.filter import Filter
from app.domain.property_repository import PropertyRepository
from app.domain.property_service import PropertyService


@dataclass
class PropertyService(PropertyService):
    """Class for filter properties."""
    _repository: PropertyRepository

    def get_filtered(self, filters: List[Filter]) -> List[Property]:
        if filters is not None:
            return []
        return self._repository.get_all()
