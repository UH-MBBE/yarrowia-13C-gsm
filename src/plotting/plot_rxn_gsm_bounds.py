def ensure_min_width(lb, ub, min_width):
    if ub - lb < min_width:
        mid_point = (ub + lb) / 2
        lb = mid_point - (min_width / 2)
        ub = mid_point + (min_width / 2)
    return lb, ub

def plot_rxn_gsm_bounds(ax=None, row=None, substrate=None, title=None):
    if substrate not in ['Glucose', 'Glycerol', 'Oleic Acid']:
        raise ValueError("Substrate must be 'Glucose', 'Glycerol', or 'Oleic Acid'")
    
    # Define labels for lower and upper bounds
    lb_label = f'{substrate} MFA LB'
    ub_label = f'{substrate} MFA UB'
    gsm_lb_label = f'{substrate} MFA-Constrained GSM LB'
    gsm_ub_label = f'{substrate} MFA-Constrained GSM UB'
    biomass_lb_label = f'{substrate} Biomass Cutoff GSM LB'
    biomass_ub_label = f'{substrate} Biomass Cutoff GSM UB'

    # Extract values for the horizontal lines
    lb = row[lb_label]
    ub = row[ub_label]
    gsm_lb = row[gsm_lb_label]
    gsm_ub = row[gsm_ub_label]
    biomass_lb = row[biomass_lb_label]
    biomass_ub = row[biomass_ub_label]

    # Define y-intercepts for each flux bound bar
    y_biomass = 2.65
    y_mfa = 1.9
    y_mfa_constrained = 1.25

    largest_bar = max([biomass_ub - biomass_lb, gsm_ub - gsm_lb, ub - lb])

    min_width = 0.003 * largest_bar

    # Adjust the bounds for each bar
    lb, ub = ensure_min_width(lb, ub, min_width)
    gsm_lb, gsm_ub = ensure_min_width(gsm_lb, gsm_ub, min_width)
    biomass_lb, biomass_ub = ensure_min_width(biomass_lb, biomass_ub, min_width)

    # Plot horizontal lines with the new bounds
    ax.hlines(y=y_biomass, xmin=biomass_lb, xmax=biomass_ub, color='k', linestyle='-', linewidth=10)
    ax.hlines(y=y_mfa, xmin=lb, xmax=ub, color='k', linestyle='-', linewidth=10)
    ax.hlines(y=y_mfa_constrained, xmin=gsm_lb, xmax=gsm_ub, color='k', linestyle='-', linewidth=10)

    # Hide the top, right, and left spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Remove y-axis ticks
    ax.set_yticks([])

    # Calculate center positions for the text
    center_biomass = (biomass_lb + biomass_ub) / 2
    center_mfa = (lb + ub) / 2
    center_mfa_constrained = (gsm_lb + gsm_ub) / 2

    # Add custom text annotations for each label
    padding = .1
    ax.text(x=center_biomass, y=y_biomass - padding, s='GSM FVA w/ Biomass Cutoff', ha='center', va='top', fontsize=10)
    ax.text(x=center_mfa, y=y_mfa + padding, s='13C-MFA', ha='center', va='bottom', fontsize=10)
    ax.text(x=center_mfa_constrained, y=y_mfa_constrained + padding, s='GSM FVA w/ MFA-Constraints', ha='center', va='bottom', fontsize=10)

    # Calculate the x-axis limits dynamically for each reaction
    all_bounds = [lb, ub, gsm_lb, gsm_ub, biomass_lb, biomass_ub]
    min_bound = min(all_bounds)
    max_bound = max(all_bounds)
    padding = (max_bound - min_bound) * 0.1  # Adding 10% padding to each side
    ax.set_xlim(min_bound - padding, max_bound + padding)

    ax.set_ylim(1, 3)

    # Set labels for x-axis and title
    ax.set_xlabel(f'Flux Normalized to 100mmols of {substrate}')
    if title:
        ax.set_title(title, fontweight='bold', fontsize=12)
    else: 
        ax.set_title(row['Equation'], fontweight='bold', fontsize=12)