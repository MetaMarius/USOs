import slab
import os
from os import listdir
import pathlib
from os.path import isfile, join
from random import randrange

slab.set_default_samplerate(48000)

DIR = pathlib.Path(os.getcwd())

file_path = DIR / 'mitsubishi_wavs'

file_names = [file_path / f for f in listdir(file_path)
                  if isfile(join(file_path, f))
                  and not f.startswith('.')
                  and f.endswith('.wav')]

file_names.sort()

sound_files = [slab.Sound(file_names[randrange(0, len(file_names))]) for i in range(0, 6)]
