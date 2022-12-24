import discord
from discord.ext import commands
from discord.ext.commands import *
from colorama import Fore, Style
from gtts import gTTS
import random
import datetime
import string
import asyncio
import json
import requests
import urllib
import os


class SELFBOT():
    __version__ = 1

application_id = 1048594623062351952
large_image_id = 1048596984862347294

with open("cong.json") as f:
    j = json.load(f)
    token = j["token"]
    prefix = j["prefix"]
client = commands.Bot(command_prefix=prefix, self_bot=True)
client.remove_command("help")

# Events

@client.event
async def on_ready():
	await client.change_presence(
		activity = discord.Activity(
			type=discord.ActivityType.streaming,
			application_id = application_id,
			name = "KapT Self-Bot",
            details = "KapT Self-Bot",
			assets = {
			  'large_image' : str(large_image_id),
			  'large_text':f'https://t.me/kapt_self_bot'
			},
			url = "https://twitch.tv/kapt"
			)
		)
print(Fore.GREEN + f"""
██╗░░██╗░░░░░░██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗
██║░██╔╝░░░░░░██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝
█████═╝░█████╗██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░
██╔═██╗░╚════╝██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░
██║░╚██╗░░░░░░██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░
╚═╝░░╚═╝░░░░░░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░
{Fore.GREEN}\n\nLogged In As This Random: {Fore.RED}[{Fore.BLUE}{client.user.name}#{client.user.discriminator}{Fore.RED}]{Fore.GREEN}\nYour ID is: {Fore.RED}[{Fore.BLUE}{client.user.id}{Fore.RED}]\n\n{Fore.RED}----------CREDITS MADE BY KapT----------{Fore.BLUE}\n\n{Fore.RED}{Fore.GREEN}__KapT SelfBot V{SELFBOT.__version__}, 50+ Commands\nMade By KapT.{Fore.RED}\n\n------------------------"""
          )

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        try:
            embed = discord.Embed(
                color=discord.Colour.from_rgb(255, 0, 0),
                description=
                "`Missing Permissions, You're Missing The Permissions Necessary To Use This Command`"
            )
            embed.set_author(name="Missing Permissions")
            await ctx.send(embed=embed)
        except:
            await ctx.send(
                """You're Missing Permissions To Execute This Command""")
    if isinstance(error, commands.MissingRequiredArgument):
        try:
            embed = discord.Embed(
                color=discord.Colour.from_rgb(255, 0, 0),
                description="Missing Required Argument, Try Again?")
            embed.set_author(name="Missing Required Argument")
            await ctx.send(embed=embed)
        except:
            await ctx.send("Missing Required Argument")


# Other Shit

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'ua': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de", "en-GB", "en-US", "es-ES", "fr", "hr", "it", "lt", "hu", "nl",
    "no", "pl", "pt-BR", "ro", "fi", "sv-SE", "vi", "tr", "cs", "el", "bg",
    "ru", "ua", "th", "zh-CN", "ja", "zh-TW", "ko"
]

# Help Commands


@client.command()
async def help(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at)
        embed.set_author(name="KapT 𝐒𝐞𝐥𝐟 𝐁𝐨𝐭", icon_url=ctx.author.avatar_url)
        embed.set_footer(text="KapT Self Bot")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_image(
            url=
            "https://media.tenor.co/videos/726c00ca7f375035bf2c599e6ed7d6fe/mp4"
        )
        embed.add_field(name="*♦ KapT 𝖒𝖔𝖉 *",
                        value="`Shows The Moderation Commands`",
                        inline=False)
        embed.add_field(name="*♦ KapT 𝑴𝒊𝒔𝒄𝒆𝒍𝒍𝒂𝒏𝒆𝒐𝒖𝒔 *",
                        value="`Shows The Miscellaneous Commands`",
                        inline=False)
        embed.add_field(name="*♦ KapT 𝖀𝖙𝖎𝖑𝖎𝖙𝖞*",
                        value="`Shows The Utility Commands`",
                        inline=False)
        embed.add_field(name="*♦ KapT 𝖘𝖙𝖆𝖙𝖚𝖘*",
                        value="`Shows The Status Commands`",
                        inline=False)
        embed.add_field(name="*♦ KapT 𝖓𝖚𝖐𝖊*",
                        value="`Shows The Nuke Commands`",
                        inline=False)
        embed.add_field(name="*♦ KapT 𝖕𝖊𝖗𝖘𝖔𝖓𝖆𝖑*",
                        value="`Shows The Personal Commands`",
                        inline=False)
        embed.add_field(name="*♦ KapT 𝖒𝖆𝖙𝖍*",
                        value="`Shows The Math Commands`",
                        inline=False)
        embed.add_field(name="*♦ KapT 𝖘𝖊𝖗𝖛𝖊𝖗*",
                        value="`Shows The Server Commands`",
                        inline=False)
        embed.add_field(name="*♦ KapT 𝖓𝖋𝖘𝖜*",
                        value="`Shows The NSFW Commands`",
                        inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__KapT SelfBot Help__**\n
**Moderation**
`Shows The Moderation Commands`
**Miscellaneous**
`Shows The Miscellaneous Commands`
**Utility**
`Shows The Utility Commands`
**Status**
`Shows The Status Commands`
**Nuke**
`Shows The Nuke Commands`
**Personal**
`Shows The Personal Commands`
**Math**
`Shows The Math Commands`
**Server**
`Shows The Server Commands`
**NSFW**
`Shows The NSFW Commands`""")


@client.command(aliases=["mod"])
async def moderation(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              description="*[] Is Required, <> Is Optional*",
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="KapT SelfBot")
        embed.set_author(name="𝙈𝙊𝘿𝙀𝙍𝘼𝙏𝙄𝙊𝙉", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="*♦ Ban [member]*",
                        value="`Bans The Specified Member`",
                        inline=False)
        embed.add_field(name="*♦ Kick [member]*",
                        value="`Kicks The Specified Member`",
                        inline=False)
        embed.add_field(
            name="*♦ AR [member] [role]*",
            value="`Adds The Specified Role To The Specified Member`",
            inline=False)
        embed.add_field(
            name="*♦ TR [member] [role]*",
            value="`Takes The Specified Role From The Specified Member`",
            inline=False)
        embed.add_field(name="*♦ Mute [member]*",
                        value="`Mutes The Specified Member`",
                        inline=False)
        embed.add_field(name="*♦ Purge <amount>*",
                        value="`Purges The Specified Amount Of Messages`",
                        inline=False)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/attachments/823051201192919136/831188629333344286/nbayoungman.gif"
        )
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__KapT SelfBot Moderation__**\n
*[] Is Required, <> Is Optional*
**Ban [member]**
`Bans The Specified Member`
**Kick [member]**
`Kicks The Specified Member`
**AR [member] [role]**
`Adds The Specified Role To The Specified Member`
**TR [member] [role]**
`Takes The Specified Role From The Specified Member`
**Mute [member]**
`Mutes The Specified Member`
**Purge <amount>**
`Purges The Specified Amount Of Messages`""")


