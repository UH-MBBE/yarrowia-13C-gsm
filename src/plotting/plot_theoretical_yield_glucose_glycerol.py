import matplotlib.pyplot as plt

# Adjust default font sizes
plt.rcParams.update({
    'font.size': 12,            # Overall default font size
    'axes.titlesize': 14,       # Font size of the axes title
    'axes.labelsize': 12,       # Font size of the x and y labels
    'xtick.labelsize': 10,      # Font size of the tick labels
    'ytick.labelsize': 10,      # Font size of the tick labels
    'legend.fontsize': 10,      # Font size of the legend
})

def plot_theoretical_yield_glucose_glycerol(glycerol_df=None, glucose_df=None):
    fig, axs = plt.subplots(1, 2, figsize=(15, 6), dpi=300)  # Create 1 row, 2 columns of plots

    # Extracting the first and last points from the dataframes
    glycerol_first_point = glycerol_df.iloc[[0]]
    glycerol_last_point = glycerol_df.iloc[[-1]]
    glucose_first_point = glucose_df.iloc[[0]]
    glucose_last_point = glucose_df.iloc[[-1]]

    # Plot for Glucose
    axs[0].plot(
        glucose_df['g_oleic_acid'], 
        glucose_df['g_co2'], 
        marker='.', 
        linestyle='-', 
        color='#BFA7A7', 
        label=r'$CO_2$ Loss (g/g)'
    )
    axs[0].plot(
        glucose_df['g_oleic_acid'], 
        glucose_df['g_beta_carotene'], 
        marker='o', 
        linestyle='-', 
        color='#BFA7A7', 
        label='Beta-Carotene Yield (g/g)'
    )
    axs[0].plot(
        [glucose_first_point['g_oleic_acid'].values[0], glucose_last_point['g_oleic_acid'].values[0]], 
        [glucose_first_point['g_beta_carotene'].values[0], glucose_last_point['g_beta_carotene'].values[0]], 
        color='gray',
        linestyle='--'
    )
    axs[0].plot(
        [glucose_first_point['g_oleic_acid'].values[0], glucose_last_point['g_oleic_acid'].values[0]],
        [glucose_first_point['g_co2'].values[0], glucose_last_point['g_co2'].values[0]],
        color='gray',
        linestyle='--'
    )
    axs[0].set_title('Glucose and Oleic Acid Co-substrate Consumption') 
    axs[0].set_xlabel('Oleic Acid Fraction (g oleic acid / g total substrate)')
    axs[0].set_ylabel('Yield (g product / g total substrate)')
    axs[0].legend()

    # Plot for Glycerol
    axs[1].plot(
        glycerol_df['g_oleic_acid'], 
        glycerol_df['g_co2'], 
        marker='.', 
        linestyle='-', 
        color='#863376', 
        label=r'$CO_2$ Loss (g/g)'
    )
    axs[1].plot(
        glycerol_df['g_oleic_acid'], 
        glycerol_df['g_beta_carotene'], 
        marker='o', 
        linestyle='-', 
        color='#863376', 
        label='Beta-Carotene Yield (g/g)'
    )
    axs[1].plot(
        [glycerol_first_point['g_oleic_acid'].values[0], glycerol_last_point['g_oleic_acid'].values[0]], 
        [glycerol_first_point['g_beta_carotene'].values[0], glycerol_last_point['g_beta_carotene'].values[0]], 
        color='gray',
        linestyle='--'
    )
    axs[1].plot(
        [glycerol_first_point['g_oleic_acid'].values[0], glycerol_last_point['g_oleic_acid'].values[0]],
        [glycerol_first_point['g_co2'].values[0], glycerol_last_point['g_co2'].values[0]],
        color='gray',
        linestyle='--'
    )
    axs[1].set_title('Glycerol and Oleic Acid Co-substrate Consumption') 
    axs[1].set_xlabel('Oleic Acid Fraction (g oleic acid / g total substrate)')
    axs[1].set_ylabel('Yield (g product / g total substrate)')
    axs[1].legend()

    plt.suptitle('Theoretical Beta-Carotene Yield and Associated $CO_2$ Loss')
    plt.tight_layout(rect=[0, 0.03, 1, 1])  # Adjust the padding between and around subplots
    plt.savefig('../figures/theoretical_beta_carotene_comparison.png', dpi=300)
    plt.show()
