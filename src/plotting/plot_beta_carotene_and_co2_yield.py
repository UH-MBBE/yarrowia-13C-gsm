import matplotlib.pyplot as plt

def plot_beta_carotene_and_co2_yield(beta_carotene_yield_df):
    # Extracting the first and last points from the dataframe
    first_point = beta_carotene_yield_df.iloc[[0]]
    last_point = beta_carotene_yield_df.iloc[[-1]]

    # Plotting g_oleic_acid on the x-axis and g_beta_carotene on the y-axis
    plt.figure(figsize=(10, 6))
    plt.plot(
        beta_carotene_yield_df['g_oleic_acid'], 
        beta_carotene_yield_df['g_beta_carotene'], 
        marker='o', 
        linestyle='-', 
        color='blue', 
        label='Beta-Carotene Yield (g/g)'
        )

    # Plotting a line connecting the first and last points
    plt.plot([
        first_point['g_oleic_acid'].values[0], last_point['g_oleic_acid'].values[0]], 
        [first_point['g_beta_carotene'].values[0], last_point['g_beta_carotene'].values[0]], 
        color='gray',
        linestyle='--'
    )  # red dashed line for emphasis

    plt.plot(
        beta_carotene_yield_df['g_oleic_acid'], 
        beta_carotene_yield_df['g_co2'], 
        marker='o', 
        linestyle='-', 
        color='green',
        label='CO2 Loss (g/g)'
    )
    plt.plot(
        [first_point['g_oleic_acid'].values[0], last_point['g_oleic_acid'].values[0]],
        [first_point['g_co2'].values[0], last_point['g_co2'].values[0]],
        color='gray',
        linestyle='--'
    )  # red dashed line for emphasis


    plt.title('Beta-Carotene Theoretical Yield and Associated CO2 Loss in Glucose and Oleic Acid Co-Feeding')
    plt.xlabel('Oleic Acid Fraction (g oleic acid / g total Substrate)')
    plt.ylabel('Yield (g product / g total substrate)')
    plt.legend()
    plt.show()