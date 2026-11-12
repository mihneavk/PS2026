import numpy as np
import matplotlib.pyplot as plt

f1, f2, f3 = 10, 22, 34 #frecv sinusurilor

fs = 12 # frecv esant    fs < 2*f = sub-Nyquist

t_continuu = np.linspace(0, 0.5, 1000)

n = np.arange(0, 0.5, 1/fs) # esantioanele

s1 = np.cos(2 * np.pi * f1 * t_continuu)
s2 = np.cos(2 * np.pi * f2 * t_continuu)
s3 = np.cos(2 * np.pi * f3 * t_continuu)

esantioane = np.cos(2 * np.pi * f1 * n)


fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

axs[0].plot(t_continuu, s1, label='Semnal 10 Hz', color='blue')
axs[0].scatter(n, esantioane, color='red', zorder=5, label='Esantioane')
axs[0].set_ylabel('Amplitudine')
axs[0].legend(loc='upper right')
axs[0].grid(True)

axs[1].plot(t_continuu, s2, label='Semnal 22 Hz', color='purple')
axs[1].scatter(n, esantioane, color='red', zorder=5, label='Esantioane')
axs[1].set_ylabel('Amplitudine')
axs[1].legend(loc='upper right')
axs[1].grid(True)

axs[2].plot(t_continuu, s3, label='Semnal 34 Hz', color='green')
axs[2].scatter(n, esantioane, color='red', zorder=5, label='Esantioane')
axs[2].set_xlabel('Timp (s)')
axs[2].set_ylabel('Amplitudine')
axs[2].legend(loc='upper right')
axs[2].grid(True)

plt.tight_layout()

plt.savefig('ex2.pdf')
plt.show()