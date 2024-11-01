"""Main entry point for AIMetricMate bot."""

import asyncio
import logging
import sys
from typing import Optional

from aimetricmate.bot.client import AIMetricMateBot
from aimetricmate.bot import events
from aimetricmate.utils.config import init_config, get_config

logger = logging.getLogger(__name__)

async def main() -> None:
    """Initialize and run the bot."""
    # Initialize configuration
    try:
        init_config()
        config = get_config()
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        sys.exit(1)

    # Create bot instance
    bot = AIMetricMateBot()

    # Register event handlers
    bot.event(events.on_ready)
    bot.event(events.on_error)
    bot.event(events.on_command_error)

    try:
        logger.info("Starting bot...")
        async with bot:
            await bot.start(config.discord.token)
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt")
        await bot.close()
    except Exception as e:
        logger.error(f"Error running bot: {e}")
        await bot.close()
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
