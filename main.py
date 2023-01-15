from operator import truediv
import os
from pickle import TRUE
from pydoc import describe
from turtle import color


import discord
from discord import Option, SlashCommandOptionType
from dotenv import load_dotenv

from lib import OsuBot, Api, UserNotFound, RANKING_EMOJIS, UserScoreNotFound
from lib.errors import BeatmapNotFound


load_dotenv()
intents = discord.Intents.default()

bot_instance = OsuBot(intents=intents, help_command=None)
API = Api(api_key=os.getenv("API_KEY"))


@bot_instance.event
async def on_ready():
    print("Sylfe Bot has started")

@bot_instance.bridge_command(name="info")
async def info_command(ctx
    
    
    ):  

    embed = discord.Embed(
     title=f'Sylfe Bot Info',
     timestamp=discord.utils.utcnow(),
     description=f"""Bot Created by N3k0H3nt4i"""
     )

    embed.set_footer(text=f'{len(bot_instance.guilds)} guilds.')
    await ctx.respond(embed=embed)

@bot_instance.bridge_command(name="chuj")
async def chuj(ctx
    
    
    ):  

    embed = discord.Embed(
     title=f'Are you happy cherry?????',
     timestamp=discord.utils.utcnow(),
     description=f"""
     
      …………………...„„-~^^~„-„„_
………………„-^*'' : : „'' : : : : *-„
…………..„-* : : :„„--/ : : : : : : : '\
…………./ : : „-* . .| : : : : : : : : '|
……….../ : „-* . . . | : : : : : : : : |
………...\„-* . . . . .| : : : : : : : :'|
……….../ . . . . . . '| : : : : : : : :|
……..../ . . . . . . . .'\ : : : : : : : |
……../ . . . . . . . . . .\ : : : : : : :|
……./ . . . . . . . . . . . '\ : : : : : /
….../ . . . . . . . . . . . . . *-„„„„-*'
….'/ . . . . . . . . . . . . . . '|
…/ . . . . . . . ./ . . . . . . .|
../ . . . . . . . .'/ . . . . . . .'|
./ . . . . . . . . / . . . . . . .'|
'/ . . . . . . . . . . . . . . . .'|
'| . . . . . \ . . . . . . . . . .|
'| . . . . . . \„_^- „ . . . . .'|
'| . . . . . . . . .'\ .\ ./ '/ . |
| .\ . . . . . . . . . \ .'' / . '|
| . . . . . . . . . . / .'/ . . .|
| . . . . . . .| . . / ./ ./ . .|
     
     """
     )

    embed.set_footer(text=f'{len(bot_instance.guilds)} guilds.')
    await ctx.respond(embed=embed)



