from typing import Any, Dict, List, Optional, Sequence, Union
from dataclasses import dataclass
from app.domain.property import Property
from app.domain.property_repository import PropertyRepository
from mysql.connector.abstracts import MySQLConnectionAbstract, MySQLCursorAbstract

from app.infrastructure.mysql_property_repository import MySQLPropertyRepository


@dataclass
class MySQLCursorMock(MySQLCursorAbstract):
    _mockedList: List[Property]

    def execute(
        self,
        operation: str,
        params: Union[Sequence[Any], Dict[str, Any]] = (),
        multi: bool = False,
    ) -> Any:
        return None

    def fetchall(self) -> Sequence[Any]:
        return self._mockedList


@dataclass
class MySQLDBMock:
    _mockedList: List[Property]

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
        return MySQLCursorMock(self._mockedList)


MySQLConnectionAbstract.register(MySQLDBMock)


def test_get_filtered_empty():
    mock = MySQLDBMock([])
    repo = MySQLPropertyRepository(mock)
    properties = repo.get_all()

    assert len(properties) == 0


def test_get_filtered_non_empty():
    p1 = Property(1, "address", "city", "status", 100, "description", "year")
    p2 = Property(2, "address", "city", "status", 100, "description", "year")
    mock = MySQLDBMock([p1, p2])
    repo = MySQLPropertyRepository(mock)
    properties = repo.get_all()

    assert len(properties) == 2
