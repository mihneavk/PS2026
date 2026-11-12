import numpy as np
import time
import matplotlib.pyplot as plt


def fft(semnal):
    N = len(semnal)
    #caz de baza
    if N <= 1:
        return semnal

    elemente_pare = semnal[0::2]
    elemente_impare = semnal[1::2]

    rezultat_par = fft(elemente_pare)
    rezultat_impar = fft(elemente_impare)

    rez_final = [0] * N

    for k in range(N//2):      #ne trebuie doar n/2 calcule la o etapa pentru a genera n numere
        # P(x) = Par(x^2) + x * Impar(x^2)      X[k] = Par[k] + rotatie(np.exp(-2j * np.pi * k / N)) * Impar[k]
        # P(-x) = Par(x^2) - x * Impar(x^2)     X[k + N/2] = Par[k] - rotatie(np.exp(-2j * np.pi * k / N)) * Impar[k]
        rotatie = np.exp(-2j * np.pi * k / N)
        tmp = rotatie * rezultat_impar[k]
        rez_final[k] = rezultat_par[k] + tmp
        rez_final[k + N//2] = rezultat_par[k] - tmp

    return rez_final



dimensiuni = [128, 256, 512, 1024, 2048, 4096, 8192]
timp_fft, timp_np = [], []


for N in dimensiuni:
    #semnal aleator de lung N
    x = np.random.random(N)
    
    # abominatia mea
    start = time.perf_counter()
    fft(x)
    timp_fft.append(time.perf_counter() - start)
    
    #Numpy FFT
    start = time.perf_counter()
    np.fft.fft(x)
    timp_np.append(time.perf_counter() - start)

# Afișare grafic
plt.figure(figsize=(10, 6))
plt.plot(dimensiuni, timp_fft, marker='s', label='FFT Custom')
plt.plot(dimensiuni, timp_np, marker='^', label='Numpy FFT')

plt.yscale('log')
plt.xlabel('Dimensiunea vectorului (N)')
plt.ylabel('Timpul de execuție (secunde) - Scară Logaritmică')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig('ex1.pdf')
plt.show()