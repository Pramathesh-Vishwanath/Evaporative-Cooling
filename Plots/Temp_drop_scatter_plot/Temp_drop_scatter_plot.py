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
#    (5.33, 5.7),
   (3.76, 2.3),
   (4.16, 3.1),
   (4.1, 3),
   (4.33, 2.8),
   (3.76, 2.5),
   (3.82, 3.3),
   (4.1, 3.6),
   (4.03, 2.9),
   (3.33, 3),
#    (3.47, 3.7),
   (3.96, 3.7),
   (4.07, 2.6),
   (4.36, 3.4),
   (4.1, 3.95),
#    (3.93, 4.7),
   (8.44, 8.1),
   (8.46, 7.6)
    
]

# data_setup_B = [
#     (5.0, 3.0),
#     (7.2, 4.1),
#     (9.8, 5.5),
#     (12.1, 7.3),
#     (15.3, 9.0),
    
# ]

# data_setup_C = [
#     (4.5, 1.8),
#     (6.1, 2.2),
#     (8.9, 4.0),
#     (11.5, 4.5),
#     (13.8, 6.1),
    
# ]

# --- Processing data into DataFrames (leave this as is) ---
df_A = pd.DataFrame(data_setup_A, columns=['X', 'Y'])
df_A['Setup'] = 'Setup A Name'  # Change to your actual setup label

# df_B = pd.DataFrame(data_setup_B, columns=['X', 'Y'])
# df_B['Setup'] = 'Setup B Name'  # Change to your actual setup label

# df_C = pd.DataFrame(data_setup_C, columns=['X', 'Y'])
# df_C['Setup'] = 'Setup C Name'  # Change to your actual setup label

dataset = pd.concat([df_A], ignore_index=True)

# ==========================================
# 3. PLOTTING THE CHART
# ==========================================
fig, ax = plt.subplots(figsize=(6, 4.5), dpi=300)

# Define distinct, publication-friendly markers and colors
setups = dataset['Setup'].unique()
colors = ['#0C5DA5', '#00B945', '#FF9500'] # High contrast palette
markers = ['o', 's', '^']                  # Circle, Square, Triangle

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
# Let's assume your baseline target design effectiveness is eta = 0.70
eta_target = 1
x_vals = np.array([0, dataset['X'].max() + 2])
y_vals = eta_target * x_vals

ax.plot(
    x_vals, y_vals, 
    color='black', 
    linestyle='--', 
    linewidth=1.2, 
    label=f'($\eta$ = 100%) line'
)

# 5. REFINED LABELS AND AXES TUNING
ax.set_xlabel(r'Maximum Possible Temperature Drop, $T_{db,in} - T_{wb,in}$ ($^\circ$C)', fontsize=10)
ax.set_ylabel(r'Actual Temperature Drop, $T_{db,in} - T_{db,out}$ ($^\circ$C)', fontsize=10)
ax.set_title('Actual Temperature Drop vs Maximum Possible Temperature Drop', fontsize=11, pad=12, fontweight='bold')

# Ensure the plot passes through or properly visualizes the origin
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)

# Add clear grid lines suited for quantitative evaluation
ax.grid(True, linestyle=':', alpha=0.6)

# Position legend in an open spot (usually lower right or upper left depending on data slope)
ax.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='none', fontsize=8)

# 6. EXPORTING FOR YOUR REPORT
# Always save as PDF or SVG vector format so lines and text never pixelate in your final document
plt.savefig('temperature_drop_scatter.pdf', bbox_inches='tight')
plt.savefig('temperature_drop_scatter.svg', bbox_inches='tight')

print("Plot successfully generated and saved as high-resolution vector graphics (PDF/SVG)!")