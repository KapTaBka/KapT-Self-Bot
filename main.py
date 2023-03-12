import discord
from discord.ext import commands
from discord.ext.commands import *
from colorama import Fore, Style
from gtts import gTTS
import threading
from asyncio import create_task
from threading import Thread, Lock
import random
import datetime
import string
import asyncio
import json
import requests
import urllib
import time
import os
import requests as rq
from prettytable import PrettyTable

class SELFBOT():
    __version__ = 1.1

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
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                                           |
|  ██╗░░██╗░░░░░░██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗  |
|  ██║░██╔╝░░░░░░██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝  |
|  █████═╝░█████╗██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░  |
|  ██╔═██╗░╚════╝██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░  |
|  ██║░╚██╗░░░░░░██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░  |
|  ╚═╝░░╚═╝░░░░░░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░  |
|                                                                           |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                       https://t.me/kapt_self_bot                          |
|                            𝘽𝙮 𝙆𝙖𝙥𝙏                                       | 
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                           {Fore.RED}PREFIX: {prefix}{Fore.GREEN}                                  |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|""")




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
""")


@client.command(aliases=["mod"])
async def moderation(ctx):
    await ctx.message.delete()
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
**Deletedms**
`Deletes all dms with people who have the word "spam" in their nickname`
""")




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
**Anticrash**
`Start server crash by bypassing some anticrash bots`
**Auto**
`Start auto crash`
**Hookall**
`Start spamming webhooks to all channels`
**Bypass_spam [count] [text]**
`Start server raid by bypassing some antiflood bots`
**Spamall [count] [text]**
`Start server raid by bypassing some antiflood bots (in all channels)`
**Fastauto**
`Start fast crash`
**Threadspam [count]**
`Spam thread in the channel`
**Massreport [user] [count]**
`Mass reports per user and server` 
""")


