"""Discord bot client module for AIMetricMate."""

import logging
from typing import Optional

import discord
from discord.ext import commands

from aimetricmate.utils.config import get_config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AIMetricMateBot(commands.Bot):
    """Main bot class for AIMetricMate."""

    def __init__(self) -> None:
        """Initialize the bot with required intents and command prefix."""
        intents = discord.Intents.default()
        intents.message_content = True
        
        config = get_config()
        
        super().__init__(
            command_prefix=commands.when_mentioned_or(config.discord.command_prefix),
            intents=intents,
            description="A Discord bot for tracking AI development metrics"
        )
        
        self.logger = logger

    async def setup_hook(self) -> None:
        """Initialize bot components after login."""
        self.logger.info("Setting up bot components...")
        
        # Load extensions/cogs here in the future
        await self.load_extension("aimetricmate.bot.commands")
        
        self.logger.info("Bot setup complete!")

    async def close(self) -> None:
        """Clean up bot resources before shutdown."""
        self.logger.info("Shutting down bot...")
        await super().close()
