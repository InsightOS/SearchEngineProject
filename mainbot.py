from os import name
import discord
from discord import guild
from discord import colour
from discord import emoji
from discord.commands.commands import option
from discord.components import SelectOption
from discord.embeds import E
from discord.ext import commands
from discord.commands import slash_command
from discord.gateway import DiscordClientWebSocketResponse, DiscordWebSocket
from discord.ui import Button, View


client = commands.Bot(command_prefix=";")

# pip install -U git+https://github.com/Pycord-Development/pycord
#&ssl_cert_reqs=CERT_NONE

@client.event
async def on_ready():
    print("The bot is ready!")

@client.slash_command(name="add", description="Add numbers!", guild_ids=[909388586770636830])
async def add(ctx, num1, num2):
    await ctx.respond(int(num1) + int(num2))

@client.slash_command(name="subtract", description="Subtract numbers!", guild_ids=[909388586770636830])
async def add(ctx, num1, num2):
    await ctx.respond(int(num1) - int(num2))

@client.slash_command(name="multiply", description="Multiply numbers!", guild_ids=[909388586770636830])
async def add(ctx, num1, num2):
    await ctx.respond(int(num1) * int(num2))

@client.slash_command(name="divide", description="Divide numbers!", guild_ids=[909388586770636830])
async def add(ctx, num1, num2):
    await ctx.respond(int(num1) / int(num2))

@client.message_command(name="repeat", guild_ids=[909388586770636830])
async def repeat(ctx, msg : discord.Message):
    await ctx.respond(msg.content)
    

