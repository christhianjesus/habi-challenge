import os
from dataclasses import dataclass
from http.server import HTTPServer

import mysql.connector

from app.application.filter_service import FilterService
from app.application.property_service import PropertyService
from app.infrastructure.mysql_property_repository import MySQLPropertyRepository
from app.infrastructure.property_handler import PropertyHandler
from app.infrastructure.routes_handler import RoutesHandler


@dataclass
class InitAPP:
    host: str = os.getenv("APP_HOST")
    port: int = int(os.getenv("APP_PORT"))


@dataclass
class InitMYSQL:
    host: str = os.getenv("MYSQL_HOST")
    port: str = os.getenv("MYSQL_PORT")
    user: str = os.getenv("MYSQL_USER")
    password: str = os.getenv("MYSQL_PASS")
    database: str = os.getenv("MYSQL_DB")


if __name__ == "__main__":
    # Read config
    app_config = vars(InitAPP())
    db_config = vars(InitMYSQL())

    # Initialize connections
    server = HTTPServer(tuple(app_config.values()), RoutesHandler)
    db = mysql.connector.connect(**db_config)

    # Initialize repositories
    property_repository = MySQLPropertyRepository(db)

    # Initialize services
    property_service = PropertyService(property_repository)
    filter_service = FilterService()

    # Inject Dependencies
    RoutesHandler._properties_handler = PropertyHandler(
        property_service, filter_service
    )

    # Start server
    host = app_config["host"]
    port = app_config["port"]
    print(f"Server listening on {host}:{port}")

    server.serve_forever()
