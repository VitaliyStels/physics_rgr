import numpy as np
import matplotlib.pyplot as plt


epsilon_0 = 8.854e-12  # Ф/м, електрична проникність вакууму

sigma1 = 1e-9  # Кл/м²
sigma2 = -2e-9  # Кл/м²

E_left = (sigma1 / (2 * epsilon_0)) - (sigma2 / (2 * epsilon_0))
E_between = (sigma1 / (2 * epsilon_0)) + (sigma2 / (2 * epsilon_0))
E_right = -(sigma1 / (2 * epsilon_0)) - (sigma2 / (2 * epsilon_0))

E_left, E_between, E_right



d = 0.1  # наприклад, відстань між пластинами, м

# Координати точок ліворуч, між та праворуч від пластин
x_left = np.linspace(-0.1, 0, 5)
x_between = np.linspace(0, d, 5)
x_right = np.linspace(d, d + 0.1, 5)

# Напруженість поля в цих точках
E_left_points = np.full_like(x_left, E_left)
E_between_points = np.full_like(x_between, E_between)
E_right_points = np.full_like(x_right, E_right)

# Об'єднання точок для побудови графіка
x = np.concatenate([x_left, x_between, x_right])
E = np.concatenate([E_left_points, E_between_points, E_right_points])

plt.figure(figsize=(10, 6))
plt.plot(x, E, label='E(x)')
plt.xlabel('Відстань (м)')
plt.ylabel('Напруженість поля (В/м)')
plt.title('Залежність напруженості електричного поля від відстані')
plt.axvline(0, color='k', linestyle='--')
plt.axvline(d, color='k', linestyle='--')
plt.legend()
plt.grid(True)
plt.savefig('electric_field_plot.png')
plt.close()
