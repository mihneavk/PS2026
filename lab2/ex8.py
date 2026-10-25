import numpy as np
import matplotlib.pyplot as plt


alpha = np.linspace(-np.pi / 2, np.pi / 2, 1000) # 1000 de esnt


sin = np.sin(alpha)
aprox_taylor = alpha
aprox_pade = (alpha - (7 * alpha**3) / 60) / (1 + (alpha**2) / 20)

# calcul erori
err_taylor = np.abs(sin - aprox_taylor)
err_pade = np.abs(sin - aprox_pade)

fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)


axs[0].plot(alpha, sin, label='$\sin(\\alpha)$ exact', color='black', linewidth=2)
axs[0].plot(alpha, aprox_taylor, label='Aproximare Taylor ($\\alpha$)', linestyle='--', color='red')
axs[0].plot(alpha, aprox_pade, label='Aproximare Padé', linestyle=':', color='cyan', linewidth=2)
axs[0].set_title('Comparație: $\sin(\\alpha)$ vs. Taylor vs. Padé')
axs[0].legend()
axs[0].grid(True)


axs[1].plot(alpha, err_taylor, label='Eroare absolută Taylor', color='red')
axs[1].plot(alpha, err_pade, label='Eroare absolută Padé', color='blue')
axs[1].set_title('Eroarea de aproximare (Scară Liniară)')
axs[1].set_ylabel('Eroare absolută')
axs[1].legend()
axs[1].grid(True)


axs[2].semilogy(alpha, err_taylor, label='Eroare absolută Taylor (log)', color='red')
axs[2].semilogy(alpha, err_pade, label='Eroare absolută Padé (log)', color='blue')
axs[2].set_title('Eroarea de aproximare (Scară Logaritmică pe Oy)')
axs[2].set_xlabel('$\\alpha$ [radiani]')
axs[2].set_ylabel('Eroare (log)')
axs[2].legend()
axs[2].grid(True, which="both", ls="-")

plt.tight_layout()
plt.savefig('ex8.pdf')
plt.show()