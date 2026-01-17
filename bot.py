from config import *
from logic import *
import discord
from discord.ext import commands
from config import TOKEN

# Menginisiasi pengelola database
manager = DB_Map("databasfrom config import *
from logic import *
import discord
from discord.ext import commands
from config import TOKEN

user_colors = {}

# Menginisiasi pengelola database
manager = DB_Map("database.db")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())



@bot.event
async def on_ready():
    print("Bot started")

@bot.command()
async def start(ctx: commands.Context):
    await ctx.send(f"Halo, {ctx.author.name}. Masukkan !help_me untuk mengeksplorasi daftar perintah yang tersedia")

@bot.command()
async def help_me(ctx: commands.Context):
    await ctx.send(
        "**Daftar Perintah:**\n"
        "!start → Memulai bot\n"
        "!help_me → Menampilkan bantuan\n"
        "!show_city <nama_kota> → Menampilkan peta kota\n"
        "!remember_city <nama_kota> → Menyimpan kota\n"
        "!show_my_cities → Menampilkan peta kota yang kamu simpan\n"
        "!set_color <red, blue, green, yellow, purple, orange, black, cyan> → Mengubah dan menyimpan warna kamu"
    )

@bot.command()
async def set_color(ctx: commands.Context, color: str):
    user_colors[ctx.author.id] = color
    await ctx.send(f"Warna titik kota kamu diset ke **{color}**")

@bot.command()
async def show_city(ctx: commands.Context, *, city_name=""):
    if not city_name:
        await ctx.send("Silakan masukkan nama kota.")
        return

    color = user_colors.get(ctx.author.id, "red")
    path = f"map_{ctx.author.id}.png"
    manager.create_graph(path, [city_name], color=color)
    await ctx.send(file=discord.File(path))

@bot.command()
async def show_my_cities(ctx: commands.Context):
    cities = manager.select_cities(ctx.author.id)

    if not cities:
        await ctx.send("Kamu belum menyimpan kota apa pun.")
        return

    path = f"map_{ctx.author.id}.png"
    manager.create_graph(path, cities)
    await ctx.send(file=discord.File(path))

@bot.command()
async def remember_city(ctx: commands.Context, *, city_name=""):
    if manager.add_city(ctx.author.id, city_name):  # Memeriksa apakah kota ada dalam database; jika ya, menambahkannya ke memori pengguna
        await ctx.send(f'Kota {city_name} telah berhasil disimpan!')
    else:
        await ctx.send("Format tidak benar. Silakan masukkan nama kota dalam bahasa Inggris, dengan spasi setelah perintah.")

if __name__ == "__main__":
    bot.run(TOKEN)e.db")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot started")

@bot.command()
async def start(ctx: commands.Context):
    await ctx.send(f"Halo, {ctx.author.name}. Masukkan !help_me untuk mengeksplorasi daftar perintah yang tersedia")
    
@bot.command()
async def help_me(ctx: commands.Context):
    await ctx.send(
        "**Daftar Perintah:**\n"
        "!start → Memulai bot\n"
        "!help_me → Menampilkan bantuan\n"
        "!show_city <nama_kota> → Menampilkan peta kota\n"
        "!remember_city <nama_kota> → Menyimpan kota\n"
        "!show_my_cities → Menampilkan peta kota yang kamu simpan"
    )

@bot.command()
async def show_city(ctx: commands.Context, *, city_name=""):
    if not city_name:
        await ctx.send("Silakan masukkan nama kota.")
        return

    path = f"map_{ctx.author.id}.png"
    manager.create_graph(path, [city_name])
    await ctx.send(file=discord.File(path))

@bot.command()
async def show_my_cities(ctx: commands.Context):
    cities = manager.select_cities(ctx.author.id)

    if not cities:
        await ctx.send("Kamu belum menyimpan kota apa pun.")
        return

    path = f"map_{ctx.author.id}.png"
    manager.create_graph(path, cities)
    await ctx.send(file=discord.File(path))

@bot.command()
async def remember_city(ctx: commands.Context, *, city_name=""):
    if manager.add_city(ctx.author.id, city_name):  # Memeriksa apakah kota ada dalam database; jika ya, menambahkannya ke memori pengguna
        await ctx.send(f'Kota {city_name} telah berhasil disimpan!')
    else:
        await ctx.send("Format tidak benar. Silakan masukkan nama kota dalam bahasa Inggris, dengan spasi setelah perintah.")

if __name__ == "__main__":
    bot.run(TOKEN)
