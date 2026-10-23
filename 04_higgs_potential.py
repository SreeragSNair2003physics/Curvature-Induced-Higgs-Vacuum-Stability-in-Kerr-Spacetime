''' Rudimentary code for testing potential landscape code reproduction '''


import numpy as np
import matplotlib.pyplot as plt

# Defining parameters
mu_squared= 1.0
lamda= 1.0

# Setting values for q (squared size of Higgs field); and q>/=0
q= np.linspace(0, 3, 400)

# Calculating the potential energy density of Higgs field
V= -mu_squared * q + lamda * q**2

# Finding the minimum by setting first derivative to zero
q_min= mu_squared / (2 * lamda)

# Finding potential at the minimum value
V_min= -mu_squared * q_min + lamda * q_min**2



print("Location of minimum:", q_min)
print("Potential at minimum:", V_min)

# Plotting the potential landscape
plt.figure(figsize=(8, 5))
plt.plot(q, V, label="Higgs potential")
plt.scatter(q_min, V_min, label="Minimum")
plt.xlabel(r"$q = H^\dagger H$")
plt.ylabel(r"$V(q)$ (illustrative units)")
plt.title("Simplified Higgs Potential")
plt.axhline(0, linewidth=0.8)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("higgs_potential.png", dpi=300)
plt.show()
