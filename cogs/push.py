import discord
from discord.ext import commands
from discord import FFmpegAudio,FFmpegPCMAudio
import os


class Push(commands.Cog):
    def __init__(self,bot):
        self.bot = bot



    @commands.command(pass_context = True)
    async def join(self,ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice= await channel.connect()
            source = FFmpegPCMAudio("pushups.mp3")
            player = voice.play(source)
            await ctx.send("joined the voice channel")
        else:
            await ctx.send("you are not in the voice channel you must be in the voice channel")
    @commands.command(pass_context = True)
    async def leave(self,ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("i have left the voice channel")
        else:
            await ctx.send("i am not in the Voice channel")
    @commands.command() 
    async def ping(self,ctx):
        await ctx.send("PONG")


def setup(bot):
    bot.add_cog(Push(bot))