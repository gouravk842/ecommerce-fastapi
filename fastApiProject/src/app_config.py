import fastapi

from src.database import DatabaseManager


class AppConfig:
    def __init__(self, dev_mode: bool):
        self.dev_mode = dev_mode
        self.db_manager = DatabaseManager("ecommerce")
