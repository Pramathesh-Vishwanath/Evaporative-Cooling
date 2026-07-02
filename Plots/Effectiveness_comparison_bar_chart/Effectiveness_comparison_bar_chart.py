import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scienceplots

# 1. Activate the academic style sheet
plt.style.use(['science', 'no-latex'])

# ==========================================
# 2. ENTER YOUR ACTUAL RAW TRIAL DATA HERE
# ==========================================
setup_A_trials = [73, 66, 67]                   # No Guidevanes (WoI)
setup_B_trials = [86, 87]                       # No Guidevanes (WI)
setup_C_trials = [72, 76]                       # Guidevanes, No Grills (WoI)
setup_D_trials = [91, 94]                       # Guidevanes, No Grills (WI)
setup_E_trials = [81, 70]                       # Guidevanes + Grills (WoI)
setup_F_trials = [95, 96, 92]                   # Guidevanes + Grills (WI)

# --- Automated Statistical Processing ---
raw_data = {
    'No Guidevanes (WoI)': setup_A_trials,
    'No Guidevanes (WI)': setup_B_trials,
    'Guidevanes, No Grills (WoI)': setup_C_trials,
    'Guidevanes, No Grills (WI)': setup_D_trials,
    'Guidevanes + Grills (WoI)': setup_E_trials,
    'Guidevanes + Grills (WI)': setup_F_trials
}

summary_list = []
for name, trials in raw_data.items():
    summary_list.append({
        'Case Name': name,
        'Avg Effectiveness': np.mean(trials),
        'Std Dev': np.std(trials, ddof=1)
    })

# Main DataFrame preserving your specific entry order
df_master = pd.DataFrame(summary_list)

# -------------------------------------------------------------
# INTERNAL FILTERING: Split into With Isolation (WI) and Without Isolation (WoI)
# -------------------------------------------------------------
df_woi = df_master[df_master['Case Name'].str.contains(r'\(WoI\)')].reset_index(drop=True)
df_wi = df_master[df_master['Case Name'].str.contains(r'\(WI\)')].reset_index(drop=True)

# Clean up names for the X-axis labels so they don't look repetitive on the split plots
df_woi['Clean Name'] = df_woi['Case Name'].str.replace(' (WoI)', '', regex=False)
df_wi['Clean Name'] = df_wi['Case Name'].str.replace(' (WI)', '', regex=False)

# ==========================================
# 3. PLOTTING FUNCTION (Reusable for both)
# ==========================================
def generate_effectiveness_chart(df_subset, title_suffix, filename_prefix, bar_color):
    fig, ax = plt.subplots(figsize=(5.5, 4.5), dpi=300)
    
    # Create the bar chart
    ax.bar(
        df_subset['Clean Name'], 
        df_subset['Avg Effectiveness'], 
        yerr=df_subset['Std Dev'], 
        capsize=5,                      
        color=bar_color,                
        edgecolor='none',               
        width=0.45,                     # Slightly narrower bars look better with 3 items
        error_kw=dict(ecolor='#333333', lw=1.2, capthick=1.2)
    )

    # Refined axes and labels
    ax.set_ylabel(r'Average Effectiveness, $\bar{\eta}$ (\%)', fontsize=10)
    ax.set_xlabel('Configuration Setup', fontsize=10)
    ax.set_title(f'Effectiveness Comparison\n({title_suffix})', fontsize=11, pad=12, fontweight='bold')

    ax.set_ylim(0, 100)
    ax.grid(True, linestyle=':', alpha=0.6, axis='y')
    
    # Small rotation to clean up layout
    plt.xticks(ha='right', fontsize=6)
    
    # Save files
    plt.savefig(f'{filename_prefix}_effectiveness.pdf', bbox_inches='tight')
    plt.savefig(f'{filename_prefix}_effectiveness.svg', bbox_inches='tight')
    plt.close() # Close figures to free up memory

# ==========================================
# 4. EXECUTE AND GENERATE BOTH CHARTS
# ==========================================

# Chart A: Without Isolation (WoI) - Assigned a crisp Deep Blue
generate_effectiveness_chart(
    df_subset=df_woi, 
    title_suffix='Without Isolation / WoI', 
    filename_prefix='woi_cases',
    bar_color='#0C5DA5'
)

# Chart B: With Isolation (WI) - Assigned a distinct Teal/Green to visually differentiate it in your report
generate_effectiveness_chart(
    df_subset=df_wi, 
    title_suffix='With Isolation / WI', 
    filename_prefix='wi_cases',
    bar_color='#00B945'
)

print("Successfully generated 2 independent charts in vector format (PDF/SVG) keeping your exact entry sequence!")