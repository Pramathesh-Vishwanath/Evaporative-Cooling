import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scienceplots

# 1. Activate the academic style sheet
plt.style.use(['science', 'no-latex'])

# ==========================================
# 2. ENTER YOUR VELOCITY AND EFFECTIVENESS DATA
# ==========================================
# Format: (Air_Velocity_m_s, Effectiveness_Percent)
experimental_data = [
    (2.8, 74),
    (2.5, 91),
    (2.2, 94),
    (1.9, 77)
]

# Convert the raw entries into a clean DataFrame
df = pd.DataFrame(experimental_data, columns=['Velocity', 'Effectiveness'])

# ==========================================
# 3. PLOTTING THE CHART
# ==========================================
fig, ax = plt.subplots(figsize=(6, 4.5), dpi=300)

# Plot strictly the individual reading points without any connecting lines
ax.scatter(
    df['Velocity'], df['Effectiveness'],
    color='#0C5DA5',       # Professional academic blue
    marker='o',            # Clean circular marker for data points
    s=30,                  # Size of the data points
    alpha=0.85,            # Slight transparency to easily spot overlapping points
    edgecolors='none',     # Removes borders around circles for a clean look
    # label='Experimental Readings'
)

# 4. REFINED AXES, TYPOGRAPHY, AND BOUNDS
ax.set_xlabel(r'Air Velocity, $V$ (m/s)', fontsize=10)
ax.set_ylabel(r'Cooling Effectiveness, $\eta$ (\%)', fontsize=10)
ax.set_title('Effectiveness vs Fan Velocity', fontsize=11, pad=12, fontweight='bold')

# Give the percentage scale a clean standard boundary range
ax.set_ylim(50, 100)

# Add a thin dotted grid for technical readability and interpolation
ax.grid(True, linestyle=':', alpha=0.6)

# Display the legend cleanly inside an open corner
ax.legend(loc='lower left', frameon=True, facecolor='white', edgecolor='none', fontsize=9)

# 5. SAVE AS HIGH-RESOLUTION VECTOR GRAPHICS
plt.savefig('effectiveness_vs_velocity_scatter.pdf', bbox_inches='tight')
plt.savefig('effectiveness_vs_velocity_scatter.svg', bbox_inches='tight')

print("Scatter distribution chart successfully generated and saved as PDF/SVG vector graphics!")