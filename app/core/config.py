from pathlib import Path
from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):

    url: str

    port: int

    name: str

    echo: bool

    user: str

    password: str

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",
        env_prefix="DB_",
    )


class CacheSettings(BaseSettings):

    url: str
    
    host: str

    port: int

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",
        env_prefix="CACHE_",
    )


class TaskSettings(BaseSettings):

    broker_url: str

    backend_url: str

    timezone: str
    
    beat_interval: int

    worker_pool: str

    worker_concurrency: int

    accept_content: str

    serializer: str

    result_serializer: str

    create_missing_queues: bool

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",
        env_prefix="TASK_",
    )


class BrokerSettings(BaseSettings):

    host: str

    port: int

    user: str

    password: int

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",
        env_prefix="BROKER_",
    )


class JWTSettings(BaseSettings):
    """Определяет настройки JWT, которые считываются из .env файла"""

    private_key: Path

    public_key: Path

    algorithm: str

    token_type: str

    access_token_expire: int

    refresh_token_expire: int

    access_name: str

    refresh_name: str

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",
        env_prefix="JWT_",
    )


class AISetting(BaseSettings):

    gemini_api_key: str

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",
        env_prefix="AI_",
    )



ai_settings = AISetting()

db_settings = DBSettings()

jwt_settings = JWTSettings()

task_settings = TaskSettings()

cahe_settings = CacheSettings()

broker_settings = BrokerSettings()



