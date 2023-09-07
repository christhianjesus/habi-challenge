from typing import List
from dataclasses import dataclass
from app.domain.property import Property
from app.domain.property_repository import PropertyRepository
from mysql.connector.abstracts import MySQLConnectionAbstract


@dataclass
class MySQLPropertyRepository(PropertyRepository):
    """Class for query mysql properties."""

    _db: MySQLConnectionAbstract

    def get_all(self) -> List[Property]:
        cursor = self._db.cursor()
        cursor.execute(" ")

        properties = []
        for row in cursor.fetchall():
            properties.append(Property(*row))

        return properties
