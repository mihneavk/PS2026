import numpy as np
import matplotlib.pyplot as plt
import scipy
import sounddevice as sd




# cos(a) = sin(a + pi/2)
# semnal periodic - x(t) = A*sin(2*pi*f*t + phi)
A = 1
f= 1
fs = 1000
phi = 0

t = np.linspace(0, 1, fs, endpoint=False)

sin = A * np.sin(2 * np.pi * f * t + phi)
cos = A * np.cos(2 * np.pi * f * t + phi - np.pi / 2)

fig,axs = plt.subplots(2,1)

axs[0].plot(t,sin)
axs[0].set_title('Semnal sinusoidal')

axs[1].plot(t,cos)
axs[1].set_title('Semnal cosinusoidal')

plt.show()