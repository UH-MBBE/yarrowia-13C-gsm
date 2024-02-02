from gsm_bounds_from_mfa.make_rxn_constraint_string import make_rxn_constraint_string

# Generates a straindesign constraint string of GSM constraints from MFA data
def generate_gsm_constraints_from_MFA(mfa_reactions_to_use=None, central_rxn_df=None, substrate=None):

    mfa_lb_col = f'{substrate} MFA LB'
    mfa_ub_col = f'{substrate} MFA UB'

    constraint_strings = []

    for mfa_reaction in mfa_reactions_to_use:
        # get the reaction row
        reaction_row = central_rxn_df[central_rxn_df['Equation'] == mfa_reaction]

        # get reaction IDs
        reaction_ids = reaction_row['reaction_ids'].values[0]

        # get the MFA lower bound
        mfa_lb = reaction_row[mfa_lb_col].values[0]

        # get the MFA upper bound
        mfa_ub = reaction_row[mfa_ub_col].values[0]

        if substrate == 'Oleic Acid':
            # divide the bounds by 10
            mfa_lb /= 10
            mfa_ub /= 10

        # generate a constraint string
        constraint_string = make_rxn_constraint_string(reaction_ids, mfa_lb, mfa_ub)

        # add the constraint string to the list
        constraint_strings.append(constraint_string)

    # add biomass constraint
    biomass_row = central_rxn_df[central_rxn_df['Pathway'] == 'biomass formation']

    # get the biomass columns
    mfa_biomass_lb_col = f'{substrate} MFA LB'
    mfa_biomass_ub_col = f'{substrate} MFA UB'

    # get the biomass bounds
    mfa_biomass_lb = biomass_row[mfa_biomass_lb_col].values[0]
    mfa_biomass_ub = biomass_row[mfa_biomass_ub_col].values[0]

    # add biomass bounds to constraint string
    if substrate == 'Glucose' or substrate == 'Glycerol':
        # use glucose biomass reaction
        constraint_strings.append(f'biomass_glucose >= {mfa_biomass_lb}')
        constraint_strings.append(f'biomass_glucose <= {mfa_biomass_ub}')
        
        # block oil biomass reactions
        constraint_strings.append('biomass_oil = 0')

    elif substrate == 'Oleic Acid':
        # divide by 10
        mfa_biomass_lb /= 10
        mfa_biomass_ub /= 10
        
        # use oil biomass reaction
        constraint_strings.append(f'biomass_oil >= {mfa_biomass_lb}')
        constraint_strings.append(f'biomass_oil <= {mfa_biomass_ub}')
        
        # block oil biomass reactions
        constraint_strings.append('biomass_glucose = 0')

    # always block biomass_C and biomass_N
    constraint_strings.append('biomass_C = 0')
    constraint_strings.append('biomass_N = 0')

    full_constraint_string = ', '.join(constraint_strings)

    return full_constraint_string