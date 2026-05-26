from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000

    database_url: str = "postgresql://postgres:password@localhost:5432/evercrafted"
    anthropic_api_key: str = ""
    jwt_secret: str = "changeme"


settings = Settings()
