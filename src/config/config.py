from pathlib import Path
import os
from dotenv import load_dotenv
from dataclasses import dataclass, field

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

@dataclass
class Config:
    SECRET_KEY: str = field(default=os.getenv('SECRET_KEY', 'ureader_secret_key'))
    DATABASE_URL: str = field(default=os.getenv('DATABASE_URL', ''))

    def __post_init__(self):
        if not self.SECRET_KEY:
            raise ValueError("SECRET_KEY must be set.")
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL must be set.")

    @staticmethod
    def init_app(app: Any) -> None:
        app.state.secret_key = os.getenv('SECRET_KEY', '')
        app.state.database_url = os.getenv('DATABASE_URL', '')