import json
from http.server import BaseHTTPRequestHandler
from typing import Any, Dict

from app.infrastructure.handler import JsonHandler
from app.infrastructure.property_handler import PropertyHandler


class RoutesHandler(BaseHTTPRequestHandler, JsonHandler):
    _properties_handler: PropertyHandler

    def send_json_response(self, status_code: int, response_body: Dict[str, Any]):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response_body).encode())

    def do_GET(self):
        if self.path.startswith("/api/v1/properties"):
            self._properties_handler.get_filtered_properties(self)
        else:
            self.send_json_response(404, {"error": "Ruta no válida"})
