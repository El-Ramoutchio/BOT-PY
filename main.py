import discord
from discord.ext import commands
from discord import Member


client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print(f'Connected as: {client.user}')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="les joueurs de DreamTownRP"))



@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f"{ctx.author.mention} a ban {member.mention}")

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f"{ctx.author.mention} a kick {member.mention}")


@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{ctx.author.mention} a unban {member.mention}")
            return

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def mute(ctx, member: discord.Member):
  role = ctx.guild.get_role(902602635578863687)
  await member.add_roles(role)
  await ctx.send(f"{ctx.author.mention} a muté {member.mention}")

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def unmute(ctx, member: discord.Member):
  role = ctx.guild.get_role(902602635578863687)
  await member.remove_roles(role)
  await ctx.send(f"{ctx.author.mention} a unmute {member.mention}")




@client.command()
async def dreamtownrp(ctx):
    await ctx.send("Voici un lien temporaire : https://discord.gg/7djQENAj6q")

@client.command()
async def GG(ctx):
    await ctx.send("Tes trop un bg mek ta trouver la commande secrete ! 🧐")



client.run('')
    
