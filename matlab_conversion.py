import random
import slab
import os
from os import listdir
import pathlib
from os.path import isfile, join
from random import randrange
import copy

slab.set_default_samplerate(48000)

DIR = pathlib.Path(os.getcwd())                             # getting the current working directory

file_path = DIR / 'mitsubishi_wavs'                         # setting absolute path

file_names = [file_path / f for f in listdir(file_path)     # creating list of all file names
                  if isfile(join(file_path, f))
                  and not f.startswith('.')
                  and f.endswith('.wav')]

file_names.sort()

sound_files = [slab.Binaural(file_names[randrange(0, len(file_names))]) for i in range(0, 6)]  # creating 6 slab objects

output = slab.Binaural.silence(duration=1)                  # Is this step necessary? If yes, why?

for sound_file in sound_files:
    snippet = copy.deepcopy(sound_file)                     # defines one sound file after the other as snippet
    sound_length = len(sound_file)                          # Defining variable to get length of the sound file
    min = int(0.02 * 48000)                                 # defining min snippet length
    max = int(0.2 * 48000)                                  # defining max snippet length
    snippet_length = random.randrange(min, max)             # Defining variable to set a random snippet length, max 9600 min 960 samples
    offset = random.randrange(0, sound_length - snippet_length)   # creating random starting point (=offset) for the snippet
    snippet_length = slab.Signal.in_samples(snippet_length, sound_file.samplerate)   # Transforms snippet length from just an integer to an slab object, that slab can understand as a length in samples
    offset = slab.Signal.in_samples(offset, sound_file.samplerate)         # Same as above: defining offset as a length in samples in slab
    snippet.data = sound_file.data[offset:offset + snippet_length]   # creating the actual snippet by calling the .data object and intializing the length from offset to random snippet length
    output = slab.Binaural.sequence(output, snippet)                 # 1 sample of silence in every stimulus

output.play()

output.write("uso_ran_snippets_40.wav")
