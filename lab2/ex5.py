import numpy as np
import sounddevice as sd

fs = 44100
t = np.linspace(0, 1, fs)


s1 = 0.5 * np.sin(2 * np.pi * 440 * t)
s2 = 0.5 * np.sin(2 * np.pi * 880 * t)


concatenat = np.concatenate((s1, s2))


sd.play(concatenat, fs)
sd.wait()