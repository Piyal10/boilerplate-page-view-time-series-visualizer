import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')


q_low = df['value'].quantile(0.025)
q_high = df['value'].quantile(0.975)
df = df[(df['value'] >= q_low) & (df['value'] <= q_high)]

def draw_line_plot():
   
    df_line = df.copy()
    
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_line.index, df_line['value'], color='blue')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.xticks(rotation=45)
    
    
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    
    fig, ax = plt.subplots(figsize=(12, 6))
    df_bar_grouped.plot(kind='bar', ax=ax)
    ax.set_title('Average Daily Page Views by Month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')
    
    
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():

    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))
    
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    
    sns.boxplot(x='month', y='value', data=df_box, ax=ax2, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    

    fig.savefig('box_plot.png')
    return fig