@client.command()
async def status(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at,
                              description="*[] Is Required, <> Is Optional*")
        embed.set_footer(text="KapT SelfBot")
        embed.set_author(name="𝙎𝙏𝘼𝙏𝙐𝙎", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/attachments/823051201192919136/831270357763751956/rondo2.gif"
        )
        embed.add_field(name="*♦ Game*",
                        value="`Changes Your Status To A Game`",
                        inline=False)
        embed.add_field(name="*♦ Stream*",
                        value="`Changes Your Status To A Stream`",
                        inline=False)
        embed.add_field(name="*♦ Listen*",
                        value="`Changes Your Status To Listening`",
                        inline=False)
        embed.add_field(name="*♦ Watch*",
                        value="`Changes Your Status To Watching`",
                        inline=False)
        embed.add_field(name="*♦ Clear*",
                        value="`Clears Your Custom Status`",
                        inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__KapT SelfBot Status__**\n
[] Is Required, <> Is Optional*
**Game**
`Changes Your Status To A Game`
**Stream**
`Changes Your Status To A Stream`
**Listen**
`Changes Your Status To Listening`
**Watch**
`Changes Your Status To Watching`
**Clear**
`Clears Your Custom Status`""")


@client.command()
async def utility(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at,
                              description="*[] Is Required, <> Is Optional*")
        embed.set_footer(text="KapT SelfBot")
        embed.set_author(name="𝙐𝙏𝙄𝙇𝙄𝙏𝙔", icon_url=ctx.author.avatar_url)
        embed.set_image(url=ctx.author.avatar_url)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/attachments/823051201192919136/831269766232145930/quando.gif"
        )
        embed.add_field(name="*♦ AV <member>*",
                        value="`Shows The Mentioned Members Avatar`",
                        inline=False)
        embed.add_field(name="*♦ Creator*",
                        value="`Shows This SelfBots Creator`",
                        inline=False)
        embed.add_field(name="*♦ Ping*",
                        value="`Shows The Clients Latency`",
                        inline=False)
        embed.add_field(name="*♦ Info*",
                        value="`Shows Some Info About Yourself`",
                        inline=False)
        embed.add_field(name="*♦ Tts <lang> <message>*",
                        value="`Sends a Message In Text to Speech`",
                        inline=False)
        embed.add_field(
            name="*♦ 𝘿𝙪𝙢𝙥𝙚𝙢𝙤𝙟𝙞𝙨 <𝙨𝙚𝙧𝙫𝙚𝙧𝙞𝙙>*",
            value=
            "`Dumps the emojis of the specified server into the emojis file`",
            inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__KapT SelfBot Utility__**\n
*[] Is Required, <> Is Optional*
**AV <member>**
`Shows The Mentioned Users Avatar`
**Ping**
`Shows The Clients Latency`
**Info**
`Shows Some Info About Yourself`
**Tts <lang> <message>**
`Sends a Message In Text to Speech`
**Dumpemojis <serverid>**
`Sends a Message In Text to Speech`""")


