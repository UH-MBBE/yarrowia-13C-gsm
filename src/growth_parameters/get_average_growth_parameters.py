from growth_parameters.get_trial_growth_parameters import get_trial_growth_parameters
import numpy as np

def get_average_growth_parameters(growth_df=None, substrate=None, molar_mass=None):
    growth_rates = []
    yield_coefficients = [] 
    substrate_uptake_rates = []

    # loop over trials
    for trial_num in ['1', '2', '3']:
        
        # get the growth parameters for each trial
        growth_rate, yield_coefficient, substrate_uptake_rate = get_trial_growth_parameters(
            growth_df=growth_df, 
            trial_num=trial_num, 
            molar_mass=molar_mass, 
            substrate=substrate
        )

        print(f'Trial {trial_num}:')
        print(f'growth_rate = {growth_rate:.3f} hr-1')
        print(f'yield coefficient = {yield_coefficient:.3f} g biomass/mmol {substrate}')
        print(f'substrate consumption rate = {substrate_uptake_rate:.3f} mmol {substrate}/gram biomass * hr')
        print()

        # append the growth parameters to the lists
        growth_rates.append(growth_rate)
        yield_coefficients.append(yield_coefficient)
        substrate_uptake_rates.append(substrate_uptake_rate)

    # calculate the average parameter values
    growth_rate = np.average(growth_rates)
    yield_coefficient = np.average(yield_coefficients)
    substrate_uptake_rate = np.average(substrate_uptake_rates)

    # calculate the standard deviation of parameter values
    growth_rate_std = np.std(growth_rates)
    yield_coefficient_std = np.std(yield_coefficients)
    substrate_uptake_rate_std = np.std(substrate_uptake_rates)

    # print the growth parameters
    print('Average Growth Parameters:')
    print(f'growth_rate = {growth_rate:.3f} ± {growth_rate_std:.3f} hr-1')
    print(f'yield coefficient = {yield_coefficient:.3f} ± {yield_coefficient_std:.3f} g biomass/mmol {substrate}')
    print(f'substrate consumption rate = {substrate_uptake_rate:.3f} ± {substrate_uptake_rate_std:.3f} mmol {substrate}/gram biomass * hr') 

    return {
        'growth_rate': growth_rate,
        'growth_rate_std': growth_rate_std,
        'yield_coefficient': yield_coefficient,
        'yield_coefficient_std': yield_coefficient_std,
        'substrate_uptake_rate': substrate_uptake_rate,
        'substrate_uptake_rate_std': substrate_uptake_rate_std
    }