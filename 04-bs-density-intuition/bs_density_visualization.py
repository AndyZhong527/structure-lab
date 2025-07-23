import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(-4, 4, 500)

sigmas = [0.5, 1.0, 1.5]

plt.figure(figsize=(10, 6))

for sigma in sigmas:
    # 对 N(x/σ) / σ 进行绘图
    pdf = norm.pdf(x / sigma) / sigma
    plt.plot(x, pdf, label=f'σ = {sigma}')

plt.title("Standard Normal PDF under Different Volatilities (σ)")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("density_plot.png")  # 可以改为 streamlit 输出或展示
plt.show()
