import numpy as np
import matplotlib.pyplot as plt



# 1 

def x(t):
    return np.cos(520 * np.pi * t + np.pi / 3)

def y(t):
    return np.cos(280 * np.pi * t - np.pi / 3)

def z(t):
    return np.cos(120 * np.pi * t + np.pi / 3)

# (a+b)

# t_inceput = 0
# t_final = 0.03
# pas = 0.0005
# t = np.arange(t_inceput, t_final + pas, pas)

# ---------

# (c) 200 hz

t_inceput = 0
t_final = 1
pas = 0.005
t = np.arange(t_inceput, t_final + pas, pas)

# ----------

val_x = x(t)
val_y = y(t)
val_z = z(t)

fig, ax = plt.subplots(3)
ax[0].plot(t, val_x)
ax[0].stem(t,val_x)
ax[0].set_title('x(t) = cos(520πt + π/3)')
ax[1].plot(t, val_y)
ax[1].stem(t,val_y)
ax[1].set_title('y(t) = cos(280πt - π/3)')
ax[2].plot(t, val_z)
ax[2].stem(t,val_z)
ax[2].set_title('z(t) = cos(120πt + π/3)')

plt.tight_layout()
plt.show()


