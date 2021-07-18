import discord
import random
from discord import message
from discord import member
from discord.ext import commands

client = commands.Bot(command_prefix =".")

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency *1000)}ms ')

@client.command()
async def clear(ctx, amount=4):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f'Purged ``{amount}`` messages.')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
                ]
    await ctx.send(f'Question {question} \nAnswer: {random.choice(responses)}')

@client.command()
async def kick(ctx, member : discord.Member, *, reason='No reason'):
    await member.kick(reason=reason)
    await ctx.send(f'kicked ``{member}`` for ``{reason}``')

@client.command()
async def ban(ctx, member : discord.Member, *, reason='No reason'):
    await member.ban(reason=reason)
    await ctx.send(f'banned ``{member}`` for ``{reason}``')

@client.command(aliases=['whats up', 'wassup', 'what is up'])
async def sup(ctx):
    sup = [
        'nothin much',
        'nothin much, bord',
        'playing with my developer',
        'troubling Zeus in my backend :smirk:',
        'Googling how to make friends with humans. Not giving many potential results. :(',
        '*trying* to learn python. Yup, that\'s like biology for me.',
        'Banning a random dude',
            ]
    await ctx.send(random.choice(sup))

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discrimintor = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        idd = ban_entry.user.id

        if(user.name, user.discriminator) == (member_name, member_discrimintor):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned ``{user.name}#{user.discriminator}``')
            return
        if(user.id) == (member):
            await ctx.guild.unban(user)
            await ctx.send(f'unbanned ``{user.name}#{user.discriminator}``')






client.run('auth_token')
