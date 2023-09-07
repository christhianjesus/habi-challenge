from app.domain.property import Property


def test_property():
    id = 1
    address = "address"
    city = "bogota"
    status = "pre_venta"
    price = 1000000000
    description = "description"

    p = Property(id, address, city, status, price, description)

    assert p.id == id
    assert p.address == address
    assert p.city == city
    assert p.status == status
    assert p.price == price
    assert p.description == description
