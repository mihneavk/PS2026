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


plt.figure(figsize=(12, 4))
plt.plot(f, X_half)
plt.yscale('log')
plt.title('Modulul Transformatei Fourier')
plt.xlabel('Frecvența (Hz)')
plt.ylabel('|X(f)|')
plt.grid(True)
plt.savefig("d.pdf")
plt.show()


#e
x_med = x - np.mean(x)
X_cent = np.abs(np.fft.fft(x_med))[:half]

plt.figure(figsize=(12, 4))
plt.plot(f, X_cent)
plt.yscale('log')
plt.title('Modulul Transformatei Fourier -componenta continua')
plt.xlabel('Frecvența (Hz)')
plt.ylabel('|X(f)|')
plt.grid(True)
plt.savefig("e.pdf")
plt.show()


#f
top4 = np.argsort(X_cent)[-4:][::-1]

for i in top4:
    frecv = f[i]
    perioada = (1 / frecv) / 3600
    print(f"Frecventa: {frecv:.8f} Hz | Amplitudine: {X_cent[i]:.2f} | Perioada: {perioada:.2f} ore ({perioada/24:.2f} zile)")


# Frecventa: 0.00000002 Hz | Amplitudine: 1222623.35 | Perioada: 18288.00 ore (762.00 zile)  - trendul gneral de crestere
# Frecventa: 0.00000003 Hz | Amplitudine: 644088.24 | Perioada: 9144.00 ore (381.00 zile)    -  ciclul anual
# Frecventa: 0.00001157 Hz | Amplitudine: 495641.78 | Perioada: 24.00 ore (1.00 zile)        - ciclul zilnic
# Frecventa: 0.00000005 Hz | Amplitudine: 461221.83 | Perioada: 6096.00 ore (254.00 zile)    - are o frecventa foarte joasa deci probabil este un sinus care aproximeaza ceva cresteri bruste

#g
start_luni = 1056 #prima luni dupa la 1000lea esantion, ora 0000
durata_luna = 30 * 24

plt.figure(figsize=(14, 4))
plt.plot(np.arange(start_luni, start_luni + durata_luna), x[start_luni : start_luni + durata_luna])
plt.title('Traficul pe durata unei luni')
plt.xlabel('Eșantion (ore)')
plt.ylabel('Numar masini')
plt.grid(True)
plt.savefig("g.pdf")
plt.show()

#h

# Putem face media a 24 de esantioane pentru a avea o zi si facem asta pentru toate esantioanele noastre pe care vrem sa le punem in timp
# si o sa ramanem cu un vector de zile cu media de masini pe zi, apoi putem sa presupunem unele lucruri ca ne dam cu parerea unde suntem
#1. in weekend sunt mai putine masini ca nu se merge la servici si nici la scoala 2. poate facem si o media a esantioanelor dora la ore tarzii ex:22-06, pentru ca oamenii se duc la petreceri cand nu au servici a doua zi si asa poate am vedea zilele de vineri si sambata cu mai multa activitate pe graf
# lucrul asta are toate problemele, am facut niste presupuneri care tin clar de orasul in care esti si in primul rand SA TE AFLI INTR UN ORAS, daca sunt date de pe dn1, atunci toate presupunerile pica, daca e o autostrada probabil ziua de marti e cel mai liber si in weekend e full.