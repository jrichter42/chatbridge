# chatbridge by jrichter

# https://discordpy.readthedocs.io/en/latest/
# https://github.com/bbernhard/signal-cli-rest-api

import logging
import argparse

from discordbot import *

logLevel = logging.DEBUG
cacheFolderPath = './chatbridge-cache'

logger = logging.getLogger('chatbridge')
logger.setLevel(logLevel)

logFileHandle = logging.FileHandler('chatbridge.log')
logFileHandle.setLevel(logLevel)
logger.addHandler(logFileHandle)

logConsoleHandler = logging.StreamHandler()
logConsoleHandler.setLevel(logLevel)
logger.addHandler(logConsoleHandler)

def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("--discordtoken", "-dt", help="discord bot token")
    args = argParser.parse_args()

    discordBotToken = ''
    if args.discordtoken:
        discordBotToken = args.discordtoken
    else:
        with open('secrets/discordtoken') as token_file:
            discordBotToken = token_file.read()
    
    discordBot = DiscordBot()
    discordBot.run(discordBotToken)
    

if __name__ == "__main__":
    main()