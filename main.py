# chatbridge by jrichter

# https://discordpy.readthedocs.io/en/latest/
# https://github.com/bbernhard/signal-cli-rest-api

import argparse
import discord

cacheFolderPath = './chatbridge-cache'

client = discord.Client()

@client.event
async def on_ready():
    print('Login successful as user {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send('World!')

def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("--discordtoken", "-dt", help="discord bot token")
    args = argParser.parse_args()

    discordBotToken = ''
    if args.discordtoken:
        discordBotToken = args.discordtoken
    
    client.run(discordBotToken)

if __name__ == "__main__":
    main()