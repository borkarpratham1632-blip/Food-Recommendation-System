import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def feature_engineering(df):
    df['price_bucket'] = pd.cut(df['price'], bins=[0,200,500,1000], labels=[1,2,3])
    df['popularity'] = df.groupby('restaurant_id')['rating'].transform('count')
    return df
