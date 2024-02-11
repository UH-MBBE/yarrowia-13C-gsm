import matplotlib.pyplot as plt

def plot_absolute_flux_box_plot(df):
    num_labels = 20
    # Calculate the absolute values of flux for each carbon source
    df['Abs_Glucose_Flux'] = df['Glucose MFA-Constrained GSM flux'].abs()
    df['Abs_Glycerol_Flux'] = df['Glycerol MFA-Constrained GSM flux'].abs()
    df['Abs_Oleic_Acid_Flux'] = df['Oleic Acid MFA-Constrained GSM flux'].abs()

    glucose_outlier_df = df.sort_values(by='Abs_Glucose_Flux', ascending=False).copy()[:num_labels]
    glycerol_outlier_df = df.sort_values(by='Abs_Glycerol_Flux', ascending=False).copy()[:num_labels]
    oleic_acid_outlier_df = df.sort_values(by='Abs_Oleic_Acid_Flux', ascending=False).copy()[:num_labels]

    # Prepare the data for plotting
    data_to_plot = [
        df['Abs_Glucose_Flux'], 
        df['Abs_Glycerol_Flux'], 
        df['Abs_Oleic_Acid_Flux']
    ]

    # Set default font sizes using rcParams
    plt.rcParams['axes.titlesize'] = 20  # Title font size
    plt.rcParams['axes.labelsize'] = 18  # Axes label font size
    plt.rcParams['xtick.labelsize'] = 16  # X-tick label font size
    plt.rcParams['ytick.labelsize'] = 16  # Y-tick label font size

    # Creating the box plots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 10), dpi=300)

    # Box plot with outliers
    axes[0].boxplot(data_to_plot, labels=['Glucose', 'Glycerol', 'Oleic Acid'], showfliers=False)
    axes[0].set_title('GSM Reaction Rates Normalized to Carbon Uptake (Without Outliers)')
    axes[0].set_ylabel('Absolute Flux (Per 100 mmol carbon uptake)')

    # Box plot without outliers
    bp = axes[1].boxplot(data_to_plot, labels=['Glucose', 'Glycerol', 'Oleic Acid'], showfliers=True)
    axes[1].set_title('GSM Reaction Rates Normalized to Carbon Uptake (With Outliers)')
    axes[1].set_ylabel('Absolute Flux (Per 100 mmol carbon uptake)')


    for index, substrate in enumerate(bp['fliers']):
        if index == 0:
            outlier_df = glucose_outlier_df
            data_col = 'Abs_Glucose_Flux'
        elif index == 1:
            outlier_df = glycerol_outlier_df
            data_col = 'Abs_Glycerol_Flux'
        elif index == 2:
            outlier_df = oleic_acid_outlier_df
            data_col = 'Abs_Oleic_Acid_Flux'

        base_x = index + 1
        label_offset = 0.05

        y_values = substrate.get_ydata()
        y_values = sorted(y_values, reverse=True)

        y_values = y_values[:num_labels]
        
        counter = 0
        for _, row in outlier_df.iterrows():
            reaction_id = row['reaction_id']
            y = row[data_col]

            left_or_right = 'right' if counter % 2 == 0 else 'left'
            text_alignment = 'left' if left_or_right == 'right' else 'right'
            adjusted_x = base_x + label_offset if left_or_right == 'right' else base_x - label_offset
            
            counter += 1

            axes[1].text(adjusted_x, y, reaction_id, ha=text_alignment, va='center', fontsize=12)

    plt.tight_layout()

    plt.savefig(f'../figures/reaction rates by carbon source.png', dpi=300)
    plt.show()