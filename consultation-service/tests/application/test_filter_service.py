from app.application.filter_service import FilterService


def test_filter_service_empty_dict():
    s = FilterService()
    fs = s.make_filters({})

    assert len(fs) == 0


def test_filter_service_many_params():
    s = FilterService()
    fs = s.make_filters({"year": "year", "city": "city", "status": "status"})

    assert len(fs) == 3
