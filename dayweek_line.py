# -*- coding: utf-8 -*-
"""
作者：邢不行

本系列帖子“量化小讲堂”，通过实际案例教初学者使用python、pandas进行金融数据处理，希望能对大家有帮助。

必读文章《10年400倍策略分享-附视频逐行讲解代码》：http://bbs.pinggu.org/thread-5558776-1-1.html

所有系列文章汇总请见：http://bbs.pinggu.org/thread-3950124-1-1.html

想要快速、系统的学习量化知识，可以参与我与论坛合作开设的《python量化投资入门》视频课程：http://www.peixun.net/view/1028.html，我会亲自授课，随问随答。
参与课程还可以免费加入我的小密圈，我每天会在圈中分享量化的所见所思，圈子介绍：http://t.xiaomiquan.com/BEiqzVB

微信：xbx_laoshi，量化交流Q群(快满)：438143420，有问题欢迎交流。

文中用到的A股数据可在www.yucezhe.com下载，这里可以下载到所有股票、从上市日起的交易数据、财务数据、分钟数据、分笔数据、逐笔数据等。
"""
import pandas as pd


# ========== 从原始csv文件中导入日线股票数据，以浦发银行sh600000为例

# 导入数据 - 注意：这里请填写数据文件在您电脑中的路径
#stock_data = pd.read_csv('trading-data@full/stock data/sh600000.csv', parse_dates=[1])

path = r'D:\zzc\kfile\600000.csv'
f = open(path,'r') #mac不用这行，直接pd.read_csv(path)
stock_data = pd.read_csv(f)

#stock_data= stock_data.head(5)
stock_data.rename(columns={'日期':'tradeDate', '股票代码':'code', '最高价':'high', '开盘价':'open', '最低价':'low', '收盘价':'close', '换手率':'change', '成交量':'volume', '成交金额':'money', '流通市值':'traded_market_value'}, inplace = True)
stock_data['tradeDate'] = stock_data['tradeDate'].apply(lambda x: x.replace("-", ""))
#stock_data['tradeDate'] = stock_data['tradeDate'].apply(lambda x: x+' 00:00:00')
    
#print(stock_data)


# ========== 将导入的日线数据stock_data，转换为周线数据period_stock_data

# 设定转换的周期period_type，转换为周是'W'，月'M'，季度线'Q'，五分钟是'5min'，12天是'12D'
period_type = 'W'

# 将【date】设定为index
#stock_data.set_index('tradeDate', inplace=True)
#print(stock_data)
# 进行转换，周线的每个变量都等于那一周中最后一个交易日的变量值

#pd.to_datetime(stock_data.tradeDate, unit = 's')
stock_data.set_index('tradeDate', inplace=True)
stock_data.index = pd.to_datetime(stock_data.index)

print(stock_data.head(10))
period_stock_data = stock_data.resample(period_type, how='last')

# 周线的【change】等于那一周中每日【change】的连续相乘
period_stock_data['change'] = stock_data['change'].resample(period_type, how=lambda x: (x+1.0).prod() - 1.0)
# 周线的【open】等于那一周中第一个交易日的【open】
period_stock_data['open'] = stock_data['open'].resample(period_type, how='first')
# 周线的【high】等于那一周中【high】的最大值
period_stock_data['high'] = stock_data['high'].resample(period_type, how='max')
# 周线的【low】等于那一周中【low】的最小值
period_stock_data['low'] = stock_data['low'].resample(period_type, how='min')
# 周线的【volume】和【money】等于那一周中【volume】和【money】各自的和
period_stock_data['volume'] = stock_data['volume'].resample(period_type, how='sum')
period_stock_data['money'] = stock_data['money'].resample(period_type, how='sum')

# 计算周线turnover
period_stock_data['turnover'] = period_stock_data['volume'] / \
                                (period_stock_data['traded_market_value']/period_stock_data['close'])

# 股票在有些周一天都没有交易，将这些周去除
period_stock_data = period_stock_data[period_stock_data['code'].notnull()]
period_stock_data.reset_index(inplace=True)




# ========== 将计算好的周线数据period_stock_data输出到csv文件

# 导出数据 - 注意：这里请填写数据文件在您电脑中的路径
period_stock_data.to_csv('D:\\zzc\\week_stock_data.csv', index=False)
