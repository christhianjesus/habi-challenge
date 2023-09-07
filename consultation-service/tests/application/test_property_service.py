from typing import List
from app.domain.property import Property
from app.domain.property_repository import PropertyRepository
from app.application.property_service import PropertyService


class PropertyRepositoryMock(PropertyRepository):
    def get_all(self) -> List[Property]:
        return []


def test_get_filtered_empty():
    mock = PropertyRepositoryMock()
    serv = PropertyService(mock)
    properties = serv.get_filtered(None)

    assert len(properties) == 0
