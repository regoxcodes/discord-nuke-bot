import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot logged in as {bot.user}')
    print(f'🤖 Bot is ready and listening for commands!')
    print(f'📋 Use: !nuke <server_name> to nuke a server')

@bot.command(name='nuke')
async def nuke_server(ctx, *, server_name: str = None):
    """
    Nuke the server: delete all channels and roles, then recreate with a custom name
    Usage: !nuke MyNewServerName
    """
    
    # Check if user is owner
    if ctx.author != ctx.guild.owner:
        await ctx.send("❌ Only the server owner can use this command!")
        return
    
    if not server_name:
        await ctx.send("❌ Please provide a server name! Usage: `!nuke YourServerName`")
        return
    
    try:
        # Confirmation message
        embed = discord.Embed(
            title="⚠️ NUKE CONFIRMATION",
            description=f"This will:\n1. Delete ALL channels\n2. Delete ALL roles\n3. Rename server to: **{server_name}**\n\nReact with ✅ to confirm (30 seconds)",
            color=discord.Color.red()
        )
        confirmation_msg = await ctx.send(embed=embed)
        await confirmation_msg.add_reaction('✅')
        await confirmation_msg.add_reaction('❌')
        
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['✅', '❌']
        
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
            
            if str(reaction.emoji) == '❌':
                await ctx.send("❌ Nuke cancelled!")
                return
            
            if str(reaction.emoji) != '✅':
                return
                
        except discord.errors.TimeoutError:
            await ctx.send("⏱️ Nuke cancelled - timeout!")
            return
        
        # Start nuking
        nuke_status = await ctx.send("🔥 **STARTING NUKE SEQUENCE...**")
        
        guild = ctx.guild
        
        # Delete all channels
        await nuke_status.edit(content="🔥 **STARTING NUKE SEQUENCE...**\n⏳ Deleting channels...")
        for channel in guild.channels:
            try:
                await channel.delete()
            except Exception as e:
                print(f"Error deleting channel {channel.name}: {e}")
        
        # Delete all roles (except @everyone)
        await nuke_status.edit(content="🔥 **STARTING NUKE SEQUENCE...**\n⏳ Deleting channels... ✅\n⏳ Deleting roles...")
        for role in guild.roles:
            if role != guild.default_role:  # Don't delete @everyone
                try:
                    await role.delete()
                except Exception as e:
                    print(f"Error deleting role {role.name}: {e}")
        
        # Rename the server
        await nuke_status.edit(content="🔥 **STARTING NUKE SEQUENCE...**\n⏳ Deleting channels... ✅\n⏳ Deleting roles... ✅\n⏳ Renaming server...")
        await guild.edit(name=server_name)
        
        # Create a welcome channel
        await nuke_status.edit(content="🔥 **STARTING NUKE SEQUENCE...**\n⏳ Deleting channels... ✅\n⏳ Deleting roles... ✅\n⏳ Renaming server... ✅\n⏳ Creating welcome channel...")
        welcome_channel = await guild.create_text_channel("welcome")
        
        # Send completion message
        embed = discord.Embed(
            title="✅ NUKE COMPLETE!",
            description=f"🎉 Server has been nuked and renamed to **{server_name}**\n\n✨ Fresh start ready!",
            color=discord.Color.green()
        )
        await welcome_channel.send(embed=embed)
        await nuke_status.delete()
        await ctx.send("✅ **NUKE COMPLETE!** Server is now fresh and clean!")
        
    except Exception as e:
        await ctx.send(f"❌ Error during nuke: {e}")
        print(f"Error: {e}")

@bot.command(name='help')
async def help_command(ctx):
    """Show available commands"""
    embed = discord.Embed(
        title="🤖 Discord Nuke Bot Help",
        description="Available commands:",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="!nuke <server_name>",
        value="Nuke the server and rename it. Only owner can use this.",
        inline=False
    )
    embed.add_field(
        name="!help",
        value="Show this help message",
        inline=False
    )
    await ctx.send(embed=embed)

# Run the bot
TOKEN = os.getenv('DISCORD_TOKEN')
if not TOKEN:
    print("❌ ERROR: DISCORD_TOKEN not found in .env file!")
    print("Please create a .env file with your bot token. See .env.example for details.")
else:
    bot.run(TOKEN)
