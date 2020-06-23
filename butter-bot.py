#!/usr/bin/env python3
import os
from discord.ext.commands import Bot
from dotenv import load_dotenv

def main(args):
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')

    bot = Bot(command_prefix='!')

    @bot.command(name='butter', help='Pass the butter')
    async def butter(ctx):
        await ctx.send(':butter:')

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')

    bot.run(token)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])