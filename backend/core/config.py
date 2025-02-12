from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    db_path: str = Field(default_factory=lambda path: f"sqlite+aiosqlite:///{path}")