@client.command(aliases=["misc"])
async def miscellaneous(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at,
                              description="*[] Is Required, <> Is Optional*")
        embed.set_footer(text="KapT SelfBot")
        embed.set_author(name="𝙈𝙄𝙎𝘾𝙀𝙇𝙇𝘼𝙉𝙀𝙇𝙊𝙐𝙎", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/attachments/823051201192919136/831269063257751633/lilbaby.gif"
        )
        embed.add_field(
            name="*♦ Hug [member] <member>*",
            value="`Sends a gif of hugging the mentioned members/member`",
            inline=False)
        embed.add_field(
            name="*♦ Kiss [member] <member>*",
            value="`Sends a gif of kissing the mentioned members/member`",
            inline=False)
        embed.add_field(name="*♦ Spam [text]*",
                        value="`Spams The Specified Text`",
                        inline=False)
        embed.add_field(name="*♦ Ascii [text]*",
                        value="`Sends The Specified Text In Ascii`",
                        inline=False)
        embed.add_field(
            name="*♦ Wizz*",
            value="`Fake Wizzes The Server, Only Meant To Scare Friends`",
            inline=False)
        embed.add_field(
            name="*♦ Dmlist [message]*",
            value="`DMs Everyone On Your DMs List The Desired Message`",
            inline=False)
        embed.add_field(
            name="*♦ Dmfriends [message]*",
            value="`DMs Everyone On Your Friends List The Desired Message`",
            inline=False)
        embed.add_field(name="*♦ Tokeninfo [token]*",
                        value="`Checks The Desired Token`",
                        inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__KapT SelfBot Miscellaneous__**\n
*[] Is Required, <> Is Optional*
**Hug [member] <member>**
`Sends a gif of hugging the mentioned members/member`
**Kiss [member] <member>**
`Sends a gif of kissing the mentioned members/member`
**Ascii [text]**
`Sends The Specified Text In Ascii`
**Wizz**
`Fake Wizzes The Server, Only Meant To Scare Friends`
**Dmlist [message]**
`DMs Everyone On Your DMs List The Desired Message`
**Dmfriends [message]**
`DMs Everyone On Your Friends List The Desired Message`
**Tokeninfo [token]**
`Checks The Desired Token`""")


@client.command()
async def nsfw(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="KapT SelfBot")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/attachments/823051201192919136/831730772250722324/giphy-downsized.gif"
        )
        embed.set_author(name="Sexy __KapT", icon_url=ctx.author.avatar_url)
        embed.add_field(name="*♦ Hentai*",
                        value="`Sends A Hentai Image`",
                        inline=False)
        embed.add_field(name="*♦ Sex*",
                        value="`Sends A Sex Image`",
                        inline=False)
        embed.add_field(name="*♦ Tits*",
                        value="`Sends A Tit Image`",
                        inline=False)
        embed.add_field(name="*♦ Pussy*",
                        value="`Sends A Pussy Image`",
                        inline=False)
        embed.add_field(name="*♦ Dick*",
                        value="`Sends A Dick Image`",
                        inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__KapT SelfBot NSFW__**\n
*[] Is Required, <> Is Optional*
**Hentai**
`Sends A Hentai Image`
**Sex**
`Sends A Sex Image`
**Tits**
`Sends A Tit Image`
**Pussy**
`Sends A Pussy Image`
**Dick**
`Sends A Dick Image`""")



@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    await ctx.send("""**__KapT SelfBot Nuke__**\n
*[] Is Required, <> Is Optional*
**Ball**
`Bans All Server Members`
**Kall**
`Kicks All Server Members`
**Schan [name]**
`Spams Channels With The Desired Name`
**Dchan**
`Deletes All Channels In The Guild`
**Drole**
`Deletes All Roles In The Guild`
**Dellall**
`Delete all channels and roles along with the massban`
**Roles**
`Prints Out All Server Roles`
**Spam [count] [text]**
`Start spamming with selected number of times and your text`
**Bypass**
`Start server crash by bypassing some anticrash bots`
**Auto**
`Start auto crash`
**Hookall**
`Start spamming webhooks to all channels`
**Spamv2**
`Start spaming in channel`""")


@client.command()
async def math(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at,
                              description="*[] Is Required, <> Is Optional*")
        embed.set_footer(text="KapT SelfBot")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/attachments/823051201192919136/831729676375949363/cartierfucker.gif"
        )
        embed.set_author(name="𝙈𝘼𝙏𝙃", icon_url=ctx.author.avatar_url)
        embed.add_field(name="*♦ Add [number] [number]*",
                        value="`Adds The Two Desired Numbers`",
                        inline=False)
        embed.add_field(name="*♦ Subtract [number] [number]*",
                        value="`Subtracts The Two Desired Numbers`",
                        inline=False)
        embed.add_field(name="*♦ Multiply [number] [number]*",
                        value="`Multiplies The Two Desired Numbers`",
                        inline=False)
        embed.add_field(name="*♦ Divide [number] [number]*",
                        value="`Divides The Two Desired Numbers`",
                        inline=False)
        embed.add_field(
            name="*♦ Calculator [numbers]*",
            value="`Calculates The Numbers and Operators\nExample: 7*2/2`")
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__KapT SelfBot Math__**\n
*[] Is Required, <> Is Optional*
**Add [number] [number]**
`Adds The Two Desired Numbers`
**Subtract [number] [number]**
`Subtracts The Two Desired Numbers`
**Multiply [number] [number]**
`Multiplies The Two Desired Numbers`
**Divide [number] [number]**
`Divided The Two Desired Numbers`
**Calculator [numbers]**
`Calculates The Numbers And Operators\nExample: 7*2/2`""")


@client.command()
async def server(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="KapT SelfBot")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/attachments/823051201192919136/831730518365437952/f9dc7f72bc9a1f039410755aca3306ed.gif"
        )
        embed.set_author(name="𝙎𝙀𝙍𝙑𝙀𝙍", icon_url=ctx.author.avatar_url)
        embed.add_field(name="*♦ Servericon*",
                        value="`Sends The Server Icon`",
                        inline=False)
        embed.add_field(name="*♦ Serverbanner*",
                        value="`Sends The Server Banner`",
                        inline=False)
        embed.add_field(name="*♦ Servername*",
                        value="`Sends The Server Name`",
                        inline=False)
        embed.add_field(name="*♦ Serverinfo*",
                        value="`Sends The Servers Info`",
                        inline=False)
        embed.add_field(name="*♦ Serverroles*",
                        value="`Sends a List of The Servers Roles`")
        embed.add_field(name="*♦ Serverchannels*",
                        value="`Sends a List of The Servers Channels`",
                        inline=False)
        embed.add_field(name="*♦ Copy*",
                        value="`Makes An Exact Copy of The Server`",
                        inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__KapT SelfBot Server__**\n
*[] Is Required, <> Is Optional*
**Servericon**
`Sends The Server Icon`
**Serverbanner**
`Sends The Server Banner`
**Servername**
`Sends The Servername`
**Serverinfo**
`Sends The Server Info`
**Serverroles**
`Sends A List Of The Server Roles`
**Serverchannels**
`Sends A List Of The Servers Channels`
**Copy**
`Makes An Exact Copy Of The Server`""")


