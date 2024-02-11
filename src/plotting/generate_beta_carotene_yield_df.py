import pandas as pd
import straindesign as sd

def generate_beta_carotene_yield_df(model=None, substrate=None):
    beta_carotene_data = []
    for val in range(0, 41):
        g_substrate = val * 0.025
        g_oleic_acid = 1 - g_substrate
        g_beta_carotene, g_co2 = max_beta_carotene_production_from_oleic_acid(
            model=model, 
            g_glucose=g_substrate if substrate == 'Glucose' else 0,
            g_glycerol=g_substrate if substrate == 'Glycerol' else 0,
            g_oleic_acid=g_oleic_acid
        )

        beta_carotene_data.append({
            'g_substate': g_substrate,
            'g_oleic_acid': g_oleic_acid, 
            'g_beta_carotene': g_beta_carotene, 
            'g_co2': g_co2
        })

    beta_carotene_df = pd.DataFrame(beta_carotene_data)

    # rename the substrate column
    beta_carotene_df = beta_carotene_df.rename(columns={'g_substate': f'g_{substrate.lower()}'})

    return beta_carotene_df



# define a function to take in grams of glucose and grames of oleic acid and return the grams of beta carotene
def max_beta_carotene_production_from_oleic_acid(model=None, g_glucose=None, g_glycerol=None, g_oleic_acid=None):
    glucose_molar_mass = 180.16
    glycerol_molar_mass = 92.09
    oleic_acid_molar_mass = 282.47
    beta_carotene_molar_mass = 536.87

    # convert grams to millimoles
    mmol_glucose = 1000 * g_glucose / glucose_molar_mass
    mmol_glycerol = 1000 * g_glycerol / glycerol_molar_mass
    mmol_oleic_acid = 1000 * g_oleic_acid / oleic_acid_molar_mass
    
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

    # convert millimoles of beta carotene to grams
    beta_carotene_mmols = sol_max.objective_value
    beta_carotene_moles = beta_carotene_mmols / 1000
    beta_carotene_grams = beta_carotene_moles * beta_carotene_molar_mass

    # convert millimoles of CO2 to grams
    co2_mmols = sol_max.fluxes['EX_co2(e)']
    co2_moles = co2_mmols / 1000
    co2_grams = co2_moles * 44.01

    return beta_carotene_grams, co2_grams