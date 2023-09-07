from typing import List
from dataclasses import dataclass
from app.domain import Filter, Property, PropertyRepository, PropertyService


@dataclass
class PropertyService(PropertyService):
    """Class for filter properties."""
    _repository: PropertyRepository

    def getFiltered(self, filters: List[Filter]) -> List[Property]:
        pass
