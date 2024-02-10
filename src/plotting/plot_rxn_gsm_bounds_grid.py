import matplotlib.pyplot as plt
import pandas as pd

from plotting.plot_rxn_gsm_bounds import plot_rxn_gsm_bounds

def plot_rxn_gsm_bounds_grid(central_rxn_df=None, substrate=None):
    # Set up the grid dimensions
    n_rows = 16  # Adjust based on the actual number of plots
    n_cols = 3
    fig, axs = plt.subplots(n_rows, n_cols, figsize=(20, 4 * n_rows), dpi=300)  # Adjust width as needed
    axs = axs.flatten()  # Flatten the array of axes for easy iteration

    # Define labels for lower and upper bounds
    lb_label = f'{substrate} MFA LB'
    ub_label = f'{substrate} MFA UB'
    gsm_lb_label = f'{substrate} MFA-Constrained GSM LB'
    gsm_ub_label = f'{substrate} MFA-Constrained GSM UB'
    biomass_lb_label = f'{substrate} Biomass Cutoff GSM LB'
    biomass_ub_label = f'{substrate} Biomass Cutoff GSM UB'

    # Plot each subplot
    plot_idx = 0
    for index, row in central_rxn_df.iterrows():
        

        # Extract values for the horizontal lines
        lb = row[lb_label]
        ub = row[ub_label]
        gsm_lb = row[gsm_lb_label]
        gsm_ub = row[gsm_ub_label]
        biomass_lb = row[biomass_lb_label]
        biomass_ub = row[biomass_ub_label]

        # check if any values are NaN
        if any(pd.isnull([lb, ub, gsm_lb, gsm_ub, biomass_lb, biomass_ub])):
            continue
        elif row['Pathway'] == 'uptake':
            continue
        elif row['Pathway'] == 'biomass formation':
            title = "Biomass Formation"
            plot_rxn_gsm_bounds(axs[plot_idx], row=row, substrate=substrate, title=title)
            plot_idx += 1
        else:
            plot_rxn_gsm_bounds(axs[plot_idx], row=row, substrate=substrate)
            plot_idx += 1

    # Hide any unused axes
    for ax in axs[plot_idx:]:
        ax.set_visible(False)

    # Adjust layout with increased vertical spacing
    plt.subplots_adjust(hspace=0.5)  # Increase horizontal spacing between plots

    # Show the plot
    plt.savefig(f'../figures/{substrate} gsm and mfa bounds.png', dpi=300)
    plt.show()