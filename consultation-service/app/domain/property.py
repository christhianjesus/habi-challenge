from dataclasses import dataclass


@dataclass
class Property:
    """Class for keeping track of an available property."""
    _id: int
    _address: str
    _city: str
    _status: str
    _price: int
    _description: str

    @property
    def id(self) -> int:
        return self._id

    @property
    def address(self) -> str:
        return self._address

    @property
    def city(self) -> str:
        return self._city

    @property
    def status(self) -> str:
        return self._status

    @property
    def price(self) -> int:
        return self._price

    @property
    def description(self) -> str:
        return self._description
