import discord
from discord.ext import commands

import requests
import asyncio

from os import environ


class HyLink(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="verify")
    async def verify_(self, ctx):
        await ctx.send("✉️ Instructions sent in direct messages!")
        embed = discord.Embed(
            description=f'**Instructions:**\n1) Use your Minecraft client to connect to Hypixel.\n2) Once connected, and while in the lobby, right click "My Profile" in your hotbar. It is option #2.\n3) Click "Social Media" - this button is to the left of the Redstone block (the "Status" button).\n4) Click "Discord" - it is the second last option.\n5) Paste your Discord username into chat and hit enter. For reference your username is: `{ctx.author}`.\n6) You\'re done! Wait around 30 seconds and then click the :white_check_mark: reaction to continue.',
            color=discord.Colour.purple(),
        )
        embed.set_image(
            url="https://thumbs.gfycat.com/DentalTemptingLeonberger-size_restricted.gif"
        )
        embed.set_author(
            name="Link your Hypixel Profile", icon_url=self.bot.user.avatar_url
        )
        message = await ctx.author.send(embed=embed)
        await message.add_reaction("✅")

        def check(reaction, user):
            return str(reaction.emoji) in ["✅"] and user != self.bot.user

        try:
            reaction, user = await self.bot.wait_for(
                "reaction_add", check=check, timeout=450
            )

        except asyncio.TimeoutError:
            await ctx.author.send("**Timeout:** You didn't react in time.")

        else:
            if str(reaction.emoji) == "✅":
                embed = discord.Embed(color=discord.Colour.purple())
                embed.set_author(
                    name="Please enter your Minecraft username.",
                    icon_url=self.bot.user.avatar_url,
                )
                await ctx.author.send(embed=embed)
                ign = await self.bot.wait_for("message")
                r = requests.get(
                    f"https://api.hypixel.net/player?key={environ.get('API_KEY')}&name={ign.content}"
                )
                if r.json()["player"]["socialMedia"]["links"]["DISCORD"] == ctx.author:
                    await ctx.author.send("✅  You've been verified!")
                    await ctx.author.edit(nick=ign.content)
                    await ctx.author.add_roles("Verified")
                else:
                    await ctx.author.send(
                        ":x: Couldn't verify you, this could be due to you not having your discord linked, or your IGN is incorrect."
                    )


bot = commands.Bot(command_prefix="!", intents=intents=discord.Intents(guilds=True, messages=True, reactions=True))
bot.add_cog(HyLink(bot))
bot.run(environ.get("TOKEN"))
