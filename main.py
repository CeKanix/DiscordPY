import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

# Configuration des intents (permissions) du bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Création de l'instance du bot
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f'{bot.user} est connecté à Discord!')


@bot.command()
async def ping(ctx):
    """Commande simple pour tester si le bot répond"""
    await ctx.send(f'Pong! Latence: {round(bot.latency * 1000)}ms')


@bot.command(name="aide", aliases=["help"])
async def help_command(ctx):
    """Affiche la liste des commandes disponibles"""
    embed = discord.Embed(
        title="Liste des commandes disponibles",
        description="Voici toutes les commandes que vous pouvez utiliser:",
        color=discord.Color.blue()
    )

    for command in bot.commands:
        # Vérifie si l'utilisateur a la permission d'utiliser la commande
        if await command.can_run(ctx):
            embed.add_field(
                name=f"!{command.name}",
                value=command.help or "Pas de description disponible",
                inline=False
            )

    await ctx.send(embed=embed)


# Lancement du bot avec le token
bot.run(os.getenv('DISCORD_TOKEN'))