@client.command()
async def personal(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at)
        embed.set_footer(text="KapT SelfBot")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/attachments/823051201192919136/831728923683061760/6666624671237135865-1499067990.gif"
        )
        embed.set_author(name="𝙋𝙀𝙍𝙎𝙊𝙉𝘼𝙇", icon_url=ctx.author.avatar_url)
        embed.add_field(name="*♦ Guilds*",
                        value="`Displays All The Guilds You're In`",
                        inline=False)
        embed.add_field(name="*♦ Prefix*",
                        value="`Shows The Prefix`",
                        inline=False)
        embed.add_field(name="*♦ Myroles*",
                        value="`Shows All The Roles You Have`",
                        inline=False)
        embed.add_field(name="*♦ Nick [nickname]*",
                        value="`Changes Your Nickname`",
                        inline=False)
        embed.add_field(name="*♦ Nickreset*",
                        value="`Resets Your Nickname`",
                        inline=False)
        embed.add_field(name="*♦ Friendbackup*",
                        value="`Backups your friends list in Friends.txt`",
                        inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__KapT SelfBot Personal__**\n
*[] Is Required, <> Is Optional*
**Guilds**
`Displays All The Guilds You're In`
**Prefix**
`Shows The Prefix`
**Myroles**
`Shows All The Roles You Have`
**Nick [nickname]**
`Changes Your Nickname`
**Nickreset**
`Resets Your Nickname`
**Friendbackup**
`Backups your friends list in Friends.txt`
**Reactionall [count]**
`Set a reaction to as many messages as you have indicated`
**Create_guild**
`Create a server`
**Delguild**
`Delete server`""")


# Mod


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason):
    await ctx.message.delete()
    await member.ban(reason=reason)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason):
    await ctx.message.delete()
    await member.kick(reason=reason)


@client.command()
@commands.has_permissions(manage_roles=True)
async def ar(ctx, member: discord.Member, role: discord.Role):
    await ctx.message.delete()
    await member.add_roles(role)


@client.command()
@commands.has_permissions(manage_roles=True)
async def tr(ctx, member: discord.Member, role: discord.Role):
    await ctx.message.delete()
    await member.remove_roles(role)


@client.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member):
    await ctx.message.delete()
    if isinstance(error, commands.RoleNotFound):
        await ctx.send("Muted Role Not Found!")
    else:
        role = client.get_role("Muted")
        await member.add_roles(role)


@client.command()
async def purge(ctx, amount=100):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)


# Misc


@client.command()
async def hug(ctx, member: discord.Member, user: discord.Member = None):
    await ctx.message.delete()
    try:
        user = ctx.author if not user else user
        hugg = requests.get("https://nekos.life/api/v2/img/hug")
        res = hugg.json()
        embed = discord.Embed(
            description=f"{user.mention} Hugs {member.mention}",
            color=discord.Colour.from_rgb(255, 0, 0))
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"""{user.mention} Hugs {member.mention}\n\n""" +
                       res["url"])


@client.command()
async def kiss(ctx, member: discord.Member, user: discord.Member = None):
    await ctx.message.delete()
    try:
        user = ctx.author if not user else user
        kisss = requests.get("https://nekos.life/api/v2/img/kiss")
        res = kisss.json()
        embed = discord.Embed(
            description=f"{user.mention} Kisses {member.mention}",
            color=discord.Colour.from_rgb(255, 0, 0))
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"""{user.mention} Kisses {member.mention}\n\n""" +
                       res["url"])

@client.command()
async def ascii(ctx, *, message):
    await ctx.message.delete()
    ascii = requests.get(
        f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(message)}"
    ).text
    if len("```" + ascii + "```") > 2000:
        return
    await ctx.send(f"```{ascii}```")


@client.command()
async def wizz(ctx):
    await ctx.message.delete()
    msg = await ctx.send(f"`WIZZING {ctx.guild.name}`")
    await asyncio.sleep(1)
    await msg.edit(
        content=
        f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.text_channels)} Text Channels**"
    )
    await asyncio.sleep(3)
    await msg.edit(
        content=
        f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.voice_channels)} Voice Channels**"
    )
    await asyncio.sleep(2)
    await msg.edit(
        content=
        f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.categories)} Categories**"
    )
    await asyncio.sleep(2)
    await msg.edit(
        content=
        f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.roles)} Roles**"
    )
    await asyncio.sleep(5)
    await msg.edit(
        content=f"`WIZZING {ctx.guild.name}`\n**Spamming Text Channels**")
    await asyncio.sleep(5)
    await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Webhooks**"
                   )
    await asyncio.sleep(2)
    await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Roles**")
    await asyncio.sleep(3)
    await msg.edit(
        content=f"`WIZZING {ctx.guild.name}`\n**Spamming Categories**")
    await asyncio.sleep(2)
    await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Sending Pings**")
    await asyncio.sleep(10)
    await msg.edit(
        content=
        f"`WIZZING {ctx.guild.name}`\n**Banning {len(ctx.guild.members)}**")
    await msg.edit(content=f"`WIZZED {ctx.guild.name}`")


@client.command()
async def dmlist(ctx, *, x):
    await ctx.message.delete()
    for channel in client.private_channels:
        try:
            await channel.send(x)
            print(f"DMd {channel}")
        except:
            print(f"Can't DM {channel}")
            continue


@client.command()
async def level(ctx):
    await ctx.message.delete()
    responses = [
        'Cry about it', 'We love you KapT', 'Shut the up'
    ]
    answer = random.choice(responses)
    await ctx.send(answer)
    await asyncio.sleep(5)


@client.command()
async def dmfriends(ctx, *, x):
    await ctx.message.delete()
    for friend in client.user.friends:
        try:
            await friend.send(x)
            print(f"DMd {friend.name}")
        except:
            print(f"Can't DM {friend.name}")
            continue


@client.command()
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {'Authorization': _token, 'Content-Type': 'application/json'}
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me',
                           headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(
            ((int(user_id) >> 22) + 1420070400000) /
            1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get(
                'https://canary.discordapp.com/api/v6/users/@me',
                headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(
                ((int(user_id) >> 22) + 1420070400000) /
                1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                color=0x2f3136,
                description=
                f"Name: `{res['username']}#{res['discriminator']} ` **(BOT**)\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
            )
            fields = [
                {
                    'name': 'Flags',
                    'value': res['flags']
                },
                {
                    'name': 'Local language',
                    'value': res['locale'] + f"{language}"
                },
                {
                    'name': 'Verified',
                    'value': res['verified']
                },
            ]
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'],
                                 value=field['value'],
                                 inline=False)
                    em.set_thumbnail(
                        url=
                        f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
                    )
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid token")
    em = discord.Embed(
        color=0x2f3136,
        description=
        f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`",
        timestamp=ctx.message.created_at)
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {
            'name': 'Phone',
            'value': res['phone']
        },
        {
            'name': 'Flags',
            'value': res['flags']
        },
        {
            'name': 'Local language',
            'value': res['locale'] + f"{language}"
        },
        {
            'name': 'MFA',
            'value': res['mfa_enabled']
        },
        {
            'name': 'Verified',
            'value': res['verified']
        },
        {
            'name': 'Nitro',
            'value': nitro_type
        },
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'],
                         value=field['value'],
                         inline=False)
            em.set_thumbnail(
                url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
            )
    return await ctx.send(embed=em)


# Utility


@client.command()
async def av(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0))
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"{member.avatar_url}")


@client.command()
async def ping(ctx):
    await ctx.message.delete()
    msg = await ctx.send("Pinging...")
    await asyncio.sleep(1)
    await msg.edit(content=f"🏓Pong! {round(client.latency * 1000)}ms")


@client.command()
async def info(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0))
        embed.set_author(name=f"{ctx.author}'s Info!",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="**Username:**",
                        value=client.user.name,
                        inline=False)
        embed.add_field(name="**ID:**", value=client.user.id, inline=False)
        embed.add_field(name="**Servers:**",
                        value=f"{len(client.guilds)}",
                        inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"""**__{ctx.author}'s Info!__**
      
**Username:**
`{client.user.name}`
**ID:**
`{client.user.id}`
**Servers:**
`{len(client.guilds)}`
**Avatar URL**
`{client.user.avatar_url}`""")
          
@client.command()
async def tts(ctx, lang, *, text: str):
    await ctx.message.delete()
    tts = gTTS(text, lang=lang)
    filename = f'KapT Self-Bot tts.mp3'
    tts.save(filename)
    await ctx.send(file=discord.File(fp=filename, filename=filename))
    if os.path.exists(filename):
        os.remove(filename)


@client.command()
async def dumpemojis(ctx, server_id: int = None):
    await ctx.message.delete()
    try:
        if server_id is None:
            server = ctx.guild
        else:
            server = discord.utils.get(ctx.bot.guilds, id=server_id)
        emojiNum = len(server.emojis)
        folderName = 'Emojis/' + server.name.translate(
            {ord(c): None
             for c in '/<>:"\\|?*'})
        if emojiNum > 0:
            if not os.path.exists(folderName):
                os.makedirs(folderName)
        for emoji in server.emojis:
            if emoji.animated:
                fileName = folderName + '/' + emoji.name + '.gif'
            else:
                fileName = folderName + '/' + emoji.name + '.png'
            if not os.path.exists(fileName):
                with open(fileName, 'wb') as outFile:
                    req = urllib.request.Request(
                        emoji.url, headers={'user-agent': 'Mozilla/5.0'})
                    data = urllib.request.urlopen(req).read()
                    outFile.write(data)
    except:
        pass


# Status


@client.command()
async def game(ctx):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, application_id = application_id, name='KapT Self-Bot', details=f"{x}", assets={'large_image': str(large_image_id), 'large_text': 'https://t.me/kapt_self_bot'}))

@client.command()
async def stream(ctx, *, x):
    await ctx.message.delete()
    await client.change_presence(
		activity = discord.Activity(
			type=discord.ActivityType.streaming,
			application_id = application_id,
			name = "KapT Self-Bot",
            details = f"{x}",
			assets = {
			  'large_image' : str(large_image_id),
			  'large_text':f'https://t.me/kapt_self_bot'
			},
			url = "https://twitch.tv/kapt"
			)
		)

@client.command()
async def listen(ctx):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listen, name='KapT SelfBot'))


@client.command()
async def watch(ctx):
    await ctx.message.delete()
    await client.change_presence(
       activity=discord.Activity(type=discord.ActivityType.watch, name='KapT SelfBot'))



@client.command()
async def clear(ctx):
    await ctx.message.delete()
    await client.change_presence(status=discord.Status.dnd)


# Nuke


@client.command()
async def banall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try: 
          await member.ban()
        except: pass

@client.command()
async def kall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.kick()
            print(f"{Fore.GREEN} Kicked {member}")
        except:
            print(f"{Fore.GREEN} Can't Kick {member}")
        continue


@client.command()
async def schan(ctx, *, x):
    await ctx.message.delete()
    while True:
        await ctx.guild.create_text_channel(name=x)


@client.command()
async def srole(ctx, *, x):
    await ctx.message.delete()
    while True:
        await ctx.guild.create_role(name=x)


@client.command()
async def dchan(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"Deleted {channel}")
        except:
            print(f"Can't Delete {channel}")
            continue


@client.command()
async def drole(ctx):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
            await role.delete()
            print(f"Deleted {role}")
        except:
            print(f"Can't Delete {role}")
        continue


@client.command()
async def roles(ctx):
    await ctx.message.delete()
    try:
        roles = [role for role in ctx.guild.roles[::-1]]
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at)
        embed.add_field(name="**Server Roles:**",
                        value="\n".join([role.name for role in roles]))
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__Server Roles:__**\n""" +
                       "\n".join([role.name for role in roles]))


