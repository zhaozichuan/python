# -*- coding: utf-8 -*-
"""
@author: yucezhe
@contact: QQ:2089973054 email:xjc@yucezhe.com
"""
import pandas as pd
import numpy as np

# ========== 从原始csv文件中导入股票数据，以浦发银行sh600000为例


# 导入数据 - 注意：这里请填写数据文件在您电脑中的路径
#stock_data = pd.read_csv(r'D:\\zzc\\kfile\\600000.csv', parse_dates=[1])

path = r'D:\zzc\kfile\600000.csv'
f = open(path,'r') #mac不用这行，直接pd.read_csv(path)
stock_data = pd.read_csv(f)

#stock_data= stock_data.head(50)
stock_data.rename(columns={'日期':'tradeDate', '最高价':'high', '开盘价':'open', '最低价':'low', '收盘价':'close'}, inplace = True)
stock_data['tradeDate'] = stock_data['tradeDate'].apply(lambda x: x.replace("-", ""))
    
print(stock_data)

## 将数据按照交易日期从远到近排序
stock_data.sort_values(by='tradeDate', inplace=True)




# ========== 计算移动平均线


# 分别计算5日、20日、60日的移动平均线
ma_list = [5, 20, 60]


# 计算简单算术移动平均线MA - 注意：stock_data['close']为股票每天的收盘价
for ma in ma_list:
#    stock_data['MA_' + str(ma)] = pd.rolling_mean(stock_data['close'], ma)
     stock_data['MA_' + str(ma)] =stock_data['close'].rolling(window=ma,center=False).mean()


# 计算指数平滑移动平均线EMA
for ma in ma_list:
#    stock_data['EMA_' + str(ma)] = pd.ewma(stock_data['close'], span=ma)
     stock_data['EMA_' + str(ma)] = stock_data['close'].ewm(span=ma,min_periods=0,adjust=True,ignore_na=False).mean()

# 将数据按照交易日期从近到远排序
stock_data.sort_values(by='tradeDate', ascending=False, inplace=True)


# ========== 将算好的数据输出到csv文件 - 注意：这里请填写输出文件在您电脑中的路径
stock_data.to_csv('D:\\zzc\\sh600000_ma_ema.csv', index=False)