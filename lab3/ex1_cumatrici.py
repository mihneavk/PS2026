import numpy as np
import matplotlib.pyplot as plt

N = 8

linie = np.arange(N)
# print(linie)
linie = linie.reshape(1,N) #       :'(
coloana = linie.reshape(N,1)
# print(coloana)

matrice_i_j = np.dot(coloana,linie)
# print(matrice_i_j)
matrice_putere = matrice_i_j * (-2 * np.pi * 1j / N)
# print(matrice_putere)

F = np.exp(matrice_putere)
# print(F)

F_H = np.conj(F).T
produs = F_H @ F

print(np.round(produs, 3))

este_unitara = np.allclose(produs, N * np.eye(N))
print(f"{este_unitara}")
