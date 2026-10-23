''' I modified my previous map as it wasn't mapping the ergosphere as i intended. This one checks off all the correct bells and whistles. '''




import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import SymLogNorm

a_star = 0.9
r_plus = 1 + np.sqrt(1 - a_star**2)          # outer horizon (M = 1)

r = np.linspace(1.02 * r_plus, 10.0, 400)
theta = np.linspace(0, np.pi, 361)
R, TH = np.meshgrid(r, theta)

c = (a_star * np.cos(TH))**2                 # a^2 cos^2(theta)
K = 48 * (R**6 - 15*R**4*c + 15*R**2*c**2 - c**3) / (R**2 + c)**6

# --- sanity checks ---
K_factored = 48 * (R**2 - c) * ((R**2 + c)**2 - 16*R**2*c) / (R**2 + c)**6
assert np.allclose(K, K_factored)
assert np.all(np.isfinite(K))
K_schw = 48 / R**6                            # a = 0 limit
c_schw = (0.0 * np.cos(TH))**2
K_schw_test = 48 * (R**6 - 15 * R**4 * c_schw + 15 * R**2 * c_schw**2 - c_schw**3) / (R**2 + c_schw)**6

assert np.allclose(K_schw_test, 48 / R**6)
assert np.allclose(48*(R**6)/(R**2 + c_schw)**6, K_schw)

print(f"r_plus = {r_plus:.4f}")
print(f"K range: {K.min():.4f} to {K.max():.4f}")

# --- plot ---
fig, ax = plt.subplots(figsize=(10, 6))
norm = SymLogNorm(linthresh=1e-3, vmin=K.min(), vmax=K.max())
im = ax.pcolormesh(R, TH, K, shading="auto", cmap="RdBu_r", norm=norm)

ax.contour(R, TH, K, levels=[0], colors="k", linewidths=1)   # K = 0
r_ergo = 1 + np.sqrt(1 - (a_star * np.cos(theta))**2)        # ergosphere
ax.plot(r_ergo, theta, "w--", lw=1, label="ergosphere/outer static limit")

ax.set_yticks([0, np.pi/2, np.pi])
ax.set_yticklabels(["0", r"$\pi/2$", r"$\pi$"])
ax.set_xlabel(r"Dimensionless radius, $r/M$")
ax.set_ylabel(r"Polar angle, $\theta$")
ax.set_title(fr"Kerr Kretschmann scalar ($a_*={a_star}$)")
ax.legend(loc="upper right")
fig.colorbar(im, label=r"$M^4 K$ (symlog scale)")

fig.tight_layout()
fig.savefig("kerr_kretschmann_map.png", dpi=300)
plt.show()
