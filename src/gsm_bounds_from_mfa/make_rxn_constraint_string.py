from gsm_bounds_from_mfa.make_rxn_expression import make_rxn_expression

def make_rxn_constraint_string(reaction_ids, lower_bound, upper_bound):
    reaction_expression = make_rxn_expression(reaction_ids)

    # Create two separate constraint strings for lower and upper bounds
    lower_constraint = f'{reaction_expression} >= {float(lower_bound)}'
    upper_constraint = f'{reaction_expression} <= {float(upper_bound)}'

    # Combine the constraints into one string
    constraint_string = f'{lower_constraint}, {upper_constraint}'

    return constraint_string
