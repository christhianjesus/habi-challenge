from dataclasses import dataclass
from typing import List

from mysql.connector.abstracts import MySQLConnectionAbstract

from app.domain.property import Property
from app.domain.property_repository import PropertyRepository


@dataclass
class MySQLPropertyRepository(PropertyRepository):
    """Class for query mysql properties."""

    _db: MySQLConnectionAbstract

    def get_all(self) -> List[Property]:
        cursor = self._db.cursor()
        cursor.execute(
            """
                SELECT p.id, p.address, p.city, s.name, p.price, p.description, p.`year`
                FROM property p
                LEFT JOIN (
                    SELECT property_id, status_id, MAX(update_date)
                    FROM status_history
                    GROUP BY property_id
                ) cs ON p.id = cs.property_id
                LEFT JOIN status s ON cs.status_id = s.id
                WHERE p.address <> '' AND p.city <> ''
        """
        )

        properties = []
        for row in cursor.fetchall():
            description = row[5] if row[5] is not None else ""
            year = str(row[6]) if row[6] is not None else None
            new_row = row[:5] + (description, year)
            properties.append(Property(*new_row))

        return properties
