import os
import pandas as pd


#path = r'D:\zzc\HQ_ALL\hq\fileKLine\600030.csv'
#f = open(path,'r')
#stock_data = pd.read_csv(f,parse_dates=[1])

path = r'D:\zzc\HQ_ALL\hq\fileKLine\600030.csv'
f = open(path,'r') #mac不用这行，直接pd.read_csv(path)
stock_data = pd.read_csv(f,parse_dates=[1])
#stock_data['日期']=stock_data['日期']+ ' 10:20:30'
#print(stock_data)
#设定转换周期period_type  转换为周是'W',月'M',季度线'Q',五分钟'5min',12天'12D'
period_type = 'W'
#将[date]设定为    index   inplace是原地修改，不要创建一个新对象
stock_data.set_index('日期',inplace=True)

stock_data.index = pd.to_datetime(stock_data.index)

#进行转换，周线的每个变量都等于那一周中最后一个交易日的变量值
#print(stock_data.head(50))


period_stock_data = stock_data.resample(period_type,how='last')

print(period_stock_data.head(50))
##周线的change等于那一周中每日change的连续相乘
##period_stock_data['换手率'] = stock_data['换手率'].resample(period_type,how=lambda x:(x+1.0).prod()-1.0)
##周线的open等于那一周中第一个交易日的open
#period_stock_data['开盘价'] = stock_data['开盘价'].resample(period_type,how='first')
##周线的high等于那一周中的high的最大值
#period_stock_data['最高价'] = stock_data['最高价'].resample(period_type,how='max')
##周线的low等于那一周中的low的最大值
#period_stock_data['最低价'] = stock_data['最低价'].resample(period_type,how='min')
##周线的volume和money等于那一周中volume和money各自的和
#period_stock_data['成交量'] = stock_data['成交量'].resample(period_type,how='sum')
#period_stock_data['成交金额'] = stock_data['成交金额'].resample(period_type,how='sum')
##计算周线turnover
#period_stock_data['总市值'] = period_stock_data['成交量']/\
#                                (period_stock_data['总市值']/period_stock_data['收盘价'])
##股票在有些周一天都没有交易，将这些周去除
#period_stock_data = period_stock_data[period_stock_data['股票代码'].notnull()]
#period_stock_data.reset_index(inplace=True)
##导出数据
#period_stock_data.to_csv('week_stock_data.csv',index=False,encoding="gbk")