from prettyconf import config
from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn = config("DATABASE_URL")


settings = Settings()
