from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):

    url: str

    cache_url: str

    broker_url: str

    backend_url: str

    echo: bool

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",
        env_prefix="DB_",
    )

db_settings = DBSettings()
