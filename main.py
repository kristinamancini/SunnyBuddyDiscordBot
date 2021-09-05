"""
SunnyBuddy
This is a simple discord bot that replies to commands made by the user.
Image source URL: https://flyclipart.com/sun-cartoon-free-download-clip-art-sun-cartoon-png-374817

Author: Kristina Mancini

"""

import discord
import os
import random

client = discord.Client()

#sad words list
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable",  "i'm pooped", "stressed", "stressed out", "lonely", "heartbroken", "melancholy", "low-spirited", "i am pooped"]

#encouraging words list
starter_encouragements = [
    "Cheer up friend!", "Hang in there buddy", "You are a great person / bot!", "Don't give up!", "Take a break mate", "The grass is always greener on the other side!", "It be like that sometimes, cheer up mate"
]

#quotes by famous people
#sources: https://blog.hubspot.com/sales/famous-quotes
def get_quote():
    with open("quotes.txt", "r") as file:
        line = file.read().splitlines()
        quote = random.choice(line)
    return (quote)

#get jokes from text file
#jokes source: https://www.countryliving.com/life/a27452412/best-dad-jokes/
def get_joke():
  with open("jokes.txt", "r") as file:
    jokeLine = file.read().splitlines()
    joke = random.choice(jokeLine)
  return (joke)

#get encouraging statements from text file
#quotes source: https://www.keepinspiring.me/inspirational-words-of-encouragement/
def get_encouraged():
    with open("inspire.txt", "r") as file:
        encourageLine = file.read().splitlines()
        encourage = random.choice(encourageLine)
    return (encourage)

@client.event
async def on_ready():
  #await client.change_presence(activity=discord.Streaming(name="Don't click my Stream", url=f"https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
  await client.change_presence(status=discord.Status.online, activity=discord.Game('in the sunshine | $help'))
  print('We have logged in as {0.user}'.format(client))


#different commands
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)    
    
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))
    
    if msg.startswith("$joke"):
      joke = get_joke()
      await message.channel.send(joke)

    if msg.startswith("$encourage"):
      encourage = get_encouraged()
      await message.channel.send(encourage)

    if msg.startswith("$hello"):
      await message.channel.send("Hello there!")

    if msg.startswith("$ping"):
      await message.channel.send("@everyone")

    if message.content.startswith("$help"):

          await message.channel.send("Please check your direct messages for a list of commands.")

          embedVar = discord.Embed(title="Welcome to SunnyBuddy bot!", description="See below for a list of commands.", color=0xFFFF00)
          embedVar.add_field(name="$hello", value="Gives you a greeting", inline=False)
          embedVar.add_field(name="$ping", value="Pings everyone in the server", inline=False)
          embedVar.add_field(name="$inspire", value="Gives you an inspirational quote", inline=False)
          embedVar.add_field(name="$encourage", value="Gives you some words of encouragement", inline=False)
          embedVar.add_field(name="$joke", value="Tells you a funny joke", inline=False)
          embedVar.add_field(name="$help", value="DMs you a list of commands", inline=False)
          await message.author.send(embed=embedVar)

    

client.run(os.getenv('TOKEN'))