from app.application.filters import CityFilter, StatusFilter, YearFilter
from app.domain.filter import Filter
from app.domain.property import Property


def test_year_filter_apply():
    p1 = Property(1, "address", "city", "status", 100, "description", "year")
    f = YearFilter("year")

    assert issubclass(type(f), Filter)
    assert hasattr(f, "apply")
    assert f.apply(p1)


def test_city_filter_apply():
    p1 = Property(1, "address", "city", "status", 100, "description", "year")
    f = CityFilter("city")

    assert issubclass(type(f), Filter)
    assert hasattr(f, "apply")
    assert f.apply(p1)


def test_status_filter_apply():
    p1 = Property(1, "address", "city", "status", 100, "description", "year")
    f = StatusFilter("status")

    assert issubclass(type(f), Filter)
    assert hasattr(f, "apply")
    assert f.apply(p1)
