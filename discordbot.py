# chatbridge by jrichter

import logging
import discord

logger = logging.getLogger('chatbridge')

"""
class SignalMessage(Message):
    def __init__(self, id, sender, target, content, attachment, reactions):
        super().__init__(id, sender, target, content, attachment, reactions)
"""


class DiscordBot(discord.Client):
    async def on_ready(self):
        logger.info('Login successful as user {0.user}'.format(self))
        #await message.channel.send('received message:\n{0}'.format(message).replace('> ', '\n') )

    async def on_message(self, message):
        logger.debug(f'received {message}')

        if message.author == super().user:
            return

        await message.channel.send('received message: {0}'.format(message.content))

        if message.content.startswith('Hello'):
            await message.channel.send('World!')
            logger.debug('sent World!')