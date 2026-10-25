import numpy as np
import matplotlib.pyplot as plt
import scipy
import sounddevice as sd




# cos(a) = sin(a + pi/2)
# semnal periodic - x(t) = A*sin(2*pi*f*t + phi)
A = 1
f= 5
fs = 1000
phi = [0, np.pi/4, np.pi/2, 3 * np.pi / 4]

t = np.linspace(0, 1, fs,endpoint=False)

for i in phi:
    x = A * np.sin(2 * np.pi * f * t + i)
    plt.plot(t, x, label=f'phi = {i:.2f} rad')

plt.title('Semnale sinusoidale cu faze diferite')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.legend()
plt.show()


# adaugare zgomot

original = np.sin(2 * np.pi * f * t)

z = np.random.normal(0, 1, len(original)) # zgomot gaussian

SNR = [0.1, 1, 10, 100]

normaX = np.linalg.norm(original)
normaZ = np.linalg.norm(z)

fig, axs = plt.subplots(len(SNR), 1, figsize=(10, 8))

for i in range(len(SNR)):
    s = SNR[i]
    gamma = normaX / (normaZ * np.sqrt(s))
    x_zgomot = original + gamma * z
    axs[i].plot(t, x_zgomot, label=f'SNR = {s}')
    axs[i].plot(t, original, label='Semnal original', linestyle='--')
    axs[i].legend()
    axs[i].grid()

plt.show()
