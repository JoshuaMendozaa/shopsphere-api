from typing import List, Optional
from pydantic import BaseSettings, validator
#pydantic is used for settings management and validation.
#allows to define data models using pyton classes with type annotations.
#Used in FastAPI for request validation and settings management.
import secrets
#secrets is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, and security tokens.

class Settings(BaseSettings):
    # Application settings with default values and environment variable support
    APP_NAME: str = "ShopSphere API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"

    #Database settings
    DATABASE_URL: str
    TEST_DATABASE_URL: Optional[str] = None

    #Security settings
    SECRET_KEY: str = secrets.token_urlsafe(32)  # Generate a secure random
    ALGORITHM: str = "HS256" #Algorithm for JWT
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # 30 minutes

    #Redis settings
    #What is Redis? Redis is an open-source, in-memory data structure store, used as a database, cache, and message broker. It supports various data structures such as strings, hashes, lists, sets, and more.
    REDIS_URL: str = "redis://localhost:6379/0"
    CACHE_TTL: int = 3600  # Cache time-to-live in seconds

    #Stripe settings
    STRIPE_PUBLISHABLE_KEY: str
    STRIPE_SECRET_KEY: str
    STRIPE_WEBHOOK_SECRET: str

    #CORS settings
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]

    #Logging settings
    LOG_LEVEL: str = "info"
    LOG_FORMAT: str = "json"
    
    @validator("AllOWED_ORIGINS", pre=True)
    def assemble_allowed_origins(cls, v):
        if isinstance(v, str):
            return [i.strip() for i in v.split(",")]
        return v
    
    class Config:
        env_file = ".env"
        case_sensitive = True
    
settings = Settings()
#This will read the environment variables from a .env file if present and override the default values
