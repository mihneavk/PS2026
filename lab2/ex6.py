import numpy as np
import matplotlib.pyplot as plt

fs = 100 
t = np.arange(0, 20) / fs # doar 20 esant pt viz


x_a = np.sin(2 * np.pi * (fs / 2) * t)
x_b = np.sin(2 * np.pi * (fs / 4) * t)
x_c = np.sin(2 * np.pi * 0 * t)

fig, axs = plt.subplots(3, 1, figsize=(8, 6), sharex=True)
axs[0].stem(t, x_a)
axs[0].set_title('(a) $f = f_s / 2$')
axs[0].set_ylim(-1.2, 1.2)

axs[1].stem(t, x_b)
axs[1].set_title('(b) $f = f_s / 4$')
axs[1].set_ylim(-1.2, 1.2)

axs[2].stem(t, x_c)
axs[2].set_title('(c) $f = 0$ Hz')
axs[2].set_ylim(-1.2, 1.2)

plt.tight_layout()
plt.savefig('ex6.pdf')
plt.show()