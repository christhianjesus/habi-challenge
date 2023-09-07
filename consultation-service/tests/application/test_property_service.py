from typing import List
from dataclasses import dataclass
from app.domain.property import Property
from app.domain.filter import Filter
from app.domain.property_repository import PropertyRepository
from app.application.property_service import PropertyService


@dataclass
class PropertyRepositoryMock(PropertyRepository):
    _mockedList: List[Property]

    def get_all(self) -> List[Property]:
        return self._mockedList


@dataclass
class FilterMock(Filter):
    _responsesList: List[bool]

    def apply(self) -> bool:
        return self._responsesList.pop(0)


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


def test_get_filtered_filter_all():
    p1 = Property(1, "address", "city", "status", 100, "description")
    p2 = Property(2, "address", "city", "status", 100, "description")
    mock = PropertyRepositoryMock([p1, p2])
    serv = PropertyService(mock)
    filter = FilterMock([False, False])
    properties = serv.get_filtered([filter])

    assert len(properties) == 0


def test_get_filtered_filter_none():
    p1 = Property(1, "address", "city", "status", 100, "description")
    p2 = Property(2, "address", "city", "status", 100, "description")
    mock = PropertyRepositoryMock([p1, p2])
    serv = PropertyService(mock)
    filter = FilterMock([True, True])
    properties = serv.get_filtered([filter])

    assert len(properties) == 2


def test_get_filtered_two_filters():
    p1 = Property(1, "address", "city", "status", 100, "description")
    p2 = Property(2, "address", "city", "status", 100, "description")
    mock = PropertyRepositoryMock([p1, p2])
    serv = PropertyService(mock)
    filter1 = FilterMock([True, True])
    filter2 = FilterMock([False, False])
    properties = serv.get_filtered([filter1, filter2])

    assert len(properties) == 0
