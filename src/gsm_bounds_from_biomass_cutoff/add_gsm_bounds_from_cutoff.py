import pandas as pd
from genome_scale_modeling.get_min_max_flux_expression_from_ids import get_min_max_flux_expression_from_ids
from gsm_bounds_from_biomass_cutoff.add_mfa_bound_feasibility_column import add_mfa_bound_feasibility_column

def add_gsm_bounds_from_cutoff(model=None, central_rxn_df=None, substrate=None, uptake_reaction=None, biomass_cutoff=None):
    central_rxn_df = central_rxn_df.copy()

    # update the media to minimal medium with the specified sole carbon source
    medium = model.medium
    medium['EX_glc_e'] = 100 if substrate == 'Glucose' else 0
    medium['EX_glyc_e'] = 100 if substrate == 'Glycerol' else 0
    medium['EX_ocdcea_e'] = 10 if substrate == 'Oleic Acid' else 0
    medium['EX_h2o_e'] = 10000
    medium['EX_h_e'] = 10000
    medium['EX_nh4_e'] = 10000
    medium['EX_o2_e'] = 10000
    medium['EX_pi_e'] = 10000
    medium['EX_so4_e'] = 10000
    medium['trehalose_c_tp'] = 0
    model.medium = medium

    # set the reaction ids for the biomass formation to glucose
    if substrate == 'Glucose' or substrate == 'Glycerol':
        # define parts of the constraints string
        uptake_string = f'-{uptake_reaction} >= 100.0, -{uptake_reaction} <= 100.0'
        biomass_string = f'biomass_glucose >= {biomass_cutoff}, biomass_oil = 0, biomass_C = 0, biomass_N = 0'

        # ensure the proper biomass reaction is used in the GSM
        central_rxn_df.loc[central_rxn_df['Pathway'] == 'biomass formation', 'reaction_ids'] = 'biomass_glucose'

    elif substrate == 'Oleic Acid':
        # define parts of the constraints string
        uptake_string = f'-{uptake_reaction} >= 10.0, -{uptake_reaction} <= 10.0'
        biomass_string = f'biomass_glucose = 0, biomass_oil >= {biomass_cutoff}, biomass_C = 0, biomass_N = 0'

        # ensure the proper biomass reaction is used in the GSM
        central_rxn_df.loc[central_rxn_df['Pathway'] == 'biomass formation', 'reaction_ids'] = 'biomass_oil'
    else:
        raise ValueError(f'Unknown substrate: {substrate}')

    # define the constraints string
    constraints = f'{uptake_string}, {biomass_string}'
    print(constraints)

    gsm_lbs = []
    gsm_ubs = []

    # loop over MFA reactions and get the GSM bounds
    for _, row in central_rxn_df.iterrows():

        # check if the reaction is mapped to the GSM
        reaction_ids = row['reaction_ids']
        if pd.isna(reaction_ids):
            gsm_lbs.append('')
            gsm_ubs.append('')
            continue

        # get the reaction bounds
        rxn_lb, rxn_ub = get_min_max_flux_expression_from_ids(model, reaction_ids, constraints)

        gsm_lbs.append(10 * rxn_lb if substrate == 'Oleic Acid' else rxn_lb)
        gsm_ubs.append(10 * rxn_ub if substrate == 'Oleic Acid' else rxn_ub)

    gsm_lower_bound_col = f'{substrate} GSM LB'
    gsm_upper_bound_col = f'{substrate} GSM UB'

    # add the GSM bounds to the dataframe
    central_rxn_df[gsm_lower_bound_col] = gsm_lbs
    central_rxn_df[gsm_upper_bound_col] = gsm_ubs

    central_rxn_df = add_mfa_bound_feasibility_column(central_rxn_df, substrate)

    return central_rxn_df

