# Personal Python functions Javier Alfonso Lorenz (JAL)
## Import libraries
from IPython.display import display
import matplotlib.pyplot as plt
from pandas import CategoricalDtype
import seaborn as sns
# Dataframe's Information
def df_info(par_df):
    print("[-------------------------SHAPE------------------------]")
    display(par_df.shape)
    print("[-------------------------INFO-------------------------]")
    display(par_df.info())
    print("[-----------------------DESCRIBE-----------------------]")
    display(par_df.describe(include='all',datetime_is_numeric=True).round(2))
    print("[------------------------NaN's-------------------------]")
    list_cols = par_df.columns
    display(par_df[list_cols].isnull().sum())
    print("[--------------Values in categorical variables---------]")
    list_cat_cols = par_df.select_dtypes(include= [object,CategoricalDtype] , exclude=None)
    for i in list_cat_cols:
        print("------------------%s-------------------" %i)
        print("------------Unique Values--------------")
        print("Number of unique values is: %.0f" %par_df[i].unique().size)
        print(par_df[i].unique())
        print("------------Value Counts--------------")
        display(par_df[i].value_counts())

# Activate seaborn’s “default” theme
sns.set_theme()
# Usual Boxplot
def boxplot1D(par_x, par_df):
    fig, ax = plt.subplots(figsize=(20,12))
    sTitle = 'Boxplot ' + par_x 
    ax.set_title(sTitle)
    sns.boxplot(x= par_x, data= par_df)
    plt.show()
# Usual Boxplot 2D
def boxplot2D(par_x, par_y, par_df):
    fig, ax = plt.subplots(figsize=(20,12))
    sTitle = 'Boxplot ' + par_x +' vs. '+ par_y 
    ax.set_title(sTitle)
    sns.boxplot(x= par_x, y= par_y , data= par_df)
    plt.show()

# Usual Violinplot 2D
def violinplot2D(par_x, par_y, par_df):
    fig, ax = plt.subplots(figsize=(20,12))
    sTitle = 'Violinplot ' + par_x +' vs. '+ par_y 
    ax.set_title(sTitle)
    sns.violinplot(x= par_x, y= par_y , data=par_df)
    plt.show()

# Remove outliers
def remove_outlier(df_in, col_name):
    q1 = df_in[col_name].quantile(0.25)
    q3 = df_in[col_name].quantile(0.75)
    iqr = q3-q1 #Interquartile range
    fence_low  = q1-1.5*iqr
    fence_high = q3+1.5*iqr
    df_out = df_in.loc[(df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)]
    return df_out