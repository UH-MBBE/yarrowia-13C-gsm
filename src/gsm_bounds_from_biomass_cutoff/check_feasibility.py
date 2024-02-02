# Description: This file contains the function to check the feasibility of the MFA bounds with respect to the GSM bounds.
# A reaction is considered feasible if the MFA bounds are within the GSM bounds. 
# If the MFA bounds are fully outside of the GSM bounds, the reaction is considered not feasible.
def check_feasibility(gsm_bounds, mfa_bounds):
    
    gsm_lb , gsm_ub = float(gsm_bounds[0]), float(gsm_bounds[1])
    mfa_lb , mfa_ub = float(mfa_bounds[0]), float(mfa_bounds[1])

    if mfa_lb >= gsm_lb and mfa_ub <= gsm_ub:
        return 'fully feasible'
    elif mfa_ub < gsm_lb or mfa_lb > gsm_ub:
        return 'not feasible'
    else:
        return 'partially feasible'