import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs_audio, semnal = wavfile.read('aeiou.wav')

N = len(semnal)


window_size = int(0.01 * N)
step = int(window_size * 0.5)

spectrograma = []

for i in range(0, N - window_size, step):
    s = semnal[i : i + window_size]
    
    
    fft = np.fft.fft(s)
    
    # ne intereseaza doar prima jum, ca dupa e acs informatie dar conjugata
    abs_fft = np.abs(fft[:window_size // 2])
    
    spectrograma.append(abs_fft)



# facem transpusa ca sa fie timpul pe orizontala si frecventa pe verticala
spectrogram_matrix = np.array(spectrograma).T


# trandformam in scara logaritmica - in decibeli. inmultim cu 10 pt ca asta e formula din energie in decibeli
spectrogram_matrix_db = 10 * np.log10(spectrogram_matrix + 1e-10) # mai adaugam ceva nesemn ca sa lu fie log0

plt.figure(figsize=(12, 6))

durata_totala = N / fs_audio 

plt.imshow(spectrogram_matrix_db, aspect='auto', origin='lower', cmap='inferno',
           extent=[0, durata_totala, 0, fs_audio / 2])

plt.title('Spectrograma vocalelor')
plt.xlabel('Timp (secunde)')
plt.ylabel('Frecvență (Hz)')
plt.colorbar(format='%+2.0f dB', label='Magnitudine (dB)')
plt.ylim(0, 5000)

plt.savefig('ex6.pdf')
plt.show()