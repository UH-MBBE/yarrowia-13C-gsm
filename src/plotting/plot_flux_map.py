import pandas as pd
from IPython.display import display, Image
from matplotlib import pyplot as plt
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox, TextArea)
plt.ioff()

# This function takes in a flux data frame and column name, and generates a flux map using the flux values in the specified column
def plot_flux_map(
    flux_df=None, 
    flux_column=None, 
    title_string='',
    file_name='',
):
    flux_df = flux_df.copy()

    unlabeled_image = plt.imread('../figures/templates/flux_map_1_carbon_source.png')

    # add a rows for computed values if the flux column is a single column
    if isinstance(flux_column, str):
        # add a row for the second oleic acid uptake flux value
        oleic_acid_uptake_row = flux_df[flux_df['ID'] == 'OA uptake']
        oleic_acid_accoa_value = 9 * oleic_acid_uptake_row[flux_column].iloc[0]

        pp_to_f6p_row_1 = flux_df[flux_df['Equation'] == 'E4P + TKC2 <-> F6P']
        pp_to_f6p_value_1 = pp_to_f6p_row_1[flux_column].iloc[0]

        pp_to_f6p_row_2 = flux_df[flux_df['Equation'] == 'GAP + TAC3 <-> F6P']
        pp_to_f6p_value_2 = pp_to_f6p_row_2[flux_column].iloc[0]

        pp_to_gap_row_1 = flux_df[flux_df['Equation'] == 'X5P <-> GAP + TKC2']
        pp_to_gap_value_1 = pp_to_gap_row_1[flux_column].iloc[0]

        pp_to_gap_row_2 = flux_df[flux_df['Equation'] == 'GAP + TAC3 <-> F6P']
        pp_to_gap_value_2 = pp_to_gap_row_2[flux_column].iloc[0]

        biomass_row = flux_df[flux_df['pathway'] == 'biomass_formation']
        biomass_g_value = biomass_row[flux_column].iloc[0]

        co2_loss_row = flux_df[flux_df['Equation'] == 'CO2 -> CO2_EX']
        co2_loss_value = co2_loss_row[flux_column].iloc[0]

        oleic_acid_accoa = {'Location on map': '(437, 111)', flux_column: oleic_acid_accoa_value}
        ppp_to_f6p = {'Location on map': '(-643, 890)', flux_column: pp_to_f6p_value_1 + pp_to_f6p_value_2}
        ppp_to_gap = {'Location on map': '(-571, 422)', flux_column: pp_to_gap_value_1 - pp_to_gap_value_2}
        # biomass_g = {'Location on map': '(-1670, -1049)', flux_column: biomass_g_value}
        # co2_loss = {'Location on map': '(-1670, -1155)', flux_column: co2_loss_value}

        # add the new rows to the dataframe
        for new_data in [oleic_acid_accoa, ppp_to_f6p, ppp_to_gap]:
            new_row = pd.Series(new_data, index=flux_df.columns)
            new_row_df = pd.DataFrame([new_row])
            new_row_df = new_row_df.reindex(columns=flux_df.columns)
            flux_df = pd.concat([flux_df, new_row_df], ignore_index=True)

    # calculate the figure size based on the image dimensions and desired DPI
    dpi = 50  # for example, set this to your preferred DPI
    fig_width = unlabeled_image.shape[1] / dpi
    fig_height = unlabeled_image.shape[0] / dpi

    # create a figure with the calculated size
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=dpi, facecolor='white')
    imagebox = OffsetImage(unlabeled_image)
    imagebox.image.axes = ax
    xy = (0.5, 0.5)
    ab = AnnotationBbox(imagebox, xy, frameon=False)
    ax.add_artist(ab)

    # loop over each reaction in the dataframe
    for _, row in flux_df.iterrows():        
        # check that there is a location for the reaction's flux
        if not pd.isnull(row['Location on map']):
            # get the flux value
            if isinstance(flux_column, str):
                flux_value = row[flux_column] if not pd.isnull(row[flux_column]) else 0
                flux_value = 'N/A' if flux_value == '' else f'{flux_value:.1f}'
            else:
                flux_value_1 = row[flux_column[0]] if not pd.isnull(row[flux_column[0]]) else 0
                flux_value_2 = row[flux_column[1]] if not pd.isnull(row[flux_column[1]]) else 0

                flux_value_1 = 'N/A' if flux_value_1 == '' else f'{flux_value_1:.1f}'
                flux_value_2 = 'N/A' if flux_value_2 == '' else f'{flux_value_2:.1f}'

                flux_value = f'({flux_value_1}, {flux_value_2})'

            # get the location of the reaction's flux on the map as a tuple
            location =  row['Location on map'].replace('(', '').replace(')', '')
            location_list = location.split(',')
            location_tuple = tuple((int(location_list[0]), int(location_list[1])))

            # create a text area with the flux value
            offsetbox = TextArea(
                flux_value,
                textprops=dict(fontsize=40, color='black', fontweight='bold', fontfamily='Arial')
            )
            
            # creates an annotation box, which is a box that can be placed on the plot area.
            ab = AnnotationBbox(
                offsetbox, 
                xy,
                xybox=location_tuple,
                xycoords='data',
                boxcoords="offset points",
                frameon=False
            )

            # add the annotation box to the plot area
            ax.add_artist(ab)


    # Display the plot title
    offsetbox = TextArea(
        title_string,
        textprops=dict(fontsize=80, color='black', fontweight='bold', fontfamily='Arial')
    )
    
    # creates an annotation box, which is a box that can be placed on the plot area.
    ab = AnnotationBbox(
        offsetbox, 
        xy,
        xybox=tuple((1600, 1137)),
        xycoords='data',
        boxcoords="offset points",
        frameon=False
    )

    # add the title annotation box to the plot area
    ax.add_artist(ab)

    # ensure that the axes have minimal styles 
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis("off")

    # save the figure with a white background and no transparency
    plt.savefig(file_name, bbox_inches='tight', pad_inches=0, facecolor='white', transparent=False)

    return Image(file_name, width=1000)