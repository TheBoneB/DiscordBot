__title__ = "Discord Bot"
__version__ = 0.1
__author__ = "TheBoneB"

import discord

client = discord.Client()

#login data:
mail = 'mymail@domain.com'
passw = 'password'

#startup
async def logmein():
    await client.login(mail, passw)
    
def logmeout():
    await client.logout()
    
def initiate(mail, pass):
    client.run(mail, pass)

#variables:
credit = "**DisCord Bot v0.1**\nMade by *TheBoneB* using __*discord.py*__"

#main part:
async def delmsg(message):
    await client.delete_message(message)

@client.event
async def on_message(message):
    try:
        if message.content.startswith("!hello"):
            await client.send_message(message.channel, "Hey!")
        elif message.content.startswith("!credit"):
            await client.send_message(message.channel, credit)
            
    except discord.InvalidArgument:
        print("Error -3 : InvalidArgument")
    except discord.ClientException:
        print("Error -1 : ClientException")
    except discord.HTTPException:
        print("Error -2 : HTTPException")

@client.event
async def on_member_join(member):
    server = member.server
    await client.send_message(server, "Welcome, {}".format(member.mention))

initiate(mail, pass)
