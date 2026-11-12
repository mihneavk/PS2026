import numpy as np
import matplotlib.pyplot as plt

f1, f2, f3 = 10, 22, 34
fs = 100

n = np.arange(0, 0.5, 1/fs)
t_continuu = np.linspace(0, 0.5, 1000)

s1 = np.cos(2 * np.pi * f1 * t_continuu)
s2 = np.cos(2 * np.pi * f2 * t_continuu)
s3 = np.cos(2 * np.pi * f3 * t_continuu)

esantioane1 = np.cos(2 * np.pi * f1 * n)
esantioane2 = np.cos(2 * np.pi * f2 * n)
esantioane3 = np.cos(2 * np.pi * f3 * n)


fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)


axs[0].plot(t_continuu, s1, color='blue', alpha=0.5, label='Semnal 10 Hz')
axs[0].scatter(n, esantioane1, color='blue', marker='o', label='Eșantioane')
axs[0].set_ylabel('Amplitudine')
axs[0].legend(loc='upper right')
axs[0].grid(True)


axs[1].plot(t_continuu, s2, color='orange', alpha=0.5, label='Semnal 22 Hz')
axs[1].scatter(n, esantioane2, color='orange', marker='x', label='Eșantioane')
axs[1].set_ylabel('Amplitudine')
axs[1].legend(loc='upper right')
axs[1].grid(True)


axs[2].plot(t_continuu, s3, color='green', alpha=0.5, label='Semnal 34 Hz')
axs[2].scatter(n, esantioane3, color='green', marker='^', label='Eșantioane')
axs[2].set_xlabel('Timp (s)')
axs[2].set_ylabel('Amplitudine')
axs[2].legend(loc='upper right')
axs[2].grid(True)


plt.tight_layout()

plt.savefig('ex3.pdf')
plt.show()