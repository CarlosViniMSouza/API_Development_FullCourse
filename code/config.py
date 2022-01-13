from pydantic import BaseSettings


class Settings(BaseSettings):

    database_hostname: str
    database_password: str
    database_username: str
    database_name: str
    database_port: str

    access_token_expire_minutes: int
    secret_key: str
    algorithm: str

    class Config:
        env_file = ".env"

settings = Settings()