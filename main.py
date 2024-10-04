import discord
from discord.ext import commands
from pyexpat.errors import messages

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
Bot = commands.Bot(command_prefix='!', intents=intents)

@Bot.event
async def on_ready():
    print(f'{Bot.user} *your ready prompt here*')

@Bot.event
async def on_member_join(member):
    channel = Bot.get_channel(*your channel id here*)
    if channel:
        embed = discord.Embed(
            title=f'Welcome {member.name} *your title here*',
            description=f'*your description here* {member.mention}',
            color=discord.Color.*your color here*()
        )

        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f'member #{len(member.guild.members)}')
        await channel.send(embed=embed)

Bot.run(*your key here*)
