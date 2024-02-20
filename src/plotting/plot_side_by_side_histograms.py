import matplotlib.pyplot as plt
import numpy as np

# Adjust default font sizes
plt.rcParams.update({
    'font.size': 12,            # Overall default font size
    'axes.titlesize': 14,       # Font size of the axes title
    'axes.labelsize': 14,       # Font size of the x and y labels
    'xtick.labelsize': 14,      # Font size of the tick labels
    'ytick.labelsize': 14,      # Font size of the tick labels
    'legend.fontsize': 14,      # Font size of the legend
    'figure.titlesize': 14      # Font size of the figure title
})

# Modified function to include average and standard deviation in the plots
def plot_side_by_side_histograms(data1, data2, substrate=None):
    # Set up the matplotlib figure with two columns and one row
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5), dpi=300)

    # Determine the range for the x-axis
    all_data = np.concatenate((data1, data2))
    x_min, x_max = np.min(all_data), np.max(all_data)

    # Calculate the average and standard deviation
    average_data1, std_dev_data1 = np.mean(data1), np.std(data1)
    average_data2, std_dev_data2 = np.mean(data2), np.std(data2)

    # Plot the first histogram
    axes[0].hist(data1, bins=30, range=(x_min, x_max), color='skyblue', edgecolor='black', log=True)
    axes[0].axvline(average_data1, color='k', linestyle='dashed', linewidth=2)
    axes[0].set_title(f'{substrate} Biomass Bound GSM Size')
    axes[0].set_xlabel('GSM Bound Size')
    axes[0].set_ylabel('Number of Reactions')
    # Display average and std deviation
    axes[0].text(0.98, 0.98, f'Avg Upper Bound - Lower Bound: {average_data1:.2f} ± {std_dev_data1:.2f}', 
                transform=axes[0].transAxes, fontsize=10, 
                horizontalalignment='right', verticalalignment='top', 
                bbox=dict(facecolor='white', alpha=0.5, edgecolor='none', boxstyle='round,pad=0.1'))

    # Plot the second histogram
    axes[1].hist(data2, bins=30, range=(x_min, x_max), color='lightgreen', edgecolor='black', log=True)
    axes[1].axvline(average_data2, color='k', linestyle='dashed', linewidth=2)
    axes[1].set_title(f'{substrate} 13C-MFA Bound GSM Bound Size')
    axes[1].set_xlabel('GSM Bound Size')
    # Display average and std deviation
    axes[1].text(0.98, 0.98, f'Avg Upper Bound - Lower Bound: {average_data2:.2f} ± {std_dev_data2:.2f}', 
                transform=axes[1].transAxes, fontsize=10, 
                horizontalalignment='right', verticalalignment='top', 
                bbox=dict(facecolor='white', alpha=0.5, edgecolor='none', boxstyle='round,pad=0.1'))

    # Adjust the layout
    plt.tight_layout()

    plt.savefig(f'../figures/{substrate} side by side histograms.png', dpi=300)
    plt.show()
