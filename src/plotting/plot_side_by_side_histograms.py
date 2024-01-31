import matplotlib.pyplot as plt
import numpy as np

# Modified function to include average and standard deviation in the plots
def plot_side_by_side_histograms(data1, data2, title1, title2):
    # Set up the matplotlib figure with two columns and one row
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

    # Determine the range for the x-axis
    all_data = np.concatenate((data1, data2))
    x_min, x_max = np.min(all_data), np.max(all_data)

    # Calculate the average and standard deviation
    average_data1, std_dev_data1 = np.mean(data1), np.std(data1)
    average_data2, std_dev_data2 = np.mean(data2), np.std(data2)

    # Plot the first histogram
    axes[0].hist(data1, bins=30, range=(x_min, x_max), color='skyblue', edgecolor='black', log=True)
    axes[0].axvline(average_data1, color='k', linestyle='dashed', linewidth=2)
    axes[0].set_title(title1)
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
    axes[1].set_title(title2)
    axes[1].set_xlabel('GSM Bound Size')
    # Display average and std deviation
    axes[1].text(0.98, 0.98, f'Avg Upper Bound - Lower Bound: {average_data2:.2f} ± {std_dev_data2:.2f}', 
                transform=axes[1].transAxes, fontsize=10, 
                horizontalalignment='right', verticalalignment='top', 
                bbox=dict(facecolor='white', alpha=0.5, edgecolor='none', boxstyle='round,pad=0.1'))

    # Adjust the layout
    plt.tight_layout()
    plt.show()
