from typing import Any, Dict, List

from app.domain.property import Property


class PropertySerializer:
    @staticmethod
    def to_dict_list(ps: List[Property]) -> List[Dict[str, Any]]:
        dict_list = []
        for p in ps:
            dict_list.append(
                {
                    "Dirección": p.address,
                    "Ciudad": p.city,
                    "Estado": p.status,
                    "Precio de venta": p.price,
                    "Descripción": p.description,
                }
            )

        return dict_list
