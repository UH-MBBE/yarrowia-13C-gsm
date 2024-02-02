def add_NADPH_fluxes_to_df(df, model=None, substrate=None):
    nadph = model.metabolites.get_by_id('nadph[c]')

    nadph_fluxes = []
    nadph_flux_ubs = []
    nadph_flux_lbs = []
    nadph_reaction_types = []

    for _, row in df.iterrows():
        reaction_id = row['reaction_id']
        reaction = model.reactions.get_by_id(reaction_id)

        nadph_coefficient = reaction.metabolites[nadph]

        nadph_fluxes.append(row[f'{substrate} MFA-Constrained GSM flux'] * nadph_coefficient)

        if nadph_coefficient > 0:
            nadph_ub = row[f'{substrate} MFA-Constrained GSM UB'] * nadph_coefficient
            nadph_lb = row[f'{substrate} MFA-Constrained GSM LB'] * nadph_coefficient

        else:
            nadph_ub = row[f'{substrate} MFA-Constrained GSM LB'] * nadph_coefficient
            nadph_lb = row[f'{substrate} MFA-Constrained GSM UB'] * nadph_coefficient

        if nadph_ub >= 0 and nadph_lb >= 0:
            nadph_reaction_type = 'source'
        elif nadph_ub <= 0 and nadph_lb <= 0:
            nadph_reaction_type = 'sink'
        else:
            nadph_reaction_type = 'ambiguous'

        nadph_flux_ubs.append(nadph_ub)
        nadph_flux_lbs.append(nadph_lb)
        nadph_reaction_types.append(nadph_reaction_type)

    df['NADPH flux'] = nadph_fluxes
    df['NADPH flux UB'] = nadph_flux_ubs
    df['NADPH flux LB'] = nadph_flux_lbs
    df['NADPH reaction type'] = nadph_reaction_types

    # sort by NADPH flux value
    df = df.sort_values(by='NADPH flux', ascending=False)

    return df
