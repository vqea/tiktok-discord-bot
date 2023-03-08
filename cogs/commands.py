import discord, aiohttp, io
from discord.ext import commands
from io import BytesIO
from modules.TiktokApi import for_you

class commands(commands.Cog):
   def __init__(self, bot):
      self.bot = bot
          

   @commands.command(help ="repost a random tiktok video")
   async def fyp(self, ctx):
       async with ctx.typing():
         fyp_videos = await for_you()
         videos = []
         for video in fyp_videos:
           videos.append(video)
         data = random.choice(videos)
         download = data["download_urls"]["no_watermark"]
         async with aiohttp.ClientSession() as session:
          async with session.get(download) as r:
            data = await r.read()
            file = discord.File(io.BytesIO(data), filename=f"{self.bot.user.name}tok.mp4")
            await ctx.reply(file=file)
            return


   @commands.command(help="repost a tiktok video", usage="[link])
   async def tiktok(self, ctx, link: str = None):
     if link == None: return await ctx.reply("i need a link to repost a video")
     try:
       async with ctx.typing():
         async with aiohttp.ClientSession() as tiktok:
           async with tiktok.get("https://tikwm.com/api?url={}".format(link)) as x:
             f = await x.json()
             video = f["data"] 
             video_bytes = video["play"] 
             requestss = requests.get(video_bytes).content
             await ctx.reply(file = discord.File(io.BytesIO(requestss), f"{self.bot.user.name}tok.mp4"), mention_author=False)
     except:
       return await ctx.reply("there was a error while reposing this video")

async def setup(bot) -> None:
    await bot.add_cog(commands(bot))   
