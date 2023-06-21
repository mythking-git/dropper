"""
WIPWIPWPIWPIWPIWPIWPIWPI

Also not really needed as is implemented into bot.py
"""

import asyncio

async def klu_reader(cards,client,response):

    for card in range(0,cards): 
        
        await client.send(discord.Object(id='1115710194266157168'), f"k!lu {response[0][card][0]} {response[0][card][1]}\n")
        
        await asyncio.sleep(10)
        
    """
    for embed in embeds:
            
            item = embed.to_dict()
            info = item["description"]    
            
            info = info.split("\n")
            
            print(info)
            
            character = [a for a in info if a.startswith('Character')]
            series = [b for b in info if b.startswith('Series')]
            wishlists = [c for c in info if c.startswith('Wishlisted')][0].split(" ")
            
            await message.reply(f"{character[0]}\n{series[0]}\nWishlists · {wishlists[2]}")"""
