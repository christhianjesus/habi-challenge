from typing import Any, Dict, List, Optional, Sequence, Union
from dataclasses import dataclass
from app.domain.property import Property
from app.domain.property_repository import PropertyRepository
from mysql.connector.abstracts import MySQLConnectionAbstract, MySQLCursorAbstract

from app.infrastructure.mysql_property_repository import MySQLPropertyRepository


@dataclass
class MySQLCursorMock:
    _mockedList: List[Property]
    _executed: bool = False

    def execute(
        self,
        operation: str,
        params: Union[Sequence[Any], Dict[str, Any]] = (),
        multi: bool = False,
    ) -> Any:
        self._executed = True
        return None

    def fetchall(self) -> Sequence[Any]:
        return self._mockedList


MySQLCursorAbstract.register(MySQLCursorMock)


@dataclass
class MySQLDBMock:
    _mockedCursor: MySQLCursorAbstract

    def cursor(
        self,
        buffered: Optional[bool] = None,
        raw: Optional[bool] = None,
        prepared: Optional[bool] = None,
        cursor_class: Optional[type] = None,
        dictionary: Optional[bool] = None,
        named_tuple: Optional[bool] = None,
    ) -> MySQLCursorMock:
        """Instantiates and returns a mocked cursor"""
        return self._mockedCursor


MySQLConnectionAbstract.register(MySQLDBMock)


def test_get_all_empty():
    mock = MySQLDBMock(MySQLCursorMock([]))
    repo = MySQLPropertyRepository(mock)
    properties = repo.get_all()

    assert len(properties) == 0
    assert mock._mockedCursor._executed


def test_get_all_non_empty():
    t = (1, "address", "city", "status", 100, "description", "year")

    mock = MySQLDBMock(MySQLCursorMock([t]))
    repo = MySQLPropertyRepository(mock)
    properties = repo.get_all()

    assert len(properties) == 1
    assert type(properties[0]) == Property
    assert properties[0].id == 1
    assert properties[0].address == "address"
    assert properties[0].city == "city"
    assert properties[0].status == "status"
    assert properties[0].price == 100
    assert properties[0].description == "description"
    assert properties[0].year == "year"
