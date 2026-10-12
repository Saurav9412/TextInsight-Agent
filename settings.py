from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # LLM configuration
    llm_model: str = Field(default="gemini-3.5-flash-lite")
    llm_temperature: float = Field(
        default = 0.0,
        ge=0.0,
        lt=2.0
    )
    llm_max_retries: int = Field(
        default=2,
        gt=0
    )
    llm_timeout_seconds: float = Field(
        default = 20.0,
        gt=0.0
    )

    gemini_api_key: SecretStr

    @field_validator("gemini_api_key")
    @classmethod
    def validate_api_key(cls, value: SecretStr) -> SecretStr:
        if not value.get_secret_value().strip():
            raise ValueError("API_KEY must not be empty!!!")
        return value
        
settings = Settings()