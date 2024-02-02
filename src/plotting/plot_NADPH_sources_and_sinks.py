import matplotlib.pyplot as plt
from plotting.add_NADPH_fluxes_to_df import add_NADPH_fluxes_to_df

def plot_NADPH_sources_and_sinks(df, model=None, substrate=None):

    df = df.copy()  # Make a copy of the DataFrame to avoid modifying the original
    df = add_NADPH_fluxes_to_df(df, model, substrate)  # Add NADPH fluxes to the DataFrame
    fig, ax = plt.subplots(figsize=(10, 10))  # Create a figure and a single subplot

    # reverse the order of the rows in the df
    df = df.iloc[::-1]

    # Extract necessary data from the DataFrame
    reaction_ids = df['reaction_name'].tolist()
    flux_col = 'NADPH flux'
    lb_col, ub_col = 'NADPH flux LB', 'NADPH flux UB'
    reaction_types = df['NADPH reaction type'].tolist()

    color_map = {
        'source': 'lightgreen',
        'sink': 'orange',
        'ambiguous': 'skyblue'
    }

    # Prepare the data for bxp
    stats = []
    for _, row in df.iterrows():
        stats.append({
            'med': row[flux_col],
            'q1': row[lb_col],
            'q3': row[ub_col],
            'whislo': row[lb_col],  # Assuming no whiskers; set to lower bound
            'whishi': row[ub_col],  # Assuming no whiskers; set to upper bound
            'fliers': []  # Assuming no outliers
        })
    
    # Use bxp to plot horizontally
    bxp_result = ax.bxp(
        stats, 
        positions=range(1, len(stats) + 1), 
        vert=False,
        patch_artist=True, 
        showfliers=False
    )

    # Set colors based on category
    for patch, category in zip(bxp_result['boxes'], reaction_types):
        patch.set_facecolor(color_map[category])
    
    ax.set_yticklabels(reaction_ids, fontsize=9)  # Set y-tick labels to reaction IDs, adjust font size as needed
    ax.set_title(f'{substrate} NADPH Sources and Sinks')
    ax.set_xlabel(f'mmol NADPH Produced / 100 mmols {substrate}')

    # Adjust layout
    plt.tight_layout()
