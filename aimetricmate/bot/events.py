"""Event handlers for AIMetricMate bot."""

import logging
import sys
import traceback
from typing import Optional, Type

import discord
from discord.ext import commands

logger = logging.getLogger(__name__)

async def on_ready() -> None:
    """Handle bot ready event."""
    logger.info('Bot is ready!')
    logger.info('------')

async def on_error(event: str, *args, **kwargs) -> None:
    """Handle errors in event handlers."""
    logger.error(f'Error in {event}:')
    logger.error(traceback.format_exc())

async def on_command_error(
    ctx: commands.Context,
    error: Type[commands.CommandError]
) -> None:
    """Handle command errors."""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")
        return

    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command.")
        return

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Missing required argument: {error.param.name}")
        return

    # Log unexpected errors
    logger.error('Ignoring exception in command {}:'.format(ctx.command))
    logger.error(''.join(traceback.format_exception(
        type(error), error, error.__traceback__)))
