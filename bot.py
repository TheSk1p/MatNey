import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="/", help_command=None, intents=disnake.Intents.all())

CENSORED_WORDS = ["бл.ть","блять","с.ка","сука","даун"]

@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")

@bot.event
async def on_member_join(member):
    role = await disnake.utils.get(guild_id=member.guild.id, role_id=1181842915933306880)
    channel = member.guild.system_chanel

    embed = disnake.Embed(
        title="Новый учасник!",
        description=f"{member.name}#{member.discriminator}",
        color=0xffffff
    )

    await member.add_roles(role)
    await channel.send("embed=embed")

@bot.event
async def on_message(message):
    for content in message.content.split():
        for censored_word in CENSORED_WORDS:
            if content == censored_word:
                await message.delete()
                await message.channel.send(f"{message.author.mention} такие слова запрещены!!!")

bot.run("MTE4NzEwODQ1NDg1MTE1Mzk5MQ.GzHmE0.F0JD4YWSq-MBsrJWw-o1d7UHXyuBaQbGDHGf7A")
