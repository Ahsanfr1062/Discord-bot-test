from discord.ext import commands
import discord
import os


intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='!',intents = intents)



@bot.event
async def on_ready():
    print("------------------------------")
    print("Bot is ready to use for hehe")
    print("------------------------------")



initial_extension = []

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        initial_extension.append(f"cogs.{filename[:-3]}")
if __name__ == "__main__":
    for extension in initial_extension:
        bot.load_extension(extension)
print("this has been execute too")

bot.run(os.environ['DISCORD_TOKEN'])