from dataclasses import dataclass, field
from typing import Any, Dict, List

from app.application.filters import CityFilter, StatusFilter, YearFilter
from app.domain.filter import Filter
from app.domain.filter_service import FilterService
from app.domain.property import Property
from app.domain.property_service import PropertyService
from app.infrastructure.handler import JsonHandler
from app.infrastructure.property_handler import PropertyHandler


@dataclass
class PropertyServiceMock(PropertyService):
    _properties: List[Property]
    _error: bool = False
    _filters: List[Filter] = field(default_factory=list)

    def get_filtered(self, filters: List[Filter]) -> List[Property]:
        self._filters = filters
        if self._error:
            raise Exception()
        return self._properties


@dataclass
class FilterServiceMock(FilterService):
    _filters: List[Filter]
    _error: bool = False
    _params: Dict[str, List[str]] = field(default_factory=dict)

    def make_filters(self, params: Dict[str, List[str]]) -> List[Filter]:
        self._params = params
        if self._error:
            raise NotImplementedError()
        return self._filters


@dataclass
class JsonHandlerMock(JsonHandler):
    path: str
    _executed: bool = False
    _code: int = 0
    _response: Dict[str, Any] = field(default_factory=dict)

    def send_json_response(self, status_code: int, response_body: Dict[str, Any]):
        self._executed = True
        self._code = status_code
        self._response = response_body


def test_get_filtered_properties_empty():
    property_mock = PropertyServiceMock([])
    filter_mock = FilterServiceMock([])
    json_mock = JsonHandlerMock("")

    h = PropertyHandler(property_mock, filter_mock)
    h.get_filtered_properties(json_mock)

    assert len(filter_mock._params) == 0
    assert len(property_mock._filters) == 0
    assert json_mock._executed
    assert json_mock._code == 200
    assert json_mock._response["quantity"] == 0


def test_get_filtered_properties_not_implemented_error():
    property_mock = PropertyServiceMock([])
    filter_mock = FilterServiceMock([], True)
    json_mock = JsonHandlerMock("")

    h = PropertyHandler(property_mock, filter_mock)
    h.get_filtered_properties(json_mock)

    assert len(filter_mock._params) == 0
    assert len(property_mock._filters) == 0
    assert json_mock._executed
    assert json_mock._code == 400
    assert json_mock._response["error"] is not None


def test_get_filtered_properties_exception_error():
    property_mock = PropertyServiceMock([], True)
    filter_mock = FilterServiceMock([])
    json_mock = JsonHandlerMock("")

    h = PropertyHandler(property_mock, filter_mock)
    h.get_filtered_properties(json_mock)

    assert len(filter_mock._params) == 0
    assert len(property_mock._filters) == 0
    assert json_mock._executed
    assert json_mock._code == 500
    assert json_mock._response["error"] is not None


def test_get_filtered_properties_full():
    p1 = Property(1, "address", "city", "status", 100, "description", "year")
    p2 = Property(2, "address", "city", "status", 100, "description", "year")
    property_mock = PropertyServiceMock([p1, p2])
    filter_mock = FilterServiceMock(
        [StatusFilter(["pre_venta"]), CityFilter(["bogota"]), YearFilter(["2023"])]
    )
    json_mock = JsonHandlerMock(
        "http://localhost:8080/api/v1/properties?status=pre_venta&city=bogota&year=2023"
    )

    h = PropertyHandler(property_mock, filter_mock)
    h.get_filtered_properties(json_mock)

    assert len(filter_mock._params) == 3
    assert len(property_mock._filters) == 3
    assert json_mock._executed
    assert json_mock._code == 200
    assert json_mock._response["quantity"] == 2
