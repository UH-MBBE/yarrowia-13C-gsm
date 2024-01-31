# Define a function to check feasibility
def check_feasibility(gsm_bounds, mfa_bounds):
    
    gsm_lb = float(gsm_bounds[0])
    gsm_ub = float(gsm_bounds[1])
    mfa_lb = float(mfa_bounds[0])
    mfa_ub = float(mfa_bounds[1])

    if mfa_lb >= gsm_lb and mfa_ub <= gsm_ub:
        return 'fully feasible'
    elif mfa_ub < gsm_lb or mfa_lb > gsm_ub:
        return 'not feasible'
    else:
        return 'partially feasible'