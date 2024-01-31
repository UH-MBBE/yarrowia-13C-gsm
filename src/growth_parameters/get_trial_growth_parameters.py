
import math
from scipy import stats
import matplotlib.pyplot as plt

# Define a function for calculating growth parameters from a trial
def get_trial_growth_parameters(
    growth_df=None, 
    trial_num=None, 
    molar_mass=None,
    substrate=None
):
    # define the conversion factor from OD to g/L
    yarrowia_g_per_OD = 0.2966

    substrate_column = f'{substrate}_g/l_{trial_num}'
    biomass_column = f'yarrowia_OD_{trial_num}'

    time_h = growth_df['time_h'].tolist()
    substrate_g_L = growth_df[substrate_column].tolist()
    substrate_mmols_L = [1000 * g / molar_mass for g in substrate_g_L]
    starting_substrate = substrate_mmols_L[0]
    final_substrate = substrate_mmols_L[-1]

    yarrowia_OD = growth_df[biomass_column].tolist()
    yarrowia_g_L = [y * yarrowia_g_per_OD for y in yarrowia_OD]
    starting_biomass = yarrowia_g_L[0]
    final_biomass = yarrowia_g_L[-1]

    growth_rate, _, _, _, _ = stats.linregress(time_h, [math.log(val) for val in yarrowia_g_L])
    fitted_biomass_conc = [starting_biomass * math.exp(growth_rate * time) for time in time_h]
    fitted_biomass_produced = [biomass_conc - starting_biomass for biomass_conc in fitted_biomass_conc]

    delta_X = final_biomass - starting_biomass
    delta_S = starting_substrate - final_substrate
    yield_coefficient = delta_X / delta_S
    substrate_uptake_rate = (1/yield_coefficient) * growth_rate

    fitted_substrate_conc = [starting_substrate - (1 / yield_coefficient) * biomass_produced 
                                for biomass_produced in fitted_biomass_produced]
    
    # define a plotting area with two subplots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 5))

    # Set the background color of the figure to white
    fig.patch.set_facecolor('white')

    for ax in axes:
        # Set the background color of the plots to white
        ax.set_facecolor('white')
        
        # Set the color of the spines (borders) to black
        for spine in ax.spines.values():
            spine.set_edgecolor('black')
        
        # Set the color of the titles, labels, ticks, and tick labels to black
        ax.title.set_color('black')
        ax.xaxis.label.set_color('black')
        ax.yaxis.label.set_color('black')
        ax.tick_params(axis='both', colors='black')

    # plot biomass data on the left
    axes[0].set_title('Biomass Growth', fontsize=16)
    axes[0].set_xlabel('Time (hr)', fontsize=14)
    axes[0].set_ylabel('Biomass (g/L)', fontsize=14)

    # plot experimental biomass concentration data points
    axes[0].plot(time_h, yarrowia_g_L, 'o', color='red')
    # plot fitted biomass concentration curve
    axes[0].plot(time_h, fitted_biomass_conc, '-', color='red')

    # plot substrate consumption data on the right
    axes[1].set_title(f'{substrate.capitalize()} Consumption', fontsize=16)
    axes[1].set_ylabel(f'{substrate.capitalize()} (mmol/L)', fontsize=14)
    axes[1].set_xlabel('Time (hr)', fontsize=14)

    # plot experimental substrate concentration data points
    axes[1].plot(time_h, substrate_mmols_L, 'o', color='blue')
    # plot fitted substrate concentration curve
    axes[1].plot(time_h, fitted_substrate_conc, '-', color='blue')

    return growth_rate, yield_coefficient, substrate_uptake_rate