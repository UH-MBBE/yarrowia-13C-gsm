import straindesign as sd
from gsm_bounds_from_mfa.make_rxn_expression import make_rxn_expression


def get_min_max_flux_expression_from_ids(model, reaction_ids, constraints):
    # Create constraint string from reaction IDs
    constraint_string = make_rxn_expression(reaction_ids)

    # Calculate min and max values using FBA or another appropriate function
    sol_min = sd.fba(model, obj=constraint_string, constraints=constraints, obj_sense='minimize')
    sol_max = sd.fba(model, obj=constraint_string, constraints=constraints, obj_sense='maximize')

    # Check if solutions are optimal
    assert_optimal(sol_min, "minimization")
    assert_optimal(sol_max, "maximization")

    # Return the min and max values
    return sol_min.objective_value, sol_max.objective_value

def assert_optimal(solution, optimization_type):
    if solution.status == 'optimal':
        return
    else:
        raise RuntimeError(f'{optimization_type.capitalize()} did not find an optimal solution. The solution status is {solution.status}.')