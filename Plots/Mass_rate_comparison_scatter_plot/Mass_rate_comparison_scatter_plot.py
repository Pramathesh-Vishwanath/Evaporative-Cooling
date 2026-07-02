import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scienceplots

# 1. Activate the academic style sheet
plt.style.use(['science', 'no-latex'])

# ==========================================
# 2. DATA ENTRY FROM SPREADSHEET IMAGE
# ==========================================
# Format: (Measured_M1, Corrected_M1, M2)
# Both plots will lock M2 as the X-axis
data_trials = [
    # (157.6, 301.4, 304.1),
    (116, 122.4, 123.6),
    (147.3, 164.8, 166.4),
    (198.9, 159.9, 161.6),
    (229, 149.4, 151.3),
    (156.9, 133.6, 135),
    (29.4, 176.1, 177.8),
    (78.6, 191.9, 193.8),
    (243.5, 154.5, 156.1),
    (108.2, 159.9, 160.1),
    (173.8, 197.3, 198.9),
    (190.7, 197.2, 198.9),
    # (-12.1, 138.3, 139.7),
    (123.9, 180.8, 182.7),
    (25.1, 207.6, 209.4),
    (69.5, 250.3, 252.4)
]

# Process into a clean DataFrame structure
df = pd.DataFrame(data_trials, columns=['M1_Measured', 'M1_Corrected', 'M2'])

# ==========================================
# 3. REUSABLE PLOTTING FUNCTION
# ==========================================
def generate_comparison_plot(x_data, y_data, y_label, title, filename_prefix, point_color):
    # Perfect square canvas to keep physical 1:1 scale ratios visually accurate
    fig, ax = plt.subplots(figsize=(5, 5), dpi=300)
    
    # Plot experimental coordinates
    ax.scatter(
        x_data, y_data, 
        color=point_color,   
        marker='o',        
        s=30,              
        alpha=0.8,         
        edgecolors='none',
        label='Experimental Trials'
    )
    
    # Calculate uniform bounds dynamically based on data limits
    # Combining both to find absolute max/min ensures matching axis scopes
    combined_min = min(x_data.min(), y_data.min())
    combined_max = max(x_data.max(), y_data.max())
    
    # Give a bit of margins around the data limits
    min_val = combined_min - 20 if combined_min < 0 else 0
    max_val = combined_max * 1.15
    axis_limit = [min_val, max_val]
    
    # Draw perfect 45-degree y=x line
    ax.plot(
        axis_limit, axis_limit, 
        color='black', 
        linestyle='--', 
        linewidth=1.2, 
        label='Ideal Agreement ($y=x$)'
    )
    
    # Force axis configurations
    ax.set_aspect('equal') 
    ax.set_xlim(axis_limit)
    ax.set_ylim(axis_limit)
    
    # Axis typography
    ax.set_xlabel(r'Reference Evaporated Mass, $M_2$ (g/hr)', fontsize=10)
    ax.set_ylabel(y_label, fontsize=10)
    ax.set_title(title, fontsize=11, pad=12, fontweight='bold')
    
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='none', fontsize=9)
    
    # Save vector images
    plt.savefig(f'{filename_prefix}.pdf', bbox_inches='tight')
    plt.savefig(f'{filename_prefix}.svg', bbox_inches='tight')
    plt.close()

# ==========================================
# 4. EXECUTE AND GENERATE BOTH CHARTS
# ==========================================

# Chart 3A: Measured M1 vs M2 (Before Correction)
# Uses a warning-tinged color (Dark Red) to highlight raw deviation/scatter
generate_comparison_plot(
    x_data=df['M2'],
    y_data=df['M1_Measured'],
    y_label=r'Measured Mass, $M_{1,measured}$ (g/hr)',
    title='Measured $M_1$ vs. $M_2$',
    filename_prefix='comparison_measured_vs_m2',
    point_color='#A50C0C' 
)

# Chart 3B: Corrected M1 vs M2 (After Correction)
# Uses your professional academic Blue to show the clean alignment
generate_comparison_plot(
    x_data=df['M2'],
    y_data=df['M1_Corrected'],
    y_label=r'Corrected Mass, $M_{1,corrected}$ (g/hr)',
    title='Corrected $M_1$ vs. $M_2$',
    filename_prefix='comparison_corrected_vs_m2',
    point_color='#0C5DA5'
)

print("Both plots generated successfully with M2 locked on the X-axis!")