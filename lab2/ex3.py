import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd

#copie lab1 ex2

import numpy as np
import matplotlib.pyplot as plt

fs = 44100 # schimbam frecventa de esantionare la 44100 Hz pentru a putea reda sunetul 

figura, axe = plt.subplots(3, 2, figsize=(15, 12))
figura.tight_layout(pad=5.0) 


# a 400 Hz, 1600 esantioane
frecventaa = 400
esantioanea = 1600
timpa = np.arange(esantioanea) / fs
semnala = np.sin(2 * np.pi * frecventaa * timpa)

axe[0, 0].plot(timpa[:100], semnala[:100]) # afisam primele 100 esant
axe[0, 0].set_title("a) Semnal sinusoidal (400 Hz, 1600 esantioane)")
axe[0, 0].set_xlabel("Timp [s]")
axe[0, 0].set_ylabel("Amplitudine")
axe[0, 0].grid(True)

# b 800 Hz, 3 secunde

frecventab = 800
duratab = 3 # sec
timpb = np.arange(duratab * fs) / fs
semnalb = np.sin(2 * np.pi * frecventab * timpb)

axe[0, 1].plot(timpb[:100], semnalb[:100])
axe[0, 1].set_title("b) Semnal sinusoidal (800 Hz, 3 secunde)")
axe[0, 1].set_xlabel("Timp [s]")
axe[0, 1].set_ylabel("Amplitudine")
axe[0, 1].grid(True)


# c sawtooth 240Hz

frecventac = 240
timpc = np.arange(fs) / fs # generam 1 sec de semnal
semnalc = 2 * np.mod(timpc * frecventac, 1) - 1

axe[1, 0].plot(timpc[:150], semnalc[:150])
axe[1, 0].set_title("c) Semnal Sawtooth (240 Hz)")
axe[1, 0].set_xlabel("Timp [s]")
axe[1, 0].set_ylabel("Amplitudine")
axe[1, 0].grid(True)


# d semnal square 300Hz

frecventad = 300
timpd = np.arange(fs) / fs 
semnald = np.sign(np.sin(2 * np.pi * frecventad * timpd))

axe[1, 1].plot(timpd[:150], semnald[:150])
axe[1, 1].set_title("d) Semnal Square (300 Hz)")
axe[1, 1].set_xlabel("Timp [s]")
axe[1, 1].set_ylabel("Amplitudine")
axe[1, 1].grid(True)

semnale = [
    ("a) Sinus 400 Hz", semnala),
    ("b) Sinus 800 Hz", semnalb),
    ("c) Sawtooth 240 Hz", semnalc),
    ("d) Square 300 Hz", semnald)
]

for nume, semnal in semnale:
    print(f"{nume}")
    sd.play(0.3 * semnal, fs) # am pus 0.3 ca era prea tare sunetul
    sd.wait()


nume_fisier = 'semnal_c_sawtooth.wav'
wav.write(nume_fisier, fs, semnalc.astype(np.float32))

rate_citit, semnal_incarcate = wav.read(nume_fisier)
print(f"Verificare - frecventa :{rate_citit} - numar esantioane: {len(semnal_incarcate)}")
print(np.allclose(semnalc, semnal_incarcate))