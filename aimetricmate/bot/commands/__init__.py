"""Command handlers for AIMetricMate bot."""

import logging
from typing import Optional, Mapping, List

import discord
from discord.ext import commands

logger = logging.getLogger(__name__)

class CustomHelpCommand(commands.HelpCommand):
    """Custom help command implementation."""
    
    async def send_bot_help(self, mapping: Mapping[Optional[commands.Cog], List[commands.Command]]) -> None:
        """Send help for all commands."""
        embed = discord.Embed(
            title="AIMetricMate Help",
            description=self.context.bot.description,
            color=discord.Color.blue()
        )
        
        for cog, commands_list in mapping.items():
            filtered = await self.filter_commands(commands_list)
            if filtered:
                cog_name = getattr(cog, "qualified_name", "No Category")
                commands_text = "\n".join(f"`{c.name}`: {c.short_doc}" for c in filtered)
                embed.add_field(name=cog_name, value=commands_text, inline=False)
        
        await self.get_destination().send(embed=embed)

class GeneralCommands(commands.Cog):
    """General purpose commands."""

    def __init__(self, bot: commands.Bot):
        """Initialize the cog with bot instance."""
        self.bot = bot
        # Remove default help command
        self.bot.help_command = CustomHelpCommand()
        # Set the cog for the help command
        self.bot.help_command.cog = self

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context) -> None:
        """Check bot's latency.
        
        Args:
            ctx: The command context
        """
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! Latency: {latency}ms")

async def setup(bot: commands.Bot) -> None:
    """Set up the commands cog."""
    await bot.add_cog(GeneralCommands(bot))
