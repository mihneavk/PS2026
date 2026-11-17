import numpy as np
import matplotlib.pyplot as plt

# usecols=2 ca sa luam doar valoarea esantionului
x = np.genfromtxt('Train.csv', delimiter=',', skip_header=1, usecols=2)

N = len(x)
fs = 1 / 3600 # o ora

#d
X = np.fft.fft(x)
X_abs = np.abs(X)


half = N // 2
X_half = X_abs[:half]

# Vectorul de frecvențe în Hz
f = np.arange(half) * fs / N

X = np.fft.fft(x)

frecv = np.fft.fftfreq(N, d=3600)  # ca "f = np.arange(half) * fs / N" dar face si partea a 2 a a vectorului, care are frecventele negative ale primei parti

fc = 2.5e-5 #0.000025Hz

X[np.abs(frecv) > fc] = 0 # stergem frecv mai mari decat fc (mai des decat odata la 11 ore)

x_filtrat = np.real(np.fft.ifft(X)) # folosim .real ca mai ramane din erori de calcul si o frimitura de parte complexa

plt.figure(figsize=(14, 5))
plt.plot(x, label='Semnalul brut', alpha=0.6)
plt.plot(x_filtrat, label='Semnalul filtrat (trece-jos, fc = 2.5e-5 Hz)', linewidth=2, color='orange')
plt.title('Compararea semnalului brut cu semnalul filtrat')
plt.xlabel('Eșantioane (ore)')
plt.ylabel('Număr mașini')
plt.legend()
plt.grid(True)
plt.savefig("i.pdf")
plt.show()