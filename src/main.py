from discord.ext import commands

from color import GREEN

from player import PlayerCache

bot = commands.Bot(command_prefix="btl!")

@bot.event
async def on_ready():
	print(f"{GREEN} >> ON READY <<")

@bot.command()
async def select(ctx: commands.Context, character_name: str):
	cache = PlayerCache.instance()
	player = cache.get(ctx.guild.id)

	contains_characters = map(lambda c: c.name(), player.characters)
	
	if character_name in contains_characters:
		player.select(find_character(player.characters, selected_character))