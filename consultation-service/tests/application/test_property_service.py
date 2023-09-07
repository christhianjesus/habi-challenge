from typing import List
from dataclasses import dataclass
from app.domain.property import Property
from app.domain.property_repository import PropertyRepository
from app.application.property_service import PropertyService


@dataclass
class PropertyRepositoryMock(PropertyRepository):
    l: List[Property]

    def get_all(self) -> List[Property]:
        return []


def test_get_filtered_empty():
    mock = PropertyRepositoryMock([])
    serv = PropertyService(mock)
    properties = serv.get_filtered(None)

    assert len(properties) == 0


def test_get_filtered_non_empty():
    p = Property(1, "address", "city", "status", 100, "description")
    mock = PropertyRepositoryMock([p])
    serv = PropertyService(mock)
    properties = serv.get_filtered(None)

    assert len(properties) == 1