@client.command()
async def math(ctx):
    await ctx.message.delete()
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
`Makes An Exact Copy Of The Server`
**Leave**
`Command for the server leaving`
**Invite [invite]**
`Command for information about the invite`
**Clonechannel**
`Command for cloning channel`""")


@client.command()
async def personal(ctx):
    await ctx.message.delete()
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
async def purge(ctx, amount: int):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)


# Misc


@client.command()
async def hug(ctx, member: discord.Member, user: discord.Member = None):
    await ctx.message.delete()
    user = ctx.author if not user else user
    hugg = requests.get("https://nekos.life/api/v2/img/hug")
    res = hugg.json()
    await ctx.send(f"""{user.mention} Hugs {member.mention}\n\n""" +
                       res["url"])


@client.command()
async def kiss(ctx, member: discord.Member, user: discord.Member = None):
    await ctx.message.delete()
    user = ctx.author if not user else user
    kisss = requests.get("https://nekos.life/api/v2/img/kiss")
    res = kisss.json()
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
async def deletedms(ctx, name='spam'):
	await ctx.message.delete()
	removed=0
	for dm in client.private_channels:
		if name.lower() in str(dm).lower():
			while True:
				response=requests.delete(f"https://discord.com/api/v9/channels/{dm.id}", headers={'authorization': token})
				if response!=401: break
				sleep(response.json()['retry_after'])
			removed+=1
	await ctx.send(f"**Successfully removed {removed} dms!**")

# Utility


@client.command()
async def av(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    await ctx.message.delete()
    ctx.send(f"{member.avatar_url}")


@client.command()
async def ping(ctx):
    await ctx.message.delete()
    msg = await ctx.send("Pinging...")
    await asyncio.sleep(1)
    await msg.edit(content=f"🏓Pong! {round(client.latency * 1000)}ms")


@client.command()
async def info(ctx):
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
async def massreport(ctx, count = 10, member: discord.Member = None):
    if member: pass
    elif ctx.message.reference:
        try: 
            async for message in ctx.history():
                if message.id == ctx.message.reference.message_id:
                    member = await ctx.guild.fetch_member(message.author)
                    break
        except: return await ctx.message.edit(content = "Failed to get target user.")
    else: return await ctx.message.edit(content = "Target user not specified! Reply to a message sent by the target user or provide it as a command argument (Usage: `.massreport [number] [@user]`).")
    await ctx.message.edit(content = f"Mass report {member.mention} started. Please wait...")
    start_time1 = round(time.time())
    start_time1_fmt = datetime.datetime.fromtimestamp(start_time1).strftime("%Y/%m/%d %H:%M:%S.%f")
    tokens_array = open("tokens.txt", "r").read().split("\n")
    log_table = PrettyTable(["№ report", "Report time", "Token number", "Reason", "Report status", "Channel ID", "Message ID"])
    log_table.sortby = "№ report"
    log_table.align = 'l'
    log_text = f'''**__Mass Reporter by KapT Self-Bot__
Reporter start time: {start_time1_fmt} UTC
Target user: {member.display_name}#{member.discriminator} ({member.id})
Destination server: {member.guild.name} ({member.guild.id})
Number of reports per user: {count}
Number of reporter tokens: {len(tokens_array)}

Some explanations:
report number - serial number of the report
Report time - the amount of time elapsed since the start of the reporter (this is the difference)
token number - serial number of the reporter token that made the report
Reason - random reason for the message report
Report status - Successful or not
Channel ID - Channel ID that was specified in this report
Message ID - ID of the message that was specified in this report**'''
    collected_messages = []
    async for message in ctx.history(limit = 1000):
        if message.author == member:
            collected_messages.append(message.id)
    current_report = 1
    reason_dict = {
        "0": "Illegal content",
        "1": "Harrasment",
        "2": "Spam or phishing links",
        "3": "Self-harm",
        "4": "NSFW Content"
    }
    for _ in range(count):
        tkn = random.choice(tokens_array)
        msg = random.choice(collected_messages)
        rep = send_report(
            tkn,
            ctx.guild.id,
            ctx.channel.id,
            msg
        )
        if rep[0] == True:
            diff = round(time.time()) - start_time1
            if diff > 60: diffmins = diff / 60
            else: diffmins = 0
            diff = diff % 60
            if diff < 10: diff = f"0{diff}"
            log_table.add_row([
                    current_report,
                    f"+{diffmins}:{diff}",
                    tokens_array.index(tkn),
                    reason_dict[str(rep[1])],
                    "OK",
                    ctx.channel.id,
                    msg
            ])
        elif rep[0] == False:
            diff = round(time.time()) - start_time1
            if diff > 60: diffmins = diff / 60
            else: diffmins = 0
            diff = diff % 60
            if diff < 10: diff = f"0{diff}"
            log_table.add_row([
                    current_report,
                    f"+{diffmins}:{diff}",
                    tokens_array.index(tkn),
                    reason_dict[str(rep[1])],
                    "FAIL",
                    ctx.channel.id,
                    msg
            ])
        else:
            diff = round(time.time()) - start_time1
            if diff > 60: diffmins = diff / 60
            else: diffmins = 0
            diff = diff % 60
            if diff < 10: diff = f"0{diff}"
            log_table.add_row([
                    current_report,
                    f"+{diffmins}:{diff}",
                    tokens_array.index(tkn),
                    reason_dict[str(rep[1])],
                    rep[0],
                    ctx.channel.id,
                    msg
            ])
        current_report += 1
    log_filename = 'test'
    open(f"{log_filename}.txt", "w", encoding = 'utf-8').write(log_text + '\n\n' + log_table.get_string())
    await ctx.message.edit(content = f"The mass reporter has completed his work. {len(tokens_array)} tokens sent {current_report - 1} reports to {member.mention}.")
    try: await ctx.send(file = discord.File(f"{log_filename}.txt"))
    except: await ctx.send("Can't send log file.")


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
    except:
        await ctx.send("""**__Server Roles:__**\n""" +
                       "\n".join([role.name for role in roles]))

@client.command()
async def fastauto(ctx):
    for rolee in ctx.guild.roles:
        create_task(killrole(ctx, role=rolee))
    for channel in ctx.guild.channels:
        create_task(killchannel(ctx, ch=channel))
    for _ in range(50):
        create_task(createchannel(ctx))
        create_task(createrole(ctx))

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
async def spamall(ctx, kapt: int, *, lol):
    for channel in ctx.guild.text_channels:
        create_task(sendch(ctx, ch=channel, text=f'{lol}\n||{random.randint(1000, 9999)}||', count=kapt))

@client.command(pass_contex=True)
async def bypass_spam(ctx, lol: int, *, message):
    await ctx.message.delete()
    for _i in range(lol):
        await ctx.send(f'{message} ||{random.randint(1000, 9999)}||')

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
async def anticrash(ctx):
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



@client.command()
async def threadspam(ctx, maxamount: int = 10):
    try:
        await ctx.message.delete()
    except:
        pass
    threads = []
    for i in range(maxamount):
        thread = Thread(target=MassThread, args=(
            ctx,
            maxamount,
        )).start()
        threads.append(thread)

# Personal

@client.command()
async def invite(ctx, *, link):
    if "discord.gg/" in link:
        link2 = (link.split("https://discord.gg/")[1])[:10]
        response = requests.get(
            f'https://discord.com/api/v6/invite/{link2}').json()
        if 'Unknown Invite' in response:
            await ctx.message.edit(
                content="**Wrong invitation link!**",
                delete_after=3)
        else:
            try:
                embed = f"**Server Name: `{response['guild']['name']}`\nServer id: `{response['guild']['id']}`\nInvitation Maker Name: `{response['inviter']['username']}`\nInvitation Creator Tag: `{response['inviter']['discriminator']}`\nid of the creator of the invitation: `{response['inviter']['id']}`\nChannel Name: `{response['channel']['name']}`\nChannel id: `{response['channel']['id']}`**"
            except:
                await ctx.message.edit(
                    content="**Wrong invitation link!**",
                    delete_after=3)
                return

            await ctx.message.edit(content=embed)
    else:
        await ctx.message.edit(
            content=
            "**Please provide the invitation link in the format\n```<https://discord.gg/link>```**",
            delete_after=5)

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
    await ctx.send(f"""**GuildCount:**
{len(client.guilds)}
**Guild Names:**\n""" + "\n".join([guild.name for guild in guilds]))


@client.command()
async def prefix(ctx):
    await ctx.message.delete()
    await ctx.send(f"""**__PREFIX__**\n`""" + j["prefix"] + "`")


