__title__ = "Discord Bot"
__version__ = 0.2
__author__ = "TheBoneB"

import discord

client = discord.Client()

#login data:
mail = 'mymail@domain.com'
passw = 'password'

#startup
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    for server in client.servers:
        channel = discord.utils.find(lambda n: n.name == "general", server.channels)
        await client.send_message(channel, "Hello, @{}".format("everyone"))
    print("Said hi to the dwellers")

async def logmein():
    await client.login(mail, passw)
    
def logmeout():
    client.logout()
    
def initiate(mail, pass):
    client.run(mail, pass)

#variables:
credit = "**DisCord Bot v0.1**\nMade by *TheBoneB* using __*discord.py*__\n      *with great help from __DefaltSimon__*"
help = """\
**Help:**
!help - displays this message
!ping - ;)
!credit - displays credits
!hello - Bot says hi!
"""

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
        elif message.content.lower().startswith("!ping"):
            await client.send_message(message.channel, "**!Pong**")
        elif message.content.startswith("!help"):
            await client.send_message(message.channel, help)
        #Admin Commands:
        elif message.content.startswith("Bot.") and (" " not in message.content):
            #>Bot.command.subcommand_something
            comm = message.content.strip("Bot.").split(".")
            if comm[0] == "kill":
                await client.send_message(message.channel, "Goodbye @{}".format("everyone"))
                print("Exiting program")
                logmeout()
                client.close()
            elif comm[0] == "prefix":
                if len(comm) == 1:
                    await client.send_message(message.channel, "Prefix: " + "*work in progress*") #add prefix later
                else:
                    if comm[1] == "set-default":
                        print("Set prefix to default\n  Prefix: !")
                        #add prefixes later
                    elif comm[1][:2] == "set" and ("_" in comm[1]):
                        print("Changed prefix to: ", str(comm[1].strip("set_")))
                        #add prefixes later
                        #add settings later
            else:
                print("Unknown BOT command")
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
