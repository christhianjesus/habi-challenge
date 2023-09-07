from app.domain.property import Property


def test_property():
    id = 1
    address = "address"
    city = "bogota"
    status = "pre_venta"
    price = 1000000000
    description = "description"
    year = "2023"

    p = Property(id, address, city, status, price, description, year)

    assert p.id == id
    assert p.address == address
    assert p.city == city
    assert p.status == status
    assert p.price == price
    assert p.description == description
