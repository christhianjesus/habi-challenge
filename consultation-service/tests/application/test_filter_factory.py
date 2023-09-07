from app.application.filters import YearFilter, CityFilter, StatusFilter
from app.application.filter_factory import create_filter_factory


def test_create_year_filter():
    f = create_filter_factory("year", "year")

    assert isinstance(f, YearFilter)


def test_create_city_filter():
    f = create_filter_factory("city", "city")

    assert isinstance(f, CityFilter)


def test_create_status_filter():
    f = create_filter_factory("status", "status")

    assert isinstance(f, StatusFilter)


def test_create_non_valid_filter():
    try:
        create_filter_factory("invalid", "invalid")
    except Exception as e:
        assert type(e) == NotImplementedError
    else:
        assert False
