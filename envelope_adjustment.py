import pathlib
import slab
from os import listdir
import os
import random


DIR = pathlib.Path(os.getcwd())
file_path = DIR / "uso_500ms"
file_names = [file_path / f for f in listdir(file_path)]

sound_files = [slab.Binaural(file_name) for file_name in file_names]
bum = slab.Binaural("AW_A_bum_room-10-30-3_control.wav")
env = bum.envelope()
env = env[:, 0]


uso_sounds = [sound_files[i].envelope(apply_envelope=env) for i in range(len(sound_files))]
random.choice(uso_sounds).play()


# slab.Sound("Rconst_Oconst.wav").waveform(start=0, end=48000)
