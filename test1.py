# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 11:16:56 2018

@author: Administrator
"""


import pandas as pd



# 针对具体某个股票，计算前n日的最高、最低价格
def get_high_low(df, n):
    df.sort_values(by=['tradeDate'], ascending=True, inplace=True)
    df['newhigh'] = df['highestPrice'].shift(1)
    df['newlow'] = df['lowestPrice'].shift(1)
    df['nhigh'] = pd.rolling_max(df['newhigh'], window=n, min_periods=1)
    df['nlow'] = pd.rolling_min(df['newlow'], window=n, min_periods=1)
    return df




if __name__ == "__main__":
   
    path = r'D:\zzc\kfile\600000.csv'
    f = open(path,'r') #mac不用这行，直接pd.read_csv(path)
    stock_price = pd.read_csv(f)
    stock_price= stock_price.head(50)
    stock_price.rename(columns={'日期':'tradeDate', '最高价':'highestPrice', '最低价':'lowestPrice'}, inplace = True)
    stock_price['tradeDate'] = stock_price['tradeDate'].apply(lambda x: x.replace("-", ""))
    
    df=get_high_low(stock_price,6)
    
    print(df)