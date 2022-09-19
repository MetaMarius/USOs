import slab
import pathlib
import os
from os import listdir
import random
import copy
from datetime import datetime
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy
slab.set_default_samplerate(44100)
DIR = pathlib.Path(os.getcwd())
folder_path = DIR / 'data' / 'final_uso_selection'
file_paths = [folder_path / f for f in listdir(folder_path)]
both = [1, 2, 3, 4, 5, 4, 3, 2, 1]
away = [1, 2, 3, 4, 5]
toward = [5, 4, 3, 2, 1]
sound_IDs = [2, 3, 5, 7, 10, 11, 14, 17, 18, 19, 20, 21, 22, 25, 27, 28]

log = {
    1: [20],
    2: [67],
    3: [224],
    4: [748],
    5: [2500]
}

var_1 = {
    1: [20],
    2: [120],
    3: [420],
    4: [1100],
    5: [2500]
}

var_2 = {
    1: [20],
    2: [220],
    3: [600],
    4: [1400],
    5: [2500]

}


def training(uso, distance_groups, isi=1.0, order=both):
    training_sequence = slab.Trialsequence(conditions=[1, 2, 3, 4, 5], trials=order)
    for group in training_sequence:
        distance = random.choice(distance_groups[group])
        if uso == 'random':
            file_name = "N_uso_300ms_" + str(random.choice(sound_IDs)) + "_room-10-35-3_dist-" + str(distance) + ".wav"
        else:
            file_name = "N_uso_300ms_" + str(uso) + "_room-10-35-3_dist-" + str(distance) + ".wav"
        sound = slab.Sound(folder_path / file_name)
        out = copy.deepcopy(sound)
        out.data = out.data[:slab.Sound.in_samples(isi, 44100)]
        print(file_name)
        out = out.ramp(duration=0.01)
        out.play()


def experiment(distance_groups, category='', uso='random', name='', isi=1.0, n_reps=1):
    right_answers = 0
    experiment_sequence = slab.Trialsequence(conditions=[1, 2, 3, 4, 5], n_reps=n_reps, kind="random_permutation")
    for group in experiment_sequence:
        distance = random.choice(distance_groups[group])
        if uso == 'random':
            file_name = "N_uso_300ms_" + str(random.choice(sound_IDs)) + "_room-10-35-3_dist-" + str(distance) + ".wav"
        else:
            file_name = "N_uso_300ms_" + str(uso) + "_room-10-35-3_dist-" + str(distance) + ".wav"
        sound = slab.Sound(folder_path / file_name)
        out = copy.deepcopy(sound)
        out.data = out.data[:slab.Sound.in_samples(isi, 44100)]
        print(file_name)
        out = out.ramp(duration=0.01)
        out.play()
        answer = int(input('Which distance group was played? -> '))
        experiment_sequence.add_response(experiment_sequence.this_trial)
        experiment_sequence.add_response(answer)
        if experiment_sequence.this_trial == answer:
            right_or_wrong = 1
            right_answers += 1
        else:
            right_or_wrong = 0
        experiment_sequence.add_response(right_or_wrong)

    results_file = slab.ResultsFile(subject=category, folder="Confusion_Matrix/Results")
    today = datetime.now()
    results_file.write(name, tag='Name')
    results_file.write(today.strftime('%Y/%m/%d'), tag='Date')
    results_file.write(today.strftime('%H:%M:%S'), tag='Time')
    results_file.write(category, tag='Category')
    results_file.write(distance_groups, tag="Distances")
    results_file.write(uso, tag='USO')
    results_file.write(experiment_sequence, tag='Trial')
    print(str(right_answers) + "/" + str(experiment_sequence.n_trials))
    print("Finished")
    return results_file


# create confusion matrix #
# extract data
results_folder_path = DIR / "Results" / 'Test'
results_file_paths = [results_folder_path / f for f in listdir(results_folder_path)]
data = [slab.ResultsFile.read_file(results_file_paths[i], tag="Trial") for i in range(len(results_file_paths))]
actual = []
given = []
trial_data = [data[i]["data"] for i in range(len(data))]
for rounds in trial_data:
    for trials in rounds:
        actual.append(trials[0])
for rounds in trial_data:
    for trials in rounds:
        given.append(trials[1])

# create matrix and plot data
c_matrix = metrics.confusion_matrix(actual, given)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=c_matrix, display_labels=[1, 2, 3, 4, 5])
print(c_matrix)
cm_display.plot()
plt.show()
print(metrics.accuracy_score(actual, given))