@bot_instance.bridge_command(name="pussy")
async def info_command(ctx
    
    
    ):  

    embed = discord.Embed(
     title=f'Are you happy losuli???',
     timestamp=discord.utils.utcnow(),
     description=f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠔⠁⣤⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠓⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠿⠂⣀⣴⣶⣶⠟⠋⠀⠁⠙⠻⣶⣶⣦⡀⠀⠀⠀⠀⠀⠉⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠂⣀⠀⠀⡛⠁⣼⣿⡿⢹⡏⠀⠀⠀⠀⠀⠀⢸⣿⣿⣽⣤⡀⠀⠀⣽⠖⠀⠀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣱⣶⠖⠃⣼⣿⣿⣠⣿⣷⠀⠀⣸⠀⡀⣀⣸⣿⣿⣿⣿⣷⠀⠀⠈⠃⠀⢠⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⢉⠀⠀⠛⡇⠀⠶⢿⣿⣿⣿⣿⣿⢠⣼⣿⢸⣧⣿⣿⣿⣿⣿⣿⣇⠀⣵⡶⠀⣀⡜⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣶⡆⠀⠀⠀⠀⣼⠿⣿⣿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿⣿⣿⡿⠀⠀⠈⠀⣀⣼⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠀⠀⠀⠀⢀⣴⠂⢸⣿⣿⣿⣿⣿⣿⣿⣿⡙⣿⣿⣿⠏⠁⣤⣀⣴⣾⡿⠋⠙⢦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⣰⠋⣁⣴⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⡝⣟⠁⡰⠉⢹⣿⡟⢁⠀⢠⡏⠀⢀⣀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⣿⠧⠀⡈⠁⠛⠀⢿⡟⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠟⠋⠁⠀⠀⠀⠀⠀⠈⠉⠻⠛⠛⠻⡿⠛⠋⠉⠉⠀⠀⠉⠙⠻⢿⣿⣦⣄⠳⠒⠦⡴⣄⠀⠀⣿⣄⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷⡄⠀⠓⢺⠀⠞⠉⠋⠀
⠀⠀⠀⠀⠀⢀⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣶⣸⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⠀⠀⠀⠀⠀
⠀⠀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠅⠀⣷⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠉⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀
⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣄⠀⠀⠀⢈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀
⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣦⢴⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠟⠀⠀⠀
⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡿⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀
⠀⠀⠈⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀
⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣧⣏⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣶⣶⣦⣤⣤⣤⣶⣾⣿⣿⣿⣿⢻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⠈⢻⣿⣿⣿⣷⣶⣤⣤⣀⣀⣤⣤⣶⣾⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣭⣥⣤⣭⣿⣿⣿⣿⠇⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡶⣶⣶⣶⣶⣶⣶⣶⡆⢰⣶⡆⠀⠰⠶⢤⣖⣆⣤⣠⣶⣶⣶⣦⣖⣦⠶⣴⠟⣶⡶⣶⡶⠀⠀⠀⠀⠀⠀⠀⠀

     """
     )

    embed.set_footer(text=f'{len(bot_instance.guilds)} guilds.')
    await ctx.respond(embed=embed)
























@bot_instance.slash_command(name='player', description='Check player statistics.')
async def osu_player(
        ctx,
        name: str,
        mode: Option(
            SlashCommandOptionType.string,
            description="osu! game type.",
            choices=["osu!", "osu!mania", "Taiko", "CtB"]
        ) = "osu!"
):
    try:
        player = await API.get_osu_player(name=name, mode=mode)
        best_score = await player.best_score
        best_score_map = await best_score.map
    except UserNotFound:
        return await ctx.respond(
            embed=discord.Embed(title="User not found!", colour=discord.Colour.red()),
            ephemeral=True
        )
    except UserScoreNotFound:
        return await ctx.respond(
            embed=discord.Embed(title="User has no stats in this game mode!", colour=discord.Colour.red()),
            ephemeral=True
        )
    except BeatmapNotFound:
        return await ctx.respond(
            embed=discord.Embed(title="Beatmap to display user scores not found!", colour=discord.Colour.red()),
            ephemeral=True
        )




    embed = discord.Embed(
        title=f'{player.username} **{player.country}** :flag_{player.country.lower()}: - Lvl. {player.level}',
        timestamp=discord.utils.utcnow(),

        description=f"""
        [Profile](https://osu.ppy.sh/users/{player.user_id})
        『』**Rank:** `{player.rank}` ***Country Rank:** `{player.country_rank}` :flag_{player.country.lower()}:
        『』**PP:** **`{player.pp}`** **Accuracy**: `{player.accuracy}%`
        『』**Ranks count:**
               <:SilverSS:1048930750923292742>  `{player.total_ssh}`
               <:SS:1048930749392375848>  `{player.total_ss}` 
               <:SilverS:1048930747773366282>  `{player.total_sh}`
               <:S_:1048930745860759582>  `{player.total_s}`
               <:A_:1048930739019845694>  `{player.total_a}`\n
        『』**Playcount:** {player.play_count} Time: **{player.total_time}**
        『』**joined on {player.join_date}**
        """,

    )

    embed.set_footer(text=f'{len(bot_instance.guilds)} guilds.')
    await ctx.respond(embed=embed)



'''
@bot_instance.slash_command(name='recent', description='Check player recent play.')
async def recent_play(
        ctx,
        name: str,
        mode: Option(
            SlashCommandOptionType.string,
            description="osu! game type.",
            choices=["osu!", "osu!mania", "Taiko", "CtB"]
        ) = "osu!"
):   

    try:
        player = await API.get_osu_player(name=name, mode=mode)
    except UserNotFound:
        return await ctx.respond(
            embed=discord.Embed(title="User not found!", colour=discord.Colour.red()),
            ephemeral=True
        )






    embed = discord.Embed(
        title=f'"{player.username} Recent Play',
        timestamp=discord.utils.utcnow(),

        color=discord.Color.blue(),
        description=f"""{player.recent_score}
        """,

    )

    embed.set_footer(text=f'{len(bot_instance.guilds)} guilds.')
    await ctx.respond(embed=embed)
 '''

@bot_instance.slash_command(name='recent', description='Check player recent play.')
async def recent_play(ctx, name: str,  
            mode: Option(
            SlashCommandOptionType.string,
            description="osu! game type.",
            choices=["osu!", "osu!mania", "Taiko", "CtB"]
        ) = "osu!"):
    try:
        player = await API.get_osu_player(name=name, mode=mode)
    except UserNotFound:
        return await ctx.respond(
            embed=discord.Embed(title="User not found!", colour=discord.Colour.red()),
            ephemeral=True
        )

    embed = discord.Embed(
        title=f"{player.username}'s Recent Play",
        timestamp=discord.utils.utcnow(),
        color=discord.Color.blue(),
        description=f"{player.recent_play}"
    )

    embed.set_footer(text=f'{len(bot_instance.guilds)} guilds.')
    await ctx.respond(embed=embed)







if __name__ == "__main__":
    bot_instance.run(os.getenv("TOKEN"))
