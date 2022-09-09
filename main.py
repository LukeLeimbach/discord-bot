#!/usr/bin/env python

# Imports
from discord.ext import commands
import discord
import pickle
import math
import asyncio
import os
from dotenv import load_dotenv

# References
# Interaction: https://discordpy.readthedocs.io/en/master/interactions/api.html#interaction
# Discord: https://discordpy.readthedocs.io/en/stable/api.html#discord.Member.voice
# Discord.ext: https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Context

# Ready client
intents = discord.Intents.all()
client = commands.Bot(command_prefix=">>>", intents=intents)
bot_id = 828417423522267166


@client.event
async def on_ready():
    print(f"[+] {client.user.display_name} is ready")


# Dumps the vote limit
@client.command()
async def votelimit(ctx, *, cap):
    filename = "limit"
    outfile = open(filename, "wb")
    pickle.dump(int(cap), outfile)
    outfile.close()
    print(f"[+] Voting cap has been set to {cap}")


# Dumps time limit in minutes
@client.command()
async def timelimit(ctx, *, time):
    filename = "time"
    outfile = open(filename, "wb")
    pickle.dump(int(time), outfile)
    outfile.close()
    print(f"[+] Voting time has been set to {time} minutes")


# Returns pickled vote limit
def getVoteLimit():
    filename = "limit"
    infile = open(filename, "rb")
    final = pickle.load(infile)
    infile.close()
    return final


# Returns pickled time limit in minutes
def getTimeLimit():
    filename = "time"
    infile = open(filename, "rb")
    final = pickle.load(infile)
    infile.close()
    return int(final)


# Variables for votekick function
timer_finished = False


@client.command()
async def votekick(ctx, *, member: discord.Member):
    print(f"Votekick started against {member.display_name}")

    # Resets function
    global votekick_message_id
    global yes_reaction_count
    yes_reaction_count = 0

    start_embed = discord.Embed(title="🥶Votekick Started🥶",
                                description=f"{member.mention} forgor 💀 that nobody likes him 👿\nmaking him tonights big loser 💨\n\n"
                                            f"{getVoteLimit()} of you bozos 💯 have exactly | {getTimeLimit()} | minit ⏱ "
                                            f"to get\nthis dweeb 🤓 out of my mf server 👍\n\n",
                                color=0xfff700)

    time_out_embed = discord.Embed(title="⏱You out of time⏱",
                                   description=f"Unfortunately, {member.mention} gets to stay 👎",
                                   color=0xfa0000)

    kick_embed = discord.Embed(title="🥾 RIP Bozo 🥾",
                               description=f"Less go <:DABABY:823769285787648051>, {member.mention} got schmacked.\n"
                                           f"Tommy Hillfiger 💯 would be proud",
                               color=0x22ff00)

    rejoin_embed = discord.Embed(title="🖕 Join back ig loser 🖕",
                                 # Sends invite to the dweeb that got kicked
                                 description=await ctx.channel.create_invite(),
                                 color=0xf50aed)

    # Sends votekick message then sends id outside function
    votekick_message = await ctx.send(embed=start_embed)
    votekick_message_id = votekick_message.id

    # Reacts to start the voting
    await votekick_message.add_reaction("👍")

    # Counter Function
    async def counter():
        global kicked_member
        time_limit = getTimeLimit()
        for i in range(int(math.floor(time_limit * 60))):
            if yes_reaction_count == int(getVoteLimit()):
                # Kicks user
                await ctx.send(embed=kick_embed)

                # Invites user back
                dm = await member.create_dm()
                await dm.send(embed=rejoin_embed)

                # Saves member
                kicked_member = member
                await member.kick()
                return
            await asyncio.sleep(1)
        # Times out after timer is complete
        await ctx.send(embed=time_out_embed)

    # Opens thread to finish out function and let rest of program run
    asyncio.get_event_loop().create_task(counter())


@client.event
async def on_reaction_add(reaction, user):
    global yes_reaction_count
    if user.id != bot_id:
        if reaction.message.id == votekick_message_id:
            if reaction.emoji == "👍":
                yes_reaction_count += 1


@client.event
async def on_reaction_remove(reaction, user):
    global yes_reaction_count
    if user.id != bot_id:
        if reaction.message.id == votekick_message_id:
            if reaction.emoji == "👍":
                yes_reaction_count -= 1


@client.event
async def on_member_join(member: discord.Member):
    if member.id == kicked_member.id:
        for role in kicked_member.roles:
            if role.id == 261601676941721602:
                continue
            await member.add_roles(role)


# Get token from .env and run client
load_dotenv()
TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
