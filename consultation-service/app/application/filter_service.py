from typing import List
from app.application.filter_factory import create_filter_factory
from app.domain.filter import Filter
from app.domain.filter_service import FilterService


class FilterService(FilterService):
    def make_filters(self, params: dict) -> List[Filter]:
        filters = []
        for key, value in params.items():
            filters.append(create_filter_factory(key, value))

        return filters
