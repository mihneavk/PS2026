import numpy as np
import matplotlib.pyplot as plt

N = 8

F = np.zeros((N, N), dtype=complex)
for i in range(N):
    for j in range(N):
        F[i, j] = np.cos(2 * np.pi * i * j / N) - 1j * np.sin(2 * np.pi * i * j / N)


print(F)
F_H = np.conj(F).T
produs = F_H @ F
print(np.round(produs, 3))

este_unitara = np.allclose(produs, N * np.eye(N)) #  --- F^H * F trb sa dea matricea unitate altfel e grav (inm cu N)
print(f"matrice unitara: {este_unitara}")

plt.figure(figsize=(12, 10))
for i in range(N):
    plt.subplot(N, 2, 2*i + 1)
    plt.plot(F[i].real, marker='o', color='b')
    plt.title(f"Linia {i} - Partea Reala")
    
    plt.subplot(N, 2, 2*i + 2)
    plt.plot(F[i].imag, marker='o', color='r')
    plt.title(f"Linia {i} - Partea Imaginara")

plt.tight_layout()
plt.show()