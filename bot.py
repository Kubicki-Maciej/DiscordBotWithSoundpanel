import sys
import time
import discord
from discord import FFmpegPCMAudio, voice_client, guild
from discord.ext import commands
import youtube_dl
from dotenv import load_dotenv
import asyncio

import Sound
import auth as a


youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename


intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="!", intents=intents)



@client.command(pass_context=True)
async def player(ctx):
    if ctx.author.voice:
        sys.path.append('E:\SoundsPanel')
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('troll.mp3')
        voice.play(source)

    else:
        await ctx.send("you are not in voice channel")


@client.command()
async def hellotest(tic):
    toc = time.perf_counter()
    print(f" odtwarzanie trwało : {toc - tic:0.4f} seconds")
    print("hello")


@client.command()
async def play_music_from_sound_panel(path, tic):
    print(f"play music {path}")
    toc = time.perf_counter()
    print(f" wczytanie trwało : {toc - tic:0.4f} seconds")
    lok = time.perf_counter()
    if client.voice_clients[0].is_playing():
        print("player gra")
        client.voice_clients[0].stop()
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(path))
    client.voice_clients[0].play(source)
    glok = time.perf_counter()
    print(f" wczytanie odtwarzania pliku trwało : {glok - lok:0.4f} seconds")



@client.command()
async def stop_sound_panel():
    if client.voice_clients[0]:
        client.voice_clients[0].stop()

@client.event
async def on_ready():
    print("TEST Bot is ready to use")
    print("*******TEST*TEST*TEST********")


@client.command()
async def hello(ctx):
    await ctx.send("Hello Im SoundBox player")


# joke on start
@client.event
async def on_meber_join(meber):
    print("Hello new meber")


@client.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
    else:
        await ctx.send("you are not in voice channel")





@client.command(pass_context=True)
async def play(ctx, query='Yumi_Matsutoya_-_Haru_yo_koi_-_Kreygasm_RIGHT_VERSION-JPxfAYYo7NA.webm'):
    """Plays a file from the local filesystem"""

    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
    ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('Now playing: {}'.format(query))

@client.command(pass_context=True)
async def andrzej(ctx, query='E:\\discordBotSoundsPanel\\music\\kekw\\a-imie-jego-andrzej-duda-john-cena.mp3'):
    """Plays a AndrzejDuda from the local filesystem"""

    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
    ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send(' :)))) ')


@client.command(pass_context=True)
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Left Channel")
    else:
        await ctx.send("you are not in voice channel")


@client.command(name='play_song', help='To play song')
async def play_song(ctx, url):
    """ Command for playing youtube songs"""
    try:
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=client.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        # await ctx.send('**Now playing:** {}'.format(filename))
    except:
        ctx.send("The bot_l is not connected to a voice channel.")


@client.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        voice_client.pause()
    else:
        ctx.send("The bot_l is not playing anything at the moment.")


@client.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        voice_client.resume()
    else:
        ctx.send("The bot_l was not playing anything before this. Use play_song command")


@client.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        voice_client.stop()
    else:
        ctx.send("The bot_l is not playing anything at the moment.")


@client.command(name='volume', help='Change Volume')
async def volume(ctx, volume):
    if ctx.voice_client:
        await ctx.send(f"Volume changed to: {volume}")
        discord.PCMVolumeTransformer.volume = volume


# discord.opus.load_opus()
# https://discordpy.readthedocs.io/en/stable/api.html#voice-related


def run():
    print("bot_l command run")
    client.run(a.token)


# client.run(a.token)



