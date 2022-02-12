#Llamado de Librerias
#from inspect import Parameter
import discord
from discord import client
from discord.embeds import Embed
from discord.errors import ClientException
from discord.ext import commands
from discord.utils import get
import datetime
from discord.file import File
from discord.flags import Intents
import conf.formats 

#Lista de Variables
Prefix = ">"
DescriptionBot = "Goverment"
#Token = "OTAwMDgyODM4MTQ0MTc2MTI4.YW8Jdw.76TySGwY699I1efUbRlANUwT8nU"
Token = 'ODg3NTA5MjIzNDc3NDc3Mzc2.YUFLYA.HSGOz-32sea2BV3o308M9dUWO1U'

Status =  discord.Status.online
Activity = discord.Game(f"[{Prefix}] Goverment Administration")

Client = commands.Bot(command_prefix = Prefix, case_insensitive = True, help_command = None, description = DescriptionBot)

#Lista de Variables Fijas
Months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

#Funciones
def Create_Embed(Title = "", Description = "", Fields = (), Thumbnail = "", Timestamp = datetime.datetime.utcnow(), Color = discord.Color.red()):
    Embed = discord.Embed(title = f'{Title}', description = f'{Description}', timestamp=Timestamp, color=Color)
    for Field in Fields:
        if Field != " ":
            Embed.add_field(name = f"{Field[0]}", value = f"{Field[1]}")
    if Thumbnail != '':
        Embed.set_thumbnail(url = f'{Thumbnail}')
    return Embed

# Events
@Client.event
async def on_ready():                                               #Bot Startup
    await Client.change_presence(status = Status, activity = Activity, afk=False)
    print("Bot ready")

@Client.event
async def on_command_error(ctx, error):                             #Manejo de errores
    await ctx.send(error)
    #await ctx.message.delete()
    print(f"[{datetime.datetime.utcnow()}/Error]: {ctx.message.author} {error}")

#Commands
@Client.command()
async def help(ctx):                                                #Custom help command
    Embed = Create_Embed(Title = "Help", Description = "Help command menu", Fields = (('>info', 'Server information'), ('>purge <limit>', 'delete the last <limit> message'), ('>kick <member> <reason>', 'kick a member with reason'), ('>say <file> <content>', 'say a message with file'), ('>role <member> <add/rem> <role>','add/remove a member roles')), Color = discord.Color.red(), Thumbnail = ctx.guild.icon_url)
    await ctx.send(embed = Embed)

@Client.command(pass_context = True)
async def info(ctx):                                                #Server Info
    Embed = Create_Embed(Title = ctx.guild.name, Description = "Server info", Fields = (('Server created at',ctx.guild.created_at), ('Server Owner', ctx.guild.owner), ('Server Region', ctx.guild.region), ('Server ID', ctx.guild.id)), Color = discord.Color.red(), Thumbnail = ctx.guild.icon_url)
    await ctx.send(embed = Embed)

@Client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def hello(ctx, Member: discord.Member):                       #Say hello
    await ctx.send(f'Bienvenido {Member} al servidor!.')

@Client.command(pass_context = True)
async def ping(ctx):                                                #Ping response
    await ctx.channel.send(f"Pong {round(client.latency*1000)} ms", em)

@Client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def purge(ctx, limit:int):                                    #Purge Chat
    await ctx.message.delete()
    await ctx.channel.purge(limit = limit) 

@Client.command(pass_context = True)
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason = "None"):    #Kick Member
    await member.kick(reason=reason)
    await ctx.message.delete()
    await ctx.send(f'{discord.Member} has been kicked by {ctx.message.author} for {reason}!')


@Client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def say(ctx, File:str, *, arg = ""):                          #Escribir Chat
    await ctx.message.delete()
    if File != ".":
            await ctx.send(arg)
    else:
        await ctx.send(arg)

@Client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def embed(ctx,title = "", desc = "", thumbnail = "", *, arg = ""):#Escribir Chat
    if thumbnail == ".":    thumbnail = ctx.guild.icon_url

    Embed = Create_Embed(Title = title, Description = desc, Fields = (('1st field',f'{arg}'),('2nd field',f'{arg}')), Color = discord.Color.red(), Thumbnail = thumbnail)
    await ctx.send(embed = Embed)

@Client.command(pass_context = True)
@commands.has_permissions(manage_roles = True)                      #Add/Remove Role
async def role(ctx, member: discord.Member, modo: str, role: discord.Role, *, arg = ""):
    await ctx.message.delete()

    if modo == "add":
        await member.add_roles(role)
    else:
        await member.remove_roles(role)

#Start
Client.run(Token)