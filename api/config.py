from pydantic import BaseSettings, PostgresDsn
from prettyconf import config


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn = config("DATABASE_URL")


settings = Settings()
