import numpy as np
import matplotlib.pyplot as plt

fs = 1000
f = 50
t = np.linspace(0, 0.04, int(0.04 * fs), endpoint=False)
x = np.sin(2 * np.pi * f * t)


t_dec_a = t[::4]
x_dec_a = x[::4]


t_dec_b = t[1::4]
x_dec_b = x[1::4]

plt.figure(figsize=(9, 5))
plt.plot(t, x, label='Semnal inițial ($f_s = 1000$ Hz)', color='lightgray', marker='o')
plt.plot(t_dec_a, x_dec_a, label='(a) Decimat de la index 0 ($f_s = 250$ Hz)', color='blue', marker='s')
plt.plot(t_dec_b, x_dec_b, label='(b) Decimat de la index 1 ($f_s = 250$ Hz)', color='red', linestyle='--', marker='^')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.legend()
plt.grid(True)
plt.savefig('ex7.pdf')
plt.show()