import matplotlib.pyplot as plt

# Adjust default font sizes
plt.rcParams.update({
    'font.size': 12,            # Overall default font size
    'axes.titlesize': 18,       # Font size of the axes title
    'axes.labelsize': 18,       # Font size of the x and y labels
    'xtick.labelsize': 16,      # Font size of the tick labels
    'ytick.labelsize': 16,      # Font size of the tick labels
    'legend.fontsize': 13,      # Font size of the legend
    'figure.titlesize': 20      # Font size of the figure title
})

def plot_beta_carotene_mmol_c_yield(glycerol_df=None, glucose_df=None):
    fig, axs = plt.subplots(1, 2, figsize=(15, 6), dpi=300)  # Create 1 row, 2 columns of plots

    # Plot for Glucose
    axs[0].fill_between(
        glucose_df['mmol_c_oleic_acid'], 
        glucose_df['mmol_c_beta_carotene'], 
        glucose_df['mmol_c_co2'] + glucose_df['mmol_c_beta_carotene'] + glucose_df['mmol_c_xanthine'], 
        color='#BFA7A7', 
        alpha=0.2, 
        label=r'Fraction C to Xanthine'
    )
    axs[0].fill_between(
        glucose_df['mmol_c_oleic_acid'], 
        glucose_df['mmol_c_beta_carotene'], 
        glucose_df['mmol_c_co2'] + glucose_df['mmol_c_beta_carotene'], 
        color='#BFA7A7', 
        alpha=0.2, 
        label=r'Fraction C to $CO_2$'
    )
    axs[0].fill_between(
        glucose_df['mmol_c_oleic_acid'], 
        glucose_df['mmol_c_beta_carotene'], 
        color='#BFA7A7', 
        alpha=0.5, 
        label='Fraction C to Beta-Carotene'
    )
    axs[0].plot(
        glucose_df['mmol_c_oleic_acid'], 
        glucose_df['mmol_c_beta_carotene'], 
        marker='o', 
        linestyle='-', 
        color='#BFA7A7'
    )
    axs[0].plot(
        glucose_df['mmol_c_oleic_acid'], 
        glucose_df['mmol_c_co2'] + glucose_df['mmol_c_beta_carotene'], 
        marker='.', 
        linestyle='-', 
        color='#BFA7A7'
    )
    axs[0].plot(
        glucose_df['mmol_c_oleic_acid'], 
        glucose_df['mmol_c_co2'] + glucose_df['mmol_c_beta_carotene'] + glucose_df['mmol_c_xanthine'], 
        marker='.', 
        linestyle='-', 
        color='#BFA7A7'
    )
    axs[0].set_title('Glucose and Oleic Acid Co-substrate Consumption') 
    axs[0].set_xlabel('Fraction of Carbon from Oleic Acid')
    axs[0].set_ylabel('Fraction of Input Carbon')
    axs[0].legend()

    # Plot for Glycerol
    axs[1].fill_between(
        glycerol_df['mmol_c_oleic_acid'], 
        glycerol_df['mmol_c_beta_carotene'], 
        glycerol_df['mmol_c_co2'] + glycerol_df['mmol_c_beta_carotene'] + glycerol_df['mmol_c_xanthine'], 
        color='#863376', 
        alpha=0.2, 
        label=r'Fraction C to Xanthine'
    )
    axs[1].fill_between(
        glycerol_df['mmol_c_oleic_acid'], 
        glycerol_df['mmol_c_beta_carotene'], 
        glycerol_df['mmol_c_co2'] + glycerol_df['mmol_c_beta_carotene'], 
        color='#863376', 
        alpha=0.2, 
        label=r'Fraction C to $CO_2$'
    )
    axs[1].fill_between(
        glycerol_df['mmol_c_oleic_acid'], 
        glycerol_df['mmol_c_beta_carotene'], 
        color='#863376', 
        alpha=0.5, 
        label='Fraction C to Beta-Carotene'
    )
    axs[1].plot(
        glycerol_df['mmol_c_oleic_acid'], 
        glycerol_df['mmol_c_beta_carotene'], 
        marker='o', 
        linestyle='-', 
        color='#863376'
    )
    axs[1].plot(
        glycerol_df['mmol_c_oleic_acid'], 
        glycerol_df['mmol_c_co2'] + glycerol_df['mmol_c_beta_carotene'], 
        marker='.', 
        linestyle='-', 
        color='#863376'
    )
    axs[1].plot(
        glycerol_df['mmol_c_oleic_acid'], 
        glycerol_df['mmol_c_co2'] + glycerol_df['mmol_c_beta_carotene'] + glycerol_df['mmol_c_xanthine'], 
        marker='.', 
        linestyle='-', 
        color='#863376'
    )
    axs[1].set_title('Glycerol and Oleic Acid Co-substrate Consumption') 
    axs[1].set_xlabel('Fraction of Carbon from Oleic Acid')
    axs[1].set_ylabel('Fraction of Input Carbon')
    axs[1].legend()

    plt.suptitle('Theoretical Beta-Carotene Yield and Associated Carbon Fate')
    plt.tight_layout(rect=[0, 0.03, 1, 1])  # Adjust the padding between and around subplots
    plt.savefig('../figures/theoretical_beta_carotene_comparison.png', dpi=300)
    plt.show()

