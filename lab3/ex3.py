import numpy as np
import matplotlib.pyplot as plt

frecv_esant = 1000
timp_v = np.arange(frecv_esant) / frecv_esant

f1_v, f2_v, f3_v = 2, 40, 60
semnal_compus = np.cos(2 * np.pi * f1_v * timp_v) + 2 * np.cos(2 * np.pi * f2_v * timp_v) + 0.5 * np.cos(2 * np.pi * f3_v * timp_v)

omega_rng = np.fft.fftfreq(frecv_esant, d=1/frecv_esant)
X_val = np.abs(np.fft.fft(semnal_compus))

pozitive = omega_rng >= 0
omega_rng_poz = omega_rng[pozitive]
X_val_poz = X_val[pozitive]

fig_3, (ax3_1, ax3_2) = plt.subplots(1, 2, figsize=(12, 5))

ax3_1.plot(np.arange(frecv_esant), semnal_compus, color='olive', linewidth=1)
ax3_1.set_xlabel('Timp (esantioane)')
ax3_1.set_ylabel('x(t)')

ax3_2.stem(omega_rng_poz, X_val_poz, linefmt='b-', markerfmt='bo', basefmt='r-')
ax3_2.set_xlabel('Frecventa (Hz)')
ax3_2.set_ylabel('$|X(\\omega)|$')

plt.tight_layout()
fig_3.savefig('ex3.pdf')
plt.show()