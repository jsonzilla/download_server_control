from typing import List, Union
from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_DESCRIPTION: str

    MONGO_URL: str
    DEFAULT_DATABASE: str

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    API_TOKEN: str
    SECRET: str
    ENABLE_ADMIN: bool

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
