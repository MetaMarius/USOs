import random
import slab
import os
from os import listdir
import pathlib
from os.path import isfile, join
from random import randrange
import copy

slab.set_default_samplerate(48000)

DIR = pathlib.Path(os.getcwd())

file_path = DIR / 'mitsubishi_wavs'

file_names = [file_path / f for f in listdir(file_path)
                  if isfile(join(file_path, f))
                  and not f.startswith('.')
                  and f.endswith('.wav')]

file_names.sort()

sound_files = [slab.Binaural(file_names[randrange(0, len(file_names))]) for i in range(0, 6)]

output = slab.Binaural.silence(duration=1)

for sound_file in sound_files:
    snippet = copy.deepcopy(sound_file)
    sound_length = len(sound_file)
    min = int(0.02 * 48000)
    max = int(0.2 * 48000)
    snippet_length = random.randrange(min, max)
    offset = random.randrange(0, sound_length - snippet_length)
    snippet_length = slab.Signal.in_samples(snippet_length, sound_file.samplerate)
    offset = slab.Signal.in_samples(offset, sound_file.samplerate)
    snippet.data = sound_file.data[offset:offset + snippet_length]
    output = slab.Binaural.sequence(output, snippet)

output.play()