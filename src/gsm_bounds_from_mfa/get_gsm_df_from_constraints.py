import pandas as pd
import straindesign as sd

# This function performs both parsimonious Flux Balance Analysis (pFBA) and Flux Variability Analysis (FVA) to 
# generate and return a DataFrame detailing reaction IDs, names, full reactions, and calculated flux ranges
def get_gsm_df_from_constraints(
        model=None, 
        substrate=None,
        constraints=None,
):
    # make a copy of the model
    model = model.copy()

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

    biomass_reaction_id = 'biomass_oil' if substrate == 'Oleic Acid' else 'biomass_glucose'

    # run FVA to the get the pFBA flux ranges
    fva_solution = sd.fva(
      model, 
      constraints=constraints,
    )

    for reaction_id, row in fva_solution[:5].iterrows():
        min = row['minimum']
        max = row['maximum']

        model.reactions.get_by_id(reaction_id).bounds = (min, max)

    # pfba_solution
    pfba_solution = sd.fba(model, constraints=constraints, obj=biomass_reaction_id, obj_sense='maximize', pfba=1)

    # maybe scale the fluxes to 100 uptake for oleic acid here
    if substrate == 'Oleic Acid':
        fva_solution = fva_solution * 10

    flux_col_label = f'{substrate} MFA-Constrained GSM flux'
    lb_col_label = f'{substrate} MFA-Constrained GSM LB'
    ub_col_label = f'{substrate} MFA-Constrained GSM UB'

    # make a list of dictionaries with the reaction id, name, flux, and absolute flux
    reactions = []
    for reaction_id, flux in pfba_solution.fluxes.items():
      # add the reaction info to the list of dictionaries
      reactions.append({
        'reaction_id': reaction_id,
        'reaction_name': model.reactions.get_by_id(reaction_id).name,
        'full_reaction': model.reactions.get_by_id(reaction_id).reaction,
        flux_col_label: 10 * flux if substrate == 'Oleic Acid' else flux,
        lb_col_label: fva_solution.loc[reaction_id, 'minimum'],
        ub_col_label: fva_solution.loc[reaction_id, 'maximum'],
      })

    # make a dataframe from the list of dictionaries
    pfba_df = pd.DataFrame(reactions)

    return pfba_df