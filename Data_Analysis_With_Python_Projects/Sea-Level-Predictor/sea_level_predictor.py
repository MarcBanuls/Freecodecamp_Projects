import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', sep = ',')
    # Range of linear regresion for plotting:
    x = range(1880, 2050)
    x2 = range(2000, 2050)

    # Linear regression
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # New df to check from year 2000 onwards and its linear regression
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])



    # Create scatter plot
    fig, ax = plt.subplots(figsize = (15, 5))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    plt.plot(x, intercept + slope * x, color = 'red')


    # Create second line of best fit
    plt.plot(x2, intercept2 + slope2 * x2, color = 'green')


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
