import numpy as np
import matplotlib.pyplot as plt

f = 1000 

figura, axe = plt.subplots(3, 2, figsize=(15, 12))
figura.tight_layout(pad=5.0) 


# a 400 Hz, 1600 esantioane
frecventaa = 400
esantioanea = 1600
timpa = np.arange(esantioanea) / f
semnala = np.sin(2 * np.pi * frecventaa * timpa)

axe[0, 0].plot(timpa[:100], semnala[:100]) # afisam primele 100 esant
axe[0, 0].set_title("a) Semnal sinusoidal (400 Hz, 1600 esantioane)")
axe[0, 0].set_xlabel("Timp [s]")
axe[0, 0].set_ylabel("Amplitudine")
axe[0, 0].grid(True)

# b 800 Hz, 3 secunde

frecventab = 800
duratab = 3 # sec
timpb = np.arange(duratab * f) / f
semnalb = np.sin(2 * np.pi * frecventab * timpb)

axe[0, 1].plot(timpb[:100], semnalb[:100])
axe[0, 1].set_title("b) Semnal sinusoidal (800 Hz, 3 secunde)")
axe[0, 1].set_xlabel("Timp [s]")
axe[0, 1].set_ylabel("Amplitudine")
axe[0, 1].grid(True)


# c sawtooth 240Hz

frecventac = 240
timpc = np.arange(f) / f # generam 1 sec de semnal
semnalc = 2 * np.mod(timpc * frecventac, 1) - 1

axe[1, 0].plot(timpc[:150], semnalc[:150])
axe[1, 0].set_title("c) Semnal Sawtooth (240 Hz)")
axe[1, 0].set_xlabel("Timp [s]")
axe[1, 0].set_ylabel("Amplitudine")
axe[1, 0].grid(True)


# d semnal square 300Hz

frecventad = 300
timpd = np.arange(f) / f 
semnald = np.sign(np.sin(2 * np.pi * frecventad * timpd))

axe[1, 1].plot(timpd[:150], semnald[:150])
axe[1, 1].set_title("d) Semnal Square (300 Hz)")
axe[1, 1].set_xlabel("Timp [s]")
axe[1, 1].set_ylabel("Amplitudine")
axe[1, 1].grid(True)


# e semnal 2d aleator 128x128

semnale = np.random.rand(128, 128)

imaginee = axe[2, 0].imshow(semnale, cmap='viridis')
axe[2, 0].set_title("e) Semnal 2D aleator (128x128)")
figura.colorbar(imaginee, ax=axe[2, 0])

# f semnal 2d la alegere

semnalf = np.zeros((128, 128))
semnalf[32:96, 32:96] = np.ones((64, 64))

imaginef = axe[2, 1].imshow(semnalf, cmap='gray')
axe[2, 1].set_title("f) Semnal 2D la alegere")
figura.colorbar(imaginef, ax=axe[2, 1])

plt.show()