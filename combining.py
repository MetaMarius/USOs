import slab
from loading import load


sound1 = load("bank")
sound2 = load("bowl")
silence = slab.Sound.silence(0.5, 48000)
print(sound1)
print(sound2)
print(silence)
stimulus = slab.Sound.sequence(sound1 + silence + sound2)
stimulus.play()
