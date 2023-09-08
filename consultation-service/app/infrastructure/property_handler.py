from dataclasses import dataclass
from urllib.parse import parse_qs, urlparse

from app.domain.filter_service import FilterService
from app.domain.property_service import PropertyService
from app.infrastructure.handler import JsonHandler
from app.infrastructure.property_serializer import PropertySerializer


@dataclass
class PropertyHandler:
    """Class for handle request."""

    _service: PropertyService
    _filter_service: FilterService

    def get_filtered_properties(self, h: JsonHandler) -> None:
        # Parsea la URL para obtener los query params
        parsed_url = urlparse(h.path)
        query_params = parse_qs(parsed_url.query)

        try:
            filters = self._filter_service.make_filters(query_params)
        except NotImplementedError:
            h.send_json_response(400, {"error": "Parámetro no válido"})
            return

        try:
            properties = self._service.get_filtered(filters)
        except Exception as e:
            h.send_json_response(500, {"error": e.__str__})
            return

        properties_dict = PropertySerializer.to_dict_list(properties)

        h.send_json_response(
            200, {"quantity": len(properties_dict), "properties": properties_dict}
        )