@client.command()
async def auto(ctx):
    for a in ctx.guild.roles:
        try: await a.delete()
        except: pass
    for b in ctx.guild.channels:
        try: await b.delete()
        except: pass
    for c in ctx.guild.emojis:
        try: await c.delete()
        except: pass
    with open('crash.png', 'rb') as f:
        icon = f.read()
        try: await ctx.guild.edit(name="Crashed by KapT-SelfBot", icon=icon)
        except: pass
    for _ in range(50):
        try: await ctx.guild.create_text_channel(name="crash-by-KapT-SelfBot")
        except: pass
    for _ in range(50):
        try: await ctx.guild.create_role(name="Crashed by KapT-SelfBot")
        except: pass
    for member in ctx.guild.members:
        try: await member.ban()
        except: pass

@client.command()
async def hookall(ctx):
    member=ctx.author
    whlist=[]
    for channel in ctx.guild.text_channels:
        if member.permissions_in(channel).manage_webhooks:
            webhoks = await channel.webhooks()
            if len(webhoks) > 0:
                for webhook in webhoks:
                    whlist.append(webhook)
            else:
                webhook = await channel.create_webhook(name="Crashed by KapT-SelfBot")
                whlist.append(webhook)
    while True:
        for webhook in whlist:
            try: await webhook.send('''
@everyone @here
Crashed by KapT-SelfBot
https://github.com/KapTaBka/KapT-Self-Bot
https://t.me/kapt_self_bot
''', username = "Crashed by SelfBot-Kapt")
            except: pass

