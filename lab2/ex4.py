import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

sin = np.sin(2 * np.pi * 5 * t)
saw = signal.sawtooth(2 * np.pi * 10 * t)

suma = sin + saw


fig, axs = plt.subplots(3, 1, figsize=(8, 6), sharex=True)
axs[0].plot(t, sin, color='blue')
axs[0].set_title('Semnal 1: Sinusoidal (5 Hz)')
axs[0].grid(True)

axs[1].plot(t, saw, color='green')
axs[1].set_title('Semnal 2: Sawtooth(10 Hz)')
axs[1].grid(True)

axs[2].plot(t, suma, color='purple')
axs[2].set_title('Suma celor două semnale')
axs[2].grid(True)

plt.tight_layout()
plt.savefig('ex4.pdf')
plt.show()