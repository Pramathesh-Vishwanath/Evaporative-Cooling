import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scienceplots

# 1. Activate the academic style sheet (clean, high-contrast, publication-ready)
# Using 'no-latex' ensures it runs smoothly without needing a local LaTeX engine
plt.style.use(['science', 'no-latex'])

# ==========================================
# 2. ENTER YOUR ACTUAL EXPERIMENTAL DATA HERE
# ==========================================
# Format: (X_value, Y_value)
# Where X = T_db,in - T_wb,in
# Where Y = T_db,in - T_db,out

data_setup_A = [
    (4.1, 2.8),
    (4.33, 2.8),
    (3.76, 2.5),
    (3.82, 2.9),
    (4.1, 3)
]

data_setup_B = [
    (4.03, 3.2),
    (3.33, 2.9),
    (3.47, 3),
    (3.76, 3.1)
]

data_setup_C = [
    (4.07, 3.2),
    (4.36, 3.8),
    (3.93, 3.6),
    (3.93, 3.7)
]

data_setup_D = [
    (8.44, 8),
    (12.9, 12.6),
    (8.46, 7.8)
]

# data_setup_E = [
#     # (3.6, 2.5), (4.3, 3.5), (4.2, 3.2), (8.2, 7.5)  # Enter points for Case 5 here
# ]

# --- Processing data into DataFrames ---
df_A = pd.DataFrame(data_setup_A, columns=['X', 'Y'])
df_A['Setup'] = 'Without Guide Vanes'  # Change to your actual setup label

df_B = pd.DataFrame(data_setup_B, columns=['X', 'Y'])
df_B['Setup'] = 'With Guide Vanes'  # Change to your actual setup label

df_C = pd.DataFrame(data_setup_C, columns=['X', 'Y'])
df_C['Setup'] = 'Guide vanes + Grills'  # Change to your actual setup label

df_D = pd.DataFrame(data_setup_D, columns=['X', 'Y'])
df_D['Setup'] = 'Guide vanes + Grills, Heasted Inlet'  # Change to your actual setup label

# df_E = pd.DataFrame(data_setup_E, columns=['X', 'Y'])
# df_E['Setup'] = 'Setup E Name'  # Change to your actual setup label

# Combine all 5 datasets into one master dataframe
dataset = pd.concat([df_A, df_B, df_C, df_D], ignore_index=True)

# ==========================================
# 3. PLOTTING THE CHART
# ==========================================
fig, ax = plt.subplots(figsize=(6, 4.5), dpi=300)

# Expanded to 5 unique publication-friendly colors and markers
setups = dataset['Setup'].unique()
colors = ['#0C5DA5', '#00B945', '#FF9500', '#FF2C00']  # Blue, Green, Orange, Red
markers = ['o', 's', '^', 'v', 'D']                              # Circle, Square, Triangle-Up, Triangle-Down, Diamond

for i, setup in enumerate(setups):
    subset = dataset[dataset['Setup'] == setup]
    ax.scatter(
        subset['X'], subset['Y'], 
        label=setup, 
        color=colors[i], 
        marker=markers[i], 
        s=25,          # Marker size
        alpha=0.85,    # Slight transparency to see overlapping points
        edgecolors='none'
    )

# 4. ADD THE STANDARD ADIABATIC REFERENCE LINE (Slope = eta)
eta_target = 1
x_vals = np.array([0, dataset['X'].max() + 2])
y_vals = eta_target * x_vals

# Using an rf string to prevent syntax escape sequence warnings with \eta
ax.plot(
    x_vals, y_vals, 
    color='black', 
    linestyle='--', 
    linewidth=1.2, 
    label=rf'($\eta$ = 100%) line'
)

# 5. REFINED LABELS AND AXES TUNING
ax.set_xlabel(r'Maximum Possible Temperature Drop, $T_{db,in} - T_{wb,in}$ ($^\circ$C)', fontsize=10)
ax.set_ylabel(r'Actual Temperature Drop, $T_{db,in} - T_{db,out}$ ($^\circ$C)', fontsize=10)
ax.set_title('Actual Temperature Drop vs Maximum Possible Temperature Drop', fontsize=11, pad=12, fontweight='bold')

# Ensure the plot passes through or properly visualizes the origin
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)

# [Put this immediately after your ax.set_ylim(0, 12) line]

# Add clear grid lines suited for quantitative evaluation
ax.grid(True, linestyle=':', alpha=0.6)

# Position legend in the upper left corner
ax.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='none', fontsize=8)

# 6. EXPORTING FOR YOUR REPORT
# These lines physically write the image files to your workspace folder
plt.savefig('temperature_drop_scatter.pdf', bbox_inches='tight')
plt.savefig('temperature_drop_scatter.svg', bbox_inches='tight')

# Optional: Displays the interactive window on your monitor when executed
plt.show()

print("Plot successfully generated and saved as PDF/SVG vector graphics!")