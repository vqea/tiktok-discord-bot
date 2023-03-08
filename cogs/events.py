import discord, aiohttp, io
from io import BytesIO
from discord.ext import commands

class events(commands.Cog):
    def __init__(self, bot):

  
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
      if not message.guild: return  
      if message.author.bot: return
      try:
        msg = message.content.lower()
        if msg.startswith(f"{self.bot.user.name}"):
          await message.channel.typing()
          prompt = msg.strip(f"hey {self.bot.user.name}")
          async with aiohttp.ClientSession() as tiktok:
            async with tiktok.get("https://tikwm.com/api?url={}".format(promt)) as x:
              f = await x.json()
              video = f["data"] 
              video_bytes = video["play"] 
              requestss = requests.get(video_bytes).content
              await ctx.reply(file = discord.File(io.BytesIO(requestss), f"{self.bot.user.name}tok.mp4"), mention_author=False)
      except:
        return await ctx.reply("there was a error while reposing this video")


async def setup(bot):
    await bot.add_cog(message_events(bot))
