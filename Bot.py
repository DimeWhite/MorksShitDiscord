from discord.ext import commands
from faceit_api import FaceitData
import pyosu


OSUToken = "2e0538f28b266e07d7b16f84c7a542056a65fc9d"
FaceitToken = "4fe49639-5c4e-46fb-99dd-c979336a3d5c"
DSToken = "NzE5NDg1MjA4NDUzMTg1NTg5.Xt4QfA.Sz1CrRQSJwtDqf0eRH5WP5DB30A"

bot = commands.Bot(command_prefix="!")


@bot.command(pass_context=True)
async def faceit(ctx, arg):
    elo = faceit.player_details(arg)['games']['csgo']['faceit_elo']
    if elo is None:
        await ctx.send("Пользователь не найден")
    else:
        await ctx.send("{}\nElo = {} \nlvl =  {}".format(faceit.player_details(arg)['nickname'], elo, faceit.player_details(arg)['games']['csgo']['skill_level']))


@bot.command(pass_context=True)
async def osu(ctx, arg):
    await ctx.send("{}'s pp  = {}".format(arg, osu.user(arg, 0, 'pp_raw')))


faceit = FaceitData(FaceitToken)
osu = pyosu.main(OSUToken)
bot.run(DSToken)
