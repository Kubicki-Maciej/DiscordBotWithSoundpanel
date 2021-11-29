import pygame as pg
import time
from bot import client, play_music_from_sound_panel
song_path = None


class SoundsPlayer:

    freq = 44100  # audio CD quality
    bitsize = -16  # unsigned 16 bit
    channels = 2  # 1 is mono, 2 is stereo
    buffer = 2048  # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)

    def __init__(self):

        self.file_path_playing = None
        self.volume = 0.8
        self.client = None

    def discord_play_file(self):
        print('discord play file')
        channel_id = 878208349710196770
        path = self.file_path_playing

        tic = time.perf_counter()
        # add here function/command with play sound on discord
        client.loop.create_task(play_music_from_sound_panel(path, tic))
        # print("say hi")
        # client.loop.create_task(hellotest(tic))
        # client.command(hellotest(tic))

        # channel_id = client.chann

        # channel = client.get_channel(id)

    def load_file(self, file_path):

        try:
            pg.mixer.music.load(file_path)
            # print("Music file {} loaded!".format(file_path))
            self.file_path_playing = file_path
            global song_path
            song_path = file_path
            print(song_path)
        except pg.error:
            print("File {} not found! ({})".format(file_path, pg.get_error()))

    def play_sound(self):
        pg.mixer_music.play()

    def stop_play(self):
        pg.mixer_music.stop()

    def play_fade_out(self):
        pg.mixer_music.fadeout()

    def rewind(self):
        pg.mixer_music.rewind()

    def change_volume(self):
        pg.mixer_music.set_volume(self.volume)

    def return_path(self):
        return self.file_path_playing


player_obj = SoundsPlayer()


def test():
    player_obj.load_file('Joke.wav')
    player_obj.play_sound()