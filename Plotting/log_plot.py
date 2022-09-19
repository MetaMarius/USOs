from matplotlib import pyplot as plt, lines
import numpy as np
from math import log10
from math import log2
import slab
import os
import pathlib
from matplotlib.patches import Rectangle





# create linear plot

x = list(range(1, 2502))
y = list(range(0, 2501))
fig_lin, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(x, y)  # Plot data on the axes.
ax.set_ylabel('Distances [cm]')  # Add a y-label to the axes
ax.set_xlabel('Distances ordered linear')
ax.set_title('Distance Category')
secax = ax.secondary_xaxis('top')
secax.set_xticks([0, 20, 40, 60, 80, 100], ['0', '1', '2', '3', '4', '5'])
plt.locator_params(axis='both', nbins=40)
ax.add_artist(lines.Line2D([0, 0], [0, 2000], color='r'))
ax.add_artist(lines.Line2D([20, 20], [0, 2000], color='r'))
ax.add_artist(lines.Line2D([40, 40], [0, 2000], color='r'))
ax.add_artist(lines.Line2D([60, 60], [0, 2000], color='r'))
ax.add_artist(lines.Line2D([80, 80], [0, 2000], color='r'))
ax.add_artist(lines.Line2D([100, 100], [0, 2000], color='r'))
ax.grid(True)
rect_1 = Rectangle((5, 100), 10, 200)
rect_2 = Rectangle((25, 500), 10, 200)
rect_3 = Rectangle((45, 900), 10, 200)
rect_4 = Rectangle((65, 1300), 10, 200)
rect_5 = Rectangle((85, 1700), 10, 200)
plt.gca().add_patch(rect_1)
plt.gca().add_patch(rect_2)
plt.gca().add_patch(rect_3)
plt.gca().add_patch(rect_4)
plt.gca().add_patch(rect_5)

# create log plot
y = list(range(0, 2001))
x_for_log = np.arange(1, 101.05, 0.05)
log_x = [log10(i) for i in x_for_log]
fig_log, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(log_x, y)  # Plot data on the axes.

ax.set_ylabel('Distances [cm]')  # Add a y-label to the axes
ax.set_xlabel('Distances ordered logarithmically')
ax.set_title('Distance Category')
secax = ax.secondary_xaxis('top')
secax.set_xticks([0, log10(20), log10(40), log10(60), log10(80), 2], ['0', '1', '2', '3', '4', '5'])
ax.grid(True)
plt.locator_params(axis='both', nbins=40)
ax.add_artist(lines.Line2D([0, 0], [0, 2000], color='r'))
ax.add_artist(lines.Line2D([log10(20), log10(20)], [0, 2000], color='r'))
ax.add_artist(lines.Line2D([log10(40), log10(40)], [0, 2000], color='r'))
ax.add_artist(lines.Line2D([log10(60), log10(60)], [0, 2000], color='r'))
ax.add_artist(lines.Line2D([log10(80), log10(80)], [0, 2000], color='r'))
ax.add_artist(lines.Line2D([2.0, 2.0], [0, 2000], color='r'))

ax.add_artist(lines.Line2D([0.1, 0.3], [100, 100], color='g'))
ax.add_artist(lines.Line2D([0.5, 0.7], [200, 200], color='g'))
ax.add_artist(lines.Line2D([0.9, 1.1], [300, 300], color='g'))
ax.add_artist(lines.Line2D([1.3, 1.5], [700, 700], color='g'))
ax.add_artist(lines.Line2D([1.7, 1.9], [1700, 1700], color='g'))





# logarithmic way of selecting distances #

# follwing files would be chosen as base sounds for the distinct categories -> 2/5 = 0.4 -> every 0.4
DIR = pathlib.Path(os.getcwd())
sound_file_path = DIR / "data" / "distance_simulation"/ "300ms_normalised" / "N_uso_300ms_5_room-30-30-10"
control_sound = slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_control.wav")

# dis 1 , x = ~0.4
dis_1_log = slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_dist-40.wav")
# dis 2, x = ~0.8
dis_2_log = slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_dist-120.wav")
# dis 3, x = ~1.2
dis_3_log = slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_dist-300.wav")
# dis_4, x = ~1.6
dis_4_log = slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_dist-780.wav")
# dis_5, x = 2
dis_5_log = slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_dist-2000.wav")

# distances based on log-scale
control_sound.play()
dis_1_log.play()
dis_2_log.play()
dis_3_log.play()
dis_4_log.play()
dis_5_log.play()

# distances based on linear scale
dis_1_lin = slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_dist-20.wav")
dis_2_lin = slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_dist-500.wav")
dis_3_lin = slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_dist-1000.wav")
dis_4_lin = slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_dist-1500.wav")
dis_5_lin = slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_dist-2000.wav")

control_sound.play()
dis_1_lin.play()
dis_2_lin.play()
dis_3_lin.play()
dis_4_lin.play()
dis_5_lin.play()

# new logarithmic scale based on this:
np.logspace(log10(20), log10(2000), 5)

dist_new = [slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_dist-20.wav"),
            slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_dist-60.wav"),
            slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_dist-200.wav"),
            slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_dist-620.wav"),
            slab.Sound(sound_file_path / "N_uso_300ms_5_room-30-30-10_dist-2000.wav")]

for stimulus in dist_new:
    stimulus.play()


