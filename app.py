import discord
import time

bot = discord.Client()

@bot.event
async def on_message(message):
# Put in your own channel ID here
    channel = bot.get_channel('channel-id')
    if message.author == bot.user:
        return

    else:
        if message.channel == channel:
            print(message.content)
            intMsg = int(message.content)
            intMsg +=1
# Put in the amount of delay you want before it sends a message(in seconds)
            time.sleep(16)
            await message.channel.send(str(intMsg))

# Put your api key in here
bot.run('', bot=False)
