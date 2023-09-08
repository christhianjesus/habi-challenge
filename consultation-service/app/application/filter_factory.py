from typing import List

from app.application.filters import CityFilter, StatusFilter, YearFilter
from app.domain.filter import Filter
from app.domain.filter_kind import CITY_FILTER, STATUS_FILTER, YEAR_FILTER


def create_filter_factory(filter: str, values: List[str]) -> Filter:
    if filter == YEAR_FILTER:
        return YearFilter(values)
    if filter == CITY_FILTER:
        return CityFilter(values)
    if filter == STATUS_FILTER:
        return StatusFilter(values)

    raise NotImplementedError()
