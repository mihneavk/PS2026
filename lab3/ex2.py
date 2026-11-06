import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

nr_pct = 1000
n_v = np.arange(nr_pct)
f_sem = 15
s_x = np.sin(2 * np.pi * f_sem * n_v / nr_pct)

nr_s = 620
f_inf = 1
s_y = s_x * np.exp(-2 * np.pi * 1j * f_inf * n_v / nr_pct)

fig_1, (ax_1, ax_2) = plt.subplots(1, 2, figsize=(12, 5))
ax_1.plot(n_v, s_x, color='olive', linewidth=1)
ax_1.axhline(0, color='black', linewidth=0.8)
ax_1.plot(nr_s, s_x[nr_s], 'ro')
ax_1.plot([nr_s, nr_s], [0, s_x[nr_s]], 'r-')
ax_1.set_xlabel('Timp (esantioane)')
ax_1.set_ylabel('Amplitudine')
ax_1.set_xlim(0, nr_pct)
ax_1.set_ylim(-1.2, 1.2)

ax_2.plot(np.real(s_y), np.imag(s_y), color='blue', linewidth=0.8)
ax_2.axhline(0, color='black', linewidth=0.8)
ax_2.axvline(0, color='black', linewidth=0.8)
ax_2.plot([0, np.real(s_y[nr_s])], [0, np.imag(s_y[nr_s])], 'r-')
ax_2.plot(np.real(s_y[nr_s]), np.imag(s_y[nr_s]), 'ro')
ax_2.set_xlabel('Real')
ax_2.set_ylabel('Imaginar')
ax_2.set_xlim(-1.1, 1.1)
ax_2.set_ylim(-1.1, 1.1)
plt.tight_layout()
fig_1.savefig('ex2_1.pdf')
plt.show()

omega_lista = [1, 2, 5, 7]
fig_2, axes_lista = plt.subplots(2, 2, figsize=(10, 10))
axes_lista = axes_lista.flatten()

for idx_v, omega_v in enumerate(omega_lista):
    z_v = s_x * np.exp(-2 * np.pi * 1j * omega_v * n_v / nr_pct)
    axes_lista[idx_v].plot(np.real(z_v), np.imag(z_v), color='purple', linewidth=0.8)
    axes_lista[idx_v].axhline(0, color='black', linewidth=0.8)
    axes_lista[idx_v].axvline(0, color='black', linewidth=0.8)
    axes_lista[idx_v].set_title(f'$\\omega = {omega_v}$')
    axes_lista[idx_v].set_xlabel('Real')
    axes_lista[idx_v].set_ylabel('Imaginar')
    axes_lista[idx_v].set_xlim(-1.1, 1.1)
    axes_lista[idx_v].set_ylim(-1.1, 1.1)

plt.tight_layout()
fig_2.savefig('ex2_2.pdf')
plt.show()

fig_a, ax_a = plt.subplots(figsize=(6, 6))
ax_a.set_xlim(-1.2, 1.2)
ax_a.set_ylim(-1.2, 1.2)
ax_a.axhline(0, color='black', linewidth=0.8)
ax_a.axvline(0, color='black', linewidth=0.8)

omega_anim = 1
z_anim = s_x * np.exp(-2 * np.pi * 1j * omega_anim * n_v / nr_pct)

line_an, = ax_a.plot([], [], color='purple', linewidth=0.8)
p_an, = ax_a.plot([], [], 'ro', markersize=8)

def init_f():
    line_an.set_data([], [])
    p_an.set_data([], [])
    return line_an, p_an

def upd_f(fr_v):
    line_an.set_data(np.real(z_anim[:fr_v]), np.imag(z_anim[:fr_v]))
    p_an.set_data([np.real(z_anim[fr_v-1])], [np.imag(z_anim[fr_v-1])])
    return line_an, p_an

ani_v = FuncAnimation(fig_a, upd_f, frames=range(1, nr_pct, 10), init_func=init_f, blit=True, interval=20)
plt.show()