"""Configuration management module for AIMetricMate."""

import os
import logging
from dataclasses import dataclass
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Configure basic logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

VALID_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
VERSION = "0.1.0"

class ConfigurationError(Exception):
    """Raised when there's an error in the configuration setup."""
    pass

@dataclass
class DiscordConfig:
    """Discord bot configuration settings."""
    token: str
    guild_id: int
    command_prefix: str = "!"

    @classmethod
    def from_env(cls) -> "DiscordConfig":
        """Create a DiscordConfig instance from environment variables."""
        token = os.environ.get("DISCORD_TOKEN")
        guild_id = os.environ.get("DISCORD_GUILD_ID")
        prefix = os.environ.get("DISCORD_COMMAND_PREFIX", "!")

        if not token:
            raise ConfigurationError("DISCORD_TOKEN environment variable is required")
        if not guild_id:
            raise ConfigurationError("DISCORD_GUILD_ID environment variable is required")

        try:
            guild_id_int = int(guild_id)
        except ValueError:
            raise ConfigurationError("DISCORD_GUILD_ID must be a valid integer")

        return cls(token=token, guild_id=guild_id_int, command_prefix=prefix)

@dataclass
class EnvironmentConfig:
    """Environment-specific configuration settings."""
    is_production: bool
    debug_mode: bool
    log_level: str

    @classmethod
    def from_env(cls) -> "EnvironmentConfig":
        """Create an EnvironmentConfig instance from environment variables."""
        env = os.environ.get("ENVIRONMENT", "development")
        debug = os.environ.get("DEBUG", "false").lower() == "true"
        log_level = os.environ.get("LOG_LEVEL", "INFO").upper()

        if log_level not in VALID_LOG_LEVELS:
            raise ConfigurationError(f"Invalid LOG_LEVEL '{log_level}'. Must be one of {VALID_LOG_LEVELS}")

        return cls(
            is_production=env.lower() == "production",
            debug_mode=debug,
            log_level=log_level,
        )

@dataclass
class AppConfig:
    """Main application configuration container."""
    discord: DiscordConfig
    environment: EnvironmentConfig
    version: str

    @classmethod
    def load_config(cls, env_file: Optional[str] = None) -> "AppConfig":
        """Load and validate all configuration settings."""
        if env_file:
            logger.debug(f"Loading environment from file: {env_file}")
            if not load_dotenv(env_file):
                raise ConfigurationError(f"Failed to load environment file: {env_file}")
        else:
            logger.debug("Loading environment from default .env file")
            load_dotenv(override=True)

        return cls(
            discord=DiscordConfig.from_env(),
            environment=EnvironmentConfig.from_env(),
            version=VERSION,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert config to dict, hiding sensitive values."""
        return {
            "version": self.version,
            "discord": {
                "guild_id": self.discord.guild_id,
                "prefix": self.discord.command_prefix
            },
            "environment": {
                "is_production": self.environment.is_production,
                "debug_mode": self.environment.debug_mode,
                "log_level": self.environment.log_level
            }
        }

# Global config instance
config: Optional[AppConfig] = None

def init_config(env_file: Optional[str] = None) -> AppConfig:
    """Initialize the global configuration."""
    global config
    config = AppConfig.load_config(env_file)
    return config

def get_config() -> AppConfig:
    """Get the global configuration instance."""
    if config is None:
        raise ConfigurationError(
            "Configuration not initialized. Call init_config() first."
        )
    return config
