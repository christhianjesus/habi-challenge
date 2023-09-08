from app.application.filter_factory import create_filter_factory
from app.application.filters import CityFilter, StatusFilter, YearFilter


def test_create_year_filter():
    f = create_filter_factory("year", [])

    assert isinstance(f, YearFilter)


def test_create_city_filter():
    f = create_filter_factory("city", [])

    assert isinstance(f, CityFilter)


def test_create_status_filter():
    f = create_filter_factory("status", [])

    assert isinstance(f, StatusFilter)


def test_create_non_valid_filter():
    try:
        create_filter_factory("invalid", [])
    except Exception as e:
        assert type(e) == NotImplementedError
    else:
        assert False
