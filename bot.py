import discord
import asyncio
import ujson as json

def specialstart(message, tup, ind=0):
    if message.startswith(tup, ind):
        for pos, entry in enumerate(tup):
            if message.startswith(entry, ind):
                return (pos, entry)
    return False

class ChatterBot(discord.Client):
    def __init__(self):
        super().__init__()
        with open("settings.json") as data_file:
            settings = json.load(data_file)
        self.token = settings['token']
        self.separator = settings['separator']
        self.names = tuple(settings['names'])
        self.prefixes = tuple(i.lower()+self.separator for i in self.names)
        self.colors = tuple(settings['colors'])
        self.images = tuple(settings['images'])
        self.sources = tuple(settings['sources'])
        self.destinations = tuple(settings['destinations'])

    async def start(self):
        await super().start(self.token)

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        self.destinations = tuple(self.get_channel(i) for i in self.destinations)

    async def on_message(self, message):
        if not(message.author.bot) and message.channel.id in self.sources:
            chartup = specialstart(message.content.lower(), self.prefixes)
            if chartup!=False:
                ind, prefix = chartup 
                name, color, url = tuple(i[ind] for i in (self.names, self.colors, self.images))
                embed = discord.Embed(colour = color, description = message.content[len(prefix):].strip())
                #,icon_url=myself["images"][i]
                embed.set_author(name=name).set_thumbnail(url=url)
                await self.destinations[self.sources.index(message.channel.id)].send(embed = embed)

if __name__ == '__main__':
    def bot_run():
        bot = ChatterBot()
        bot.loop.run_until_complete(bot.start())
    bot_run()