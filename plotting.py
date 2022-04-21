import os
import pathlib
from os import listdir
import matplotlib.pyplot as plt
import slab
from tkinter import Tcl



# Getting list of file names
DIR = pathlib.Path(os.getcwd())
file_path = DIR / "uso_1_room-30-30-10/simulated"
file_names = [file_path / f for f in listdir(file_path)]
Tcl().call('lsort', '-dict', file_names)



# Creating slab Objects
sound_files = [slab.Binaural(file_name) for file_name in file_names]


# Creating plot, then saving subplots in a list, so we can iterate through them
_, [[ax1, ax2, ax3, ax4, ax5], [ax6, ax7, ax8, ax9, ax10]] = plt.subplots(
                nrows=2, ncols=5, constrained_layout=True)
ax = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10]

'''
# Looping through slab Objects, plotting the spectrum
for index, sound_file in enumerate(sound_files[0:10]):
    slab.Binaural.spectrum(sound_file, axis=ax[index], show=False)
'''

# Looping through slab Objects, plotting the waveform
for index, sound_file in enumerate(sound_files[0:10]):
    slab.Binaural.waveform(sound_file, axis=ax[index], show=False)


# Creating spectrogram for left
for index, sound_file in enumerate(sound_files[0:10]):
    slab.Binaural.spectrogram(sound_file.left, axis=ax[index], show=False)

# Creating spectrogram for right
for index, sound_file in enumerate(sound_files[0:10]):
    slab.Binaural.spectrogram(sound_file.right, axis=ax[index], show=False)

plt.show()



