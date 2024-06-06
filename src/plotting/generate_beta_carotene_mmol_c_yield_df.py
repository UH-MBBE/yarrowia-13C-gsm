import pandas as pd
import straindesign as sd

def generate_beta_carotene_mmol_c_yield_df(model=None, substrate=None):

    beta_carotene_data = []

    mmol_c_substrate_values = [val * 0.025 for val in range(41)]
    # mmol_c_substrate_values = [val * 0.025 for val in range(4)]

    for mmol_c_substrate in mmol_c_substrate_values:

        # calculate the mmol of substrate carbon depending on the substrate
        mmol_substrate = mmol_c_substrate / 6 if substrate == 'Glucose' else mmol_c_substrate / 3
        
        # calculate the mmol of oleic acid
        mmol_c_oleic_acid = 1 - mmol_c_substrate
        mmol_oleic_acid = mmol_c_oleic_acid / 18


        mmol_c_beta_carotene, mmol_c_co2, mmol_c_xanthine = max_beta_carotene_mmol_c_production_from_oleic_acid(
            model=model,
            mmol_glucose=mmol_substrate if substrate == 'Glucose' else 0,
            mmol_glycerol=mmol_substrate if substrate == 'Glycerol' else 0,
            mmol_oleic_acid=mmol_oleic_acid
        )

        beta_carotene_data.append({
            'mmol_c_substate': mmol_c_substrate,
            'mmol_c_oleic_acid': mmol_c_oleic_acid, 
            'mmol_substate': mmol_substrate,
            'mmol_oleic_acid': mmol_oleic_acid, 
            'mmol_c_beta_carotene': mmol_c_beta_carotene, 
            'mmol_c_co2': mmol_c_co2,
            'mmol_c_xanthine': mmol_c_xanthine,
        })

    beta_carotene_df = pd.DataFrame(beta_carotene_data)

    # rename the substrate column
    beta_carotene_df = beta_carotene_df.rename(columns={'mmol_c_substate': f'mmol_c_{substrate.lower()}'})
    beta_carotene_df = beta_carotene_df.rename(columns={'mmol_substate': f'mmol_{substrate.lower()}'})

    return beta_carotene_df



# define a function to take in grams of glucose and grames of oleic acid and return the grams of beta carotene
def max_beta_carotene_mmol_c_production_from_oleic_acid(model=None, mmol_glucose=None, mmol_glycerol=None, mmol_oleic_acid=None):

    # set the medium
    medium = model.medium
    medium['EX_glc_e'] = mmol_glucose
    medium['EX_ocdcea_e'] = mmol_oleic_acid
    medium['EX_glyc_e'] = mmol_glycerol
    medium['EX_h2o_e'] = 10000
    medium['EX_h_e'] = 10000
    medium['EX_nh4_e'] = 10000
    medium['EX_o2_e'] = 10000
    medium['EX_pi_e'] = 10000
    medium['EX_so4_e'] = 10000
    medium['trehalose_c_tp'] = 0
    model.medium = medium

    # get the constraints
    constraints = f'EX_glc_e = {-1 * mmol_glucose}, EX_glyc_e = {-1 * mmol_glycerol}, EX_ocdcea_e = {-1*mmol_oleic_acid}'

    sol_max = sd.fba(model, obj='EX_caro_e', constraints=constraints, obj_sense='maximize')

    # convert millimoles of beta carotene to mmol of carbon
    beta_carotene_mmols = sol_max.objective_value
    beta_carotene_mmol_c = beta_carotene_mmols * 40

    # convert millimoles of CO2 to mmol of carbon
    co2_mmol = sol_max.fluxes['EX_co2(e)']
    co2_mmol_c = co2_mmol

    # get the xanthine flux
    xanthine_mmol = sol_max.fluxes['EX_xan(e)']
    xanthine_mmol_c = xanthine_mmol * 5

    return beta_carotene_mmol_c, co2_mmol_c, xanthine_mmol_c