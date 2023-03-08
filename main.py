import discord, json
from discord.ext import commands
  
with open("config.json") as f:
   config = json.load(f)
   token = config["token"]
   token = config["prefix"]

class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix = prefix, intents=discord.Intents.all(), help_command=None)
  
    async def on_ready(self):
      await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=f"tiktok 🎄"))
      print("{} is online".format(bot.user))

    async def setup_hook(self) -> None:
      for file in os.listdir("./cogs"):
        if file.endswith(".py"):
          await self.load_extension("cogs." + file[:-3])

bot = Bot()

bot.run(token)