@client.command()
async def spamv2(ctx, num=100, *, text='@everyone @here Raid by KapT-SelfBot'):
	if num == 0 or text in ['']:
		await ctx.send(f'')
	else:
		for spam in range(int(num)):
			await ctx.send(f'{text}')

@client.command()
async def dellall(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass
    for members in ctx.guild.members:
        try:
            await members.ban()
        except:
            pass

@client.command()
async def bypass(ctx):
    for role in ctx.guild.roles:
        try:
            await role.edit(name="Crashed by KapT-SelfBot", permissions=discord.Permissions(permissions=8))
        except:
            pass
        else:
            pass
    for channel in ctx.guild.channels:
        try:
            await channel.edit(name=f"Crashed by KapT-SelfBot-{random.randint(1, 1000)}", topic="Crashed by KapT-SelfBot https://github.com/KapTaBka/KapT-Self-Bot")
        except:
            pass
        else:
            pass
    for chan in ctx.guild.text_channels:
        try:
            hell = await chan.create_webhook(name='Crashed by KapT-SelfBot')
        except:
            pass
    for i in range(30):
        for channels in ctx.guild.text_channels:
            hooks = await channels.webhooks()
            for hook in hooks:
                await hook.send('@everyone @here Crashed by KapT-SelfBot https://github.com/KapTaBka/KapT-Self-Bot https://t.me/kapt_self_bot')

async def sendhook(ctx, channelm):
		for i in range(100):
			hooks = await channelm.webhooks()
			for hook in hooks:
				await hook.send('@everyone @here Crash by KapT-SelfBot https://github.com/KapTaBka/KapT-Self-Bot https://t.me/kapt_self_bot!')

@client.command(pass_contex=True)
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)

# Personal

@client.command()
async def delguild(ctx):
	try:
		await ctx.guild.delete()
	except Exception as e:
		await ctx.send(f'An error occurred while deleting the server | `{e}`')

@client.command()
async def create_guild(ctx, *, nameg='Guild by KapT-SelfBot'):
	new = await client.create_guild(name=nameg)
	listc = await new.fetch_channels()
	for c in listc:
		await c.delete()
	await new.create_text_channel('made-by-kapt-selfbot'),
	await ctx.send(f'Server has been created {nameg}')

