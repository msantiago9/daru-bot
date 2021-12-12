import os
import requests
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=".", intents=intents, help_command=None)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = json.loads(response.text)
    quote = data[0]["q"] + " -" + data[0]["a"]
    return quote


def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any")
    data = json.loads(response.text)
    if data["type"] == "twopart":
        joke = data["setup"] + " " + data["delivery"]
        return joke
    return data["joke"]


@client.command(aliases=["quote", "q"])
async def __remember(ctx):
    await ctx.send(get_quote())


@client.command(aliases=["joke", "j"])
async def __joke(ctx):
    await ctx.send(get_joke())


@client.command(aliases=[""])
async def __nil(ctx):
    await ctx.send("...")


@client.command(aliases=["hello"])
async def __hello(ctx):
    await ctx.send("hi")


@client.command(aliases=["hakka"])
async def __hakka(ctx):
    await ctx.send("It's 'Hacker' not 'Hakka'")


@client.command(aliases=["invite", "i"])
async def __invite(ctx):
    await ctx.send(
        "<https://discord.com/api/oauth2/authorize?client_id=919592181038190633&permissions=2147732544&scope=bot>"
    )


@client.event
async def on_ready():
    print(f"logged in as {client.user}")


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="lab member")
    await member.add_roles(role)
    print("assigned role.")


client.run(os.getenv("BOT_TOKEN"))