class DropDownMenu(discord.ui.View):
    @discord.ui.select(placeholder="This is a placeholder", min_values=1, max_values=1, options=[
        discord.SelectOption(label="Google", description="Google is a popular search engine owned by Alphabet", emoji="🔍"),
        discord.SelectOption(label="Bing", description="Bing is a popular search engine owned by Microsoft", emoji="🤖"),
        discord.SelectOption(label="Yahoo", description="Yahoo is a popular search Engine", emoji="🟣"),
    ])
    async def callback(self, select, interaction: discord.Interaction):
        if select.values[0] == "Google":
            googleinfo = Button(
            label="Info", 
            style=discord.ButtonStyle.success,
            emoji="🔍"
        )
            googlelink = Button(
                label="Google.com",
                url="https://www.google.com/"
            )

            view = View()
            view.add_item(googleinfo)
            view.add_item(googlelink)

            googlembed = discord.Embed(
                title="Google",
                description="Google, a popular search engine is found in Chrome.",
                color=discord.Color.red()
            )
            googlembed.set_author(name="Sundar Pichai")
            googlembed.set_footer(text="~Created in 1998")
            googlembed.set_thumbnail(url="https://th.bing.com/th/id/OIP.rsq6Q0bnHJB-QRaolzy0_QHaE7?w=226&h=180&c=7&r=0&o=5&dpr=1.25&pid=1.7")
            googlembed.set_image(url="https://th.bing.com/th/id/R.e1cac80a8be6170cc82b9bc0fe323998?rik=v9%2ffVNF8HTLCuw&riu=http%3a%2f%2fsearchengineland.com%2ffigz%2fwp-content%2fseloads%2f2015%2f09%2fgoogle-logo-red2-slant-1920.jpg&ehk=cG%2b8zAzSiNghEBmuurARBgJCbRiCyeIu0BJvaabsOPA%3d&risl=&pid=ImgRaw&r=0")

            async def btn1callback(interaction: discord.Interaction):
                    googleinfo.disabled=True
                    await interaction.response.edit_message(embed=googlembed, view=view)
                    await interaction.followup.send('Google LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware. It is considered one of the Big Five companies in the American information technology industry, along with Amazon, Apple, Meta (Facebook) and Microsoft.[10]')

            googleinfo.callback = btn1callback

            await interaction.response.send_message(embed=googlembed, view=view)
        
        if select.values[0] == "Bing":
            bingembed = discord.Embed(
                title="Bing",
                description="Bing, a popular search engine found in Microsoft Edge.",
                colour = discord.Colour.blue()
            )
            bingembed.set_author(name="Microsoft")
            bingembed.set_footer(text="~Created in 2009")
            bingembed.set_thumbnail(url="https://th.bing.com/th/id/OIP.rU05JEf8LsJYo2kKzgJ1dwHaE8?pid=ImgDet&rs=1")
            bingembed.set_image(url="https://th.bing.com/th/id/OIP.fNhxQiPN7s7wWLsNIW-ErAHaEK?w=290&h=180&c=7&r=0&o=5&dpr=1.25&pid=1.7")

            bingbutton = Button(
                label="Info",
                style=discord.ButtonStyle.primary,
                emoji="🤖"
            )
            binglink = Button(
                label="Go to bing.com!",
                url="https://www.bing.com/"
            )
            bing=View()
            bing.add_item(bingbutton)
            bing.add_item(binglink)

            async def bingcallback(interaction: discord.Interaction):
                bingbutton.disabled=True
                await interaction.response.edit_message(embed=bingembed, view=bing)
                await interaction.followup.send("Microsoft Bing (commonly known as Bing) is a web search engine owned and operated by Microsoft. The service has its origins in Microsoft's previous search engines: MSN Search, Windows Live Search and later Live Search. Bing provides a variety of search services, including web, video, image and map search products. It is developed using ASP.NET. ")

            bingbutton.callback = bingcallback

            await interaction.response.send_message(embed=bingembed, view=bing)

        if select.values[0] == "Yahoo":
            yahooembed = discord.Embed(
                title="Yahoo",
                description="Yahoo, A popular search Engine was widely used in 2008",
                colour = discord.Colour.purple()
            )
            yahooembed.set_image(url="https://cdn.vox-cdn.com/thumbor/ab7sKh17o1dIEItiP63RFWZ7W7Y=/0x144:2000x1191/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/19224216/mb_yahoo_02.jpg")
            yahooembed.set_thumbnail(url="https://th.bing.com/th/id/OIP.r0vXmvHS4zfp2KSE7x-9HwHaHa?pid=ImgDet&rs=1")
            yahooembed.set_author(name="Yahoo inc.")
            yahooembed.set_footer(text="~Created in 1994")
            yahoobuttonlink = Button(
                label="Go to Yahoo.com!",
                url="https://in.search.yahoo.com/?fr2=inr"
            )
            yahoobutton = Button(
                label="Info",
                style=discord.ButtonStyle.secondary,
                emoji="🟣"
            )
            yahoo = View()
            yahoo.add_item(yahoobutton)
            yahoo.add_item(yahoobuttonlink)

            async def yahoobuttoncallback(interaction: discord.Interaction):
                yahoobutton.disabled=True
                await interaction.response.edit_message(embed=yahooembed, view=yahoo)
                await interaction.followup.send("Yahoo was established by Jerry Yang and David Filo in January 1994 and was one of the pioneers of the early Internet era in the 1990s.[9] In 2000, it was the most popular website worldwide.[10] Usage declined in the late 2000s as it lost market share to Google.[11][12] However, Yahoo domain websites are still among the most popular websites, ranking 12th in global engagement according to both Alexa Internet[13] and SimilarWeb.[14]")

            yahoobutton.callback=yahoobuttoncallback   

            await interaction.response.send_message(embed=yahooembed, view=yahoo)
              
@client.slash_command(name="search", description="A popular list of cool search engines!", guild_ids=[909388586770636830])
async def search(ctx):
    sample = discord.Embed(
        title="Choose your search Engine!",
        colour = discord.Colour.random()
    )
    dropdowns=DropDownMenu()

    await ctx.respond(embed=sample, view=dropdowns)


client.run('OTA5Mzg5NjUzMzk4OTQxNzI2.YZDlHQ.LwMf16wqDCtXskHeT7Q3eZRA24c')