@client.command()
async def reactionall( ctx, amount: int):
	await ctx.message.delete()
	messages = await ctx.channel.history(limit=amount).flatten()
	reactioned=0
	for message in messages:
		await message.add_reaction("🐱")
		await message.add_reaction("✅")
		reactioned+=1
	await ctx.send(f"**:white_check_mark: Successfully set reactions to {reactioned} messages!**")

@client.command()
async def guilds(ctx):
    await ctx.message.delete()
    try:
        guilds = [guild for guild in client.guilds]
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at)
        embed.add_field(name="**GuildCount:**",
                        value=f"{len(client.guilds)}",
                        inline=False)
        embed.add_field(name="**Guild Names:**",
                        value="\n".join([guild.name for guild in guilds]))
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"""**GuildCount:**
{len(client.guilds)}
**Guild Names:**\n""" + "\n".join([guild.name for guild in guilds]))


@client.command()
async def prefix(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at,
                              description=j["prefix"])
        embed.set_author(name="PREFIX", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"""**__PREFIX__**\n`""" + j["prefix"] + "`")


@client.command()
async def myroles(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at)
        roles = [role for role in ctx.author.roles]
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at)
        embed.add_field(name=f"**Roles:**",
                        value=f"{len(ctx.author.roles)}",
                        inline=False)
        embed.add_field(name="**Role Names:**",
                        value="\n".join([role.name for role in roles]))
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"""**Roles:**\n`{len(ctx.author.roles)}`
**Role Names:**\n""" + "\n".join([role.name for role in roles]))


@client.command()
async def nick(ctx, *, x):
    await ctx.message.delete()
    await ctx.author.edit(nick=x)

@client.command()
async def nickreset(ctx):
    await ctx.message.delete()
    await ctx.author.edit(nick=ctx.author.name)


@client.command(aliases=['friendexport'])
async def friendbackup(ctx):
    friends = requests.get(
        'https://canary.discordapp.com/api/v8/users/@me/relationships',
        headers={
            'authorization': token,
            'user-agent': 'Mozilla/5.0'
        }).json()
    await ctx.message.delete()
    for friend in range(0, len(friends)):
        friend_id = friends[friend]['id']
        friend_name = friends[friend]['user']['username']
        friend_discriminator = friends[friend]['user']['discriminator']
        friendinfo = f'{friend_name}#{friend_discriminator} ({friend_id})'
        with open('Friends.txt', 'a+') as f:
            f.write(friendinfo + "\n")

# Math


@client.command()
async def add(ctx, number1, number2):
    x = f"{number1}+{number2}"
    await ctx.message.delete()
    try:
        embed = discord.Embed(
            color=discord.Colour.from_rgb(255, 0, 0),
            description=f"Question: {number1} + {number2}\nAnswer: {eval(x)}")
        await ctx.send(embed=embed)
    except:
        await ctx.send(
            f"""**Question:** {number1} + {number2}\n**Answer:** {eval(x)}""")


@client.command()
async def subtract(ctx, number1, number2):
    x = f"{number1} - {number2}"
    await ctx.message.delete()
    try:
        embed = discord.Embed(
            color=discord.Colour.from_rgb(255, 0, 0),
            description=f"Question: {number1} - {number2}\nAnswer: {eval(x)}")
        await ctx.send(embed=embed)
    except:
        await ctx.send(
            f"""**Question:** {number1} - {number2}\n**Answer:** {eval(x)}""")


@client.command()
async def multiply(ctx, number1, number2):
    x = f"{number1}*{number2}"
    await ctx.message.delete()
    try:
        embed = discord.Embed(
            color=discord.Colour.from_rgb(255, 0, 0),
            description=f"Question: {number1} * {number2}\nAnswer: {eval(x)}")
        await ctx.send(embed=embed)
    except:
        await ctx.send(
            f"""**Question:** {number1} * {number2}\n**Answer:** {eval(x)}""")


@client.command()
async def divide(ctx, number1, number2):
    x = f"{number1} / {number2}"
    await ctx.message.delete()
    try:
        embed = discord.Embed(
            color=discord.Colour.from_rgb(255, 0, 0),
            description=f"Question: {number1} / {number2}\nAnswer: {eval(x)}")
        await ctx.send(embed=embed)
    except:
        await ctx.send(
            f"""**Question:** {number1} / {number2}\n**Answer:** {eval(x)}""")


@client.command()
async def calculator(ctx, *, x):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              description=f"Question: {x}\nAnswer: {eval(x)}")
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"""**Question:** {x}\n**Answer:** {eval(x)}""")


# Server


@client.command()
async def servericon(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0))
        embed.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"{ctx.guild.icon_url}")


@client.command()
async def serverbanner(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0))
        embed.set_image(url=ctx.guild.banner_url)
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"{ctx.guild.banner_url}")


@client.command()
async def servername(ctx):
    await ctx.message.delete()
    await ctx.send(ctx.guild.name)


@client.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    try:
        roles = [role for role in ctx.guild.roles[::-1]]
        channels = [channel for channel in ctx.guild.channels[::-1]]
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at)
        roles = [role for role in ctx.guild.roles[::-1]]
    except:
        await ctx.send(f"""**__SERVERINFO__**
        
**Server Name:**
`{ctx.guild.name}`
**Server ID:**
`{ctx.guild.id}`
**Server Owner:**
`{ctx.guild.owner}`
**Server Roles:**
`{len(ctx.guild.roles)}`
**Server Text Channels:**
`{len(ctx.guild.text_channels)}`
**Server Voice Channels:**
`{len(ctx.guild.voice_channels)}`
**Server Categories:**
`{len(ctx.guild.categories)}`
**Boosts:**
`{ctx.guild.premium_subscription_count}`
**Members:**
`{ctx.guild.member_count}`""")


