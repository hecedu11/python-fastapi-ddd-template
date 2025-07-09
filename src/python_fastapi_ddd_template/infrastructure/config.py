from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    aws_region: str = "us-east-1"
    dynamodb_table_name: str = "users"

    class Config:
        env_file = ".env"

settings = Settings()
