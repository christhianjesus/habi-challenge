from app.domain.filter import Filter
from app.domain.filter_kind import YEAR_FILTER, CITY_FILTER, STATUS_FILTER
from app.application.filters import YearFilter, CityFilter, StatusFilter


def create_filter_factory(filter: str, value: str) -> Filter:
    if filter == YEAR_FILTER:
        return YearFilter(value)
    if filter == CITY_FILTER:
        return CityFilter(value)
    if filter == STATUS_FILTER:
        return StatusFilter(value)

    raise NotImplementedError()