@client.command()
async def serverroles(ctx):
    await ctx.message.delete()
    try:
        roles = [role for role in ctx.guild.roles[::-1]]
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at)
        embed.add_field(name="**Server Roles:**",
                        value="\n".join([role.name for role in roles]))
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__Server Roles:__**\n""" +
                       "\n".join([role.name for role in roles]))


@client.command()
async def serverchannels(ctx):
    await ctx.message.delete()
    try:
        channels = [channel for channel in ctx.guild.channels]
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at)
        embed.add_field(name="**Server Channels:**",
                        value="\n".join([channel.name
                                         for channel in channels]))
        await ctx.send(embed=embed)
    except:
        await ctx.send("""**__Server Channels:__**\n""" +
                       "\n".join([channel.name for channel in channels]))


@client.command()
async def copy(ctx):
    await ctx.message.delete()
    await client.create_guild(f'KapTSelfbot-Copy-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'KapTSelfbot-Copy-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            for role in ctx.guild.roles:
                name = role.name
                color = role.colour
                perms = role.permissions
                await g.create_role(name=name, permissions=perms, colour=color)

# Music ( BETA )

#@client.command()
#async def play(ctx, *, query):
#    await ctx.message.delete()
#    voice = get(Exeter.voice_clients, guild=ctx.guild)
#    if voice and voice.is_connected():
#        voice.play('song.mp3')
#    else:
#        await ctx.send('You need to be a in VC to play music')

#@client.command()
#async def stop(ctx):
#    await ctx.message.delete()
#    await ctx.send("Stopped the music player!")

#@client.command()
#async def skip(ctx):
#    await ctx.message.delete()
#    await ctx.send("Skipped song!")

#@client.command()
#async def lyrics(ctx, *, args):
#    await ctx.message.delete()
#    await ctx.send("Showing lyrics for " + args)

# Nsfw


@client.command()
async def hentai(ctx):
    await ctx.message.delete()
    try:
        hentai = requests.get("https://nekos.life/api/v2/img/hentai")
        res = hentai.json()
    except:
        await ctx.send(res["url"])


@client.command()
async def sex(ctx):
    await ctx.message.delete()
    try:
        anal = requests.get("https://nekos.life/api/v2/img/anal")
        res = anal.json()
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at)
        embed.set_author(name="𝙎𝙀𝙓", icon_url=ctx.author.avatar_url)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)
    except:
        await ctx.send(res["url"])


@client.command()
async def tits(ctx):
    await ctx.message.delete()
    try:
        boobs = requests.get("https://nekos.life/api/v2/img/boobs")
        res = boobs.json()
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at)
        embed.set_author(name="𝙏𝙄𝙏𝙎", icon_url=ctx.author.avatar_url)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)
    except:
        await ctx.send(res["url"])


@client.command()
async def pussy(ctx):
    await ctx.message.delete()
    try:
        pussy = requests.get("https://nekos.life/api/v2/img/pussy")
        res = pussy.json()
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at)
        embed.set_author(name="𝙋𝙐𝙎𝙎𝙔")
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)
    except:
        await ctx.send(res["url"])


@client.command()
async def dick(ctx):
    await ctx.message.delete()
    try:
        dick = requests.get("https://nekos.life/api/v2/img/blowjob")
        res = dick.json()
        embed = discord.Embed(color=discord.Colour.from_rgb(255, 0, 0),
                              timestamp=ctx.message.created_at)
        embed.set_author(name="𝘿𝙄𝘾𝙆", icon_url=ctx.author.avatar_url)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)
    except:
        await ctx.send(res["url"])


@client.command()
async def dmall(ctx, *, msg: str):
    try:
        members = ctx.channel.members
        for member in members:
            if member is not ctx.author:
                try:
                    await member.send(f"""Send by KapT SelfBot\n {msg}""")
                except Exception:
                    pass
    except Exception:
        pass


@client.command()
async def leaveallservers(ctx):
    await ctx.message.delete()
    try:
        guilds = requests.get(
            'https://canary.discordapp.com/api/v8/users/@me/guilds',
            headers={
                'authorization': token,
                'user-agent': 'Mozilla/5.0'
            }).json()
        for guild in range(0, len(guilds)):
            guild_id = guilds[guild]['id']
            requests.delete(
                f'https://canary.discordapp.com/api/v8/users/@me/guilds/{guild_id}',
                headers={
                    'authorization': token,
                    'user-agent': 'Mozilla/5.0'
                })
    except Exception:
        pass


@client.command()
async def deleteallfriends(ctx):
    try:
        friends = requests.get(
            'https://canary.discordapp.com/api/v8/users/@me/relationships',
            headers={
                'authorization': token,
                'user-agent': 'Mozilla/5.0'
            }).json()
        for friend in range(0, len(friends)):
            friend_id = friends[friend]['id']
            requests.put(
                f'https://canary.discordapp.com/api/v8/users/@me/relationships/{friend_id}',
                json={'type': 2},
                headers={
                    'authorization': tokentonuke,
                    'user-agent': 'Mozilla/5.0'
                })
            requests.delete(
                f'https://canary.discordapp.com/api/v8/channels/{friend_id}',
                headers={
                    'authorization': token,
                    'user-agent': 'Mozilla/5.0'
                })
    except Exception:
        pass


client.run(token, bot=False)
