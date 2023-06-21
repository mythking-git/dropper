import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check, Context
import random

import imgdown 
import klu
     
TOKEN = 'NUH-UH'
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(intents=intents, command_prefix="!")    
    
@client.event
async def on_ready():
    print(f'\n\n{client.user} is now running\n\n')


@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    
    if message.author.id == 646937666251915264 and message.channel.id == 1115710194266157168:
        #await message.reply(content=message)
        embeds = message.embeds # return list of embeds
        for embed in embeds:
            
            item = embed.to_dict()
            info = item["description"]    
            
            info = info.split("\n")
            
            character = [a for a in info if a.startswith('Character')]
            series = [b for b in info if b.startswith('Series')]
            wishlists = [c for c in info if c.startswith('Wishlisted')][0].split(" ")
            
            await message.reply(f"{character[0]}\n{series[0]}\nWishlists · {wishlists[2]}")

    if message.content.startswith("!drop_read ") == True:
        response = imgdown.drop_read(message.content[11:])
        time_taken = round(response[1],2)
        card1 = response[0][0][0] + " - " + response[0][0][1] + " - Edition: " + response[0][0][2]
        card2 = response[0][1][0] + " - " + response[0][1][1] + " - Edition: " + response[0][1][2]
        card3 = response[0][2][0] + " - " + response[0][2][1] + " - Edition: " + response[0][2][2]
        if "" == response[0][3][0]:
            card4 = "No Fourth Card Detected"
            
            cards = 3
            
        else:
            cards = 4
        
            card4 = response[0][3][0] + " - " + response[0][3][1] + " - Edition: " + response[0][3][2]
            
        client_message = f"```Time Taken: {time_taken} seconds\n{card1}\n{card2}\n{card3}\n{card4}\n```"
        await message.reply(content=f"```Time Taken: {time_taken} seconds\n{card1}\n{card2}\n{card3}\n{card4}\n```", file=discord.File(response[2]))
        await klu.klu_reader(cards,message,response)

    """ 

    # Testing Only 
    
    guild = message.guild
    username = message.author
    user_message = str(message.content)
    channel = str(message.channel)
    
    ch = await client.fetch_channel("1115345885073772767")
    
    embedVar = discord.Embed(title=f"User: {username}", color=0xff0000)
    embedVar.add_field(name="DETAIL", value=f"Channel: #{channel} - {username.id}\n Guild: {guild} - {guild.id}", inline=True)
    embedVar.add_field(name="MESSAGE", value=f"```{user_message}```", inline=False)
    await ch.send(embed=embedVar)

    """
  
client.run(TOKEN)
