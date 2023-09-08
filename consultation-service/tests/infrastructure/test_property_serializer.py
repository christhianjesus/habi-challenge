from app.domain.property import Property
from app.infrastructure.property_serializer import PropertySerializer


def test_to_list_dict():
    p1 = Property(1, "address", "city", "status", 100, "description", "year")
    p2 = Property(2, "address", "city", "status", 100, "description", "year")
    dict_list = PropertySerializer.to_dict_list([p1, p2])

    assert len(dict_list) == 2
