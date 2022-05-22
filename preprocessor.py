import pandas as pd

def preprocess_df(df):

    df = df.drop(['NewDeaths', 'NewRecovered', 'Serious,Critical', 'NewCases', 'WHO Region', 'Tests/1M pop', 'Continent'
                  , 'Tot Cases/1M pop', 'Deaths/1M pop'], axis=1)

    return df

def preprocess_country(country_wise_df):
    country_wise_df = country_wise_df.drop(['New cases', 'New deaths', 'New recovered'], axis=1)

    return country_wise_df
