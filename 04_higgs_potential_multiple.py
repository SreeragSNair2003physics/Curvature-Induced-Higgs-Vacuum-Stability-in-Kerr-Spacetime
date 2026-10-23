''' I wanted to see the potential valleys when two different lambda parameters are used '''



import numpy as np
import matplotlib.pyplot as plt

# Defining parameters
mu_squared= 1.0

# Setting values for q (squared size of Higgs field); and q>/=0
q= np.linspace(0, 3, 400)

# Calculating the potentials for 2 lambda values
lamda_1= 0.5
lamda_2= 1.0

# Calculating potentials of both cases
V1 = -mu_squared * q + lamda_1 * q**2
V2 = -mu_squared * q + lamda_2 * q**2

# Finding minimum values of both cases
q_min_1 = mu_squared / (2 * lamda_1)
q_min_2 = mu_squared / (2 * lamda_2)

# Finding minimum potentials in both cases
V_min_1 = -mu_squared * q_min_1 + lamda_1 * q_min_1**2
V_min_2 = -mu_squared * q_min_2 + lamda_2 * q_min_2**2

print("for lambda = 0.5:", q_min_1, V_min_1)
print("for lambda = 1.0:", q_min_2, V_min_2)

# Plotting both potentials
plt.figure(figsize=(8, 5))
plt.plot(q, V1, label=r"$\lambda=0.5$")
plt.plot(q, V2, label=r"$\lambda=1.0$")

plt.scatter(q_min_1, V_min_1)
plt.scatter(q_min_2, V_min_2)

plt.xlabel(r"$q = H^\dagger H$")
plt.ylabel(r"$V(q)$ (illustrative units)")
plt.title("Effect of Changing the Potential Parameter")
plt.axhline(0, linewidth=0.8)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("higgs_potential_comparison.png", dpi=300)
plt.show()

