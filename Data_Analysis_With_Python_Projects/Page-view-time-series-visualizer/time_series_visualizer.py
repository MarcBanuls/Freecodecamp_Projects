import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', sep = ',', parse_dates = ['date'], index_col = 'date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
             (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (15, 5))
    ax.plot(df.index, df['value'], color = 'red', linewidth = 1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig



def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month_name()

    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean()
    df_bar = df_bar.unstack()
    month_names=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot
    fig = df_bar.plot(kind= 'bar', figsize = (10,10)).figure

    plt.title('')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    lg = plt.legend(title= 'Months', fontsize = 15, labels = month_names)
    title = lg.get_title()
    title.set_fontsize(15)

    # Save image and return fig (don't change this part)
    plt.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    df_box["month_number"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_number")
    
    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_figwidth(20)
    fig.set_figheight(10)

    ax1 = sns.boxplot(x = 'year', y = 'value', data = df_box, ax = ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    ax2 = sns.boxplot( x = 'month', y = 'value', data = df_box, ax = ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