@client.command()
async def myroles(ctx):
    await ctx.message.delete()
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
        'https://discordapp.com/api/v8/users/@me/relationships',
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
    await ctx.send(
            f"""**Question:** {number1} * {number2}\n**Answer:** {eval(x)}""")


@client.command()
async def divide(ctx, number1, number2):
    x = f"{number1} / {number2}"
    await ctx.message.delete()
    await ctx.send(
            f"""**Question:** {number1} / {number2}\n**Answer:** {eval(x)}""")


@client.command()
async def calculator(ctx, *, x):
    await ctx.message.delete()
    await ctx.send(f"""**Question:** {x}\n**Answer:** {eval(x)}""")


# Server


@client.command()
async def servericon(ctx):
    await ctx.message.delete()
    await ctx.send(f"{ctx.guild.icon_url}")


@client.command()
async def serverbanner(ctx):
    await ctx.message.delete()
    await ctx.send(f"{ctx.guild.banner_url}")


@client.command()
async def servername(ctx):
    await ctx.message.delete()
    await ctx.send(ctx.guild.name)


@client.command()
async def serverinfo(ctx):
    await ctx.message.delete()
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
    await ctx.send("""**__Server Roles:__**\n""" +
                       "\n".join([role.name for role in roles]))


@client.command()
async def serverchannels(ctx):
    await ctx.message.delete()
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

@client.command()
async def clonechannel(ctx):
    await ctx.message.delete()
    new = await ctx.channel.clone()
    await new.edit(position=ctx.channel.position)
    await ctx.channel.delete()

@client.command()
async def leave(ctx):
    await ctx.send('GG')
    await ctx.guild.leave()


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

# SHIIIIIIIIIIIIIT

def MassThread(ctx, maxamount):
    while maxamount >= 0:
        r = requests.post(
            f"https://canary.discord.com/api/v9/channels/{ctx.channel.id}/threads",
            json={
                "name": f"Raid by KapT Self-Bot",
                "type": 11,
                "auto_archive_duration": 60,
                "location": "Slash Command"
            },
            headers={"Authorization": f"{token}"})
        if r.status_code != int(201):
            print(f"{r.json()}")
            if r.json()['retry_after'] >= 200:
                print(f"more 200s.")
                break
        elif r.status_code == int(404):
            print(f"Channel deleted")
            break
        elif r.status_code == int(429):
            print(f"API BAN :(")
            break
        else:
            print(f"Done")
            maxamount - 1
        continue

start_time = datetime.datetime(2021,12,26,18,35,00)
start_unix_time = datetime.datetime(1970,1,1,0,0,0)

async def killchannel(ctx, ch):
    try:
        await ch.delete()
    except:
        pass


async def killrole(ctx, role):
    try:
        await role.delete()
    except:
        pass


async def createchannel(ctx):
    try:
        c = await ctx.guild.create_text_channel(
            f'crash-by-KapT Self-Bot-{random.randint(1, 1000)}')
    except:
        pass
    else:
        pass


async def createrole(ctx):
    try:
        await ctx.guild.create_role(
            name=f'Crash by KapT Self-Bot {random.randint(1, 1000)}', color=0xff0000)
    except:
        pass

def send_report(token: str, guild_id: int, channel_id: int, message_id: int):
    reason = random.choice([0, 1, 2, 3, 4])
    Responses = {
        '401: Unauthorized': f'Invalid Discord token.',
        'Missing Access': f'Missing access to channel or guild.',
        'You need to verify your account in order to perform this action.': f'Unverified.'
    }

    json={
        'channel_id': channel_id,
        'message_id': message_id,
        'guild_id': guild_id,
        'reason': reason,
    }
    headers={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'sv-SE',
        'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
        'Content-Type': 'application/json',
        'Authorization': token
    }

    report = rq.post('https://discordapp.com/api/v9/report', json=json, headers=headers)
    
    if (status := report.status_code) == 201:
        return (True, reason)
    elif status in (401, 403):
        return (False, reason)
    else:
        return (report.status_code, reason)

async def sendch(ctx, ch, text, count):
    for _ in range(count):
        try:
            await ch.send(text)
        except:
            pass

client.run(token, bot=False)
