import numpy as np
import matplotlib.pyplot as plt
from pointfixe import pointfixe


def f(x):
    return (x+1)*(x-1)**2


#Question 1 point fixe
def g(x):
    return x - f(x)/5

x0_r1 = -1.5
x0_r2 = 1.5
tol = 1e-6
N = 100

valeurs_r1 = pointfixe(g, x0_r1, N, tol)
valeurs_r2 = pointfixe(g, x0_r2, N, tol)

r1 = valeurs_r1[-1]  # Valeur finale comme approximation de r1
r2 = valeurs_r2[-1]  # Valeur finale comme approximation de r2

# Erreurs
E_r1 = np.abs(np.array(valeurs_r1) - r1)
E_r2 = np.abs(np.array(valeurs_r2) - r2)

# Figure 1 : Erreur en semi-log
plt.figure(1)
plt.semilogy(E_r1, label='Erreur pour r1')
plt.semilogy(E_r2, label='Erreur pour r2')
plt.xlabel("Itération n")
plt.ylabel("Erreur |x_n - r|")
plt.title("Évolution de l'erreur en semi-log")
plt.legend()
print(E_r1[1:])
print(E_r1[:-1])
print(E_r1[1:] / E_r1[:-1])
err = []

# Figure 2 : Rapport des erreurs successives
plt.figure(2)
plt.plot(E_r1[1:] / E_r1[:-1], label='E_n+1 / E_n pour r1')
plt.plot(E_r2[1:] / E_r2[:-1], label='E_n+1 / E_n pour r2')
plt.xlabel("Itération n")
plt.ylabel("E_n+1 / E_n")
plt.title("Rapport des erreurs successives")
plt.legend()

plt.show()


#Question 2 Méthode de Newton

#Question 3 Méthode de Steffenson

