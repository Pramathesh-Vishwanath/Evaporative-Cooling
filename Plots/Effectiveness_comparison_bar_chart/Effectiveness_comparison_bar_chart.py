import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'no-latex'])

setup_A_trials = [64.6, 66.5]                   
setup_B_trials = [86.4, 87.8]                       
setup_C_trials = [71.9]                       
setup_D_trials = [98.4]                       
setup_E_trials = [78]                       
setup_F_trials = [99.2]                   

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
    avg_eff = np.mean(trials)
    std_dev = np.std(trials, ddof=1)
    print(f"{name} -> Avg: {avg_eff:.2f}%, Std Dev: {std_dev:.2f}%")
    summary_list.append({
        'Case Name': name,
        'Avg Effectiveness': avg_eff,
        'Std Dev': std_dev
    })

df_master = pd.DataFrame(summary_list)

df_woi = df_master[df_master['Case Name'].str.contains(r'\(WoI\)')].reset_index(drop=True)
df_wi = df_master[df_master['Case Name'].str.contains(r'\(WI\)')].reset_index(drop=True)

df_woi['Clean Name'] = df_woi['Case Name'].str.replace(' (WoI)', '', regex=False)
df_wi['Clean Name'] = df_wi['Case Name'].str.replace(' (WI)', '', regex=False)

def generate_effectiveness_chart(df_subset, title_suffix, filename_prefix, bar_color):
    fig, ax = plt.subplots(figsize=(5.5, 4.5), dpi=300)
    
    ax.bar(
        df_subset['Clean Name'], 
        df_subset['Avg Effectiveness'], 
        # yerr=df_subset['Std Dev'], 
        capsize=5,                    
        color=bar_color,                
        edgecolor='none',               
        width=0.45,                     
        error_kw=dict(ecolor='#333333', lw=1.2, capthick=1.2)
    )

    ax.set_ylabel(r'Average Effectiveness, $\bar{\eta}$ (\%)', fontsize=10)
    ax.set_xlabel('Configuration Setup', fontsize=10)
    ax.set_title(f'Effectiveness Comparison\n({title_suffix})', fontsize=11, pad=12, fontweight='bold')

    ax.set_ylim(0, 100)
    ax.grid(True, linestyle=':', alpha=0.6, axis='y')
    
    plt.xticks(ha='right', fontsize=6)
    
    plt.savefig(f'{filename_prefix}_effectiveness.pdf', bbox_inches='tight')
    plt.savefig(f'{filename_prefix}_effectiveness.svg', bbox_inches='tight')
    plt.close()

generate_effectiveness_chart(
    df_subset=df_woi, 
    title_suffix='Without Isolation / WoI', 
    filename_prefix='woi_cases',
    bar_color='#0C5DA5'
)

generate_effectiveness_chart(
    df_subset=df_wi, 
    title_suffix='With Isolation / WI', 
    filename_prefix='wi_cases',
    bar_color='#00B945'
)

print("Successfully generated 2 independent charts in vector format (PDF/SVG) keeping your exact entry sequence!")