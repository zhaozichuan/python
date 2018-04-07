
"""
Created on Thu Mar 15 08:29:02 2018

@author: Administrator
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
import matplotlib.dates as mpd


import os
import pandas as pd
path = 'D:\\zzc\\Kfile\\'
name = '600011.csv'

def getp(pathname):
#    path = 'D:\\zzc\\Kfile\\600011.csv'
    #path = r'D:\zzc\HQ_ALL\hq\fileKLine\600030.csv'
    f = open(pathname,'r') #mac不用这行，直接pd.read_csv(path)
    df = pd.read_csv(f)
    #datestr=df.pop('日期');
    var=60 #指定几日均线数
    i=0
    ma10 =[]
    for i in range(10):
    #    print(df['收盘价'][i:i+var].describe()['mean'])
        ma10.append(df['收盘价'][i:i+var].describe()['mean'])
        d=df['日期'][i]
        o=df['开盘价'][i]
        c=df['收盘价'][i]
        code=df['股票代码'][i]
        if c>o and c > ma10[i] and o < ma10[i]:
            print('code',code,'d',d,'open',o,'close',c,'md10',ma10[i])


def all_path(dirname):
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            result.append(apath)
    return result
#print(ma10)    



#print(df[0:50].describe())
#print(df.index)
#df.to_csv("c://data3out.csv")
#print(data.describe())

#pf=df.groupby(['日期'])['收盘价'].sum()

#print(pf)  

if __name__ == "__main__":
#      path1 = all_path(path)
#      getp(path,name)
#      for i in path1 :
#         getp(i)
     path = r'D:\zzc\HQ_ALL\hq\fileKLine\600030.csv'
     f = open(path,'r') #mac不用这行，直接pd.read_csv(path)
     df = pd.read_csv(f)
    
#     nf = df.loc[:,'日期1']=
#     nf=df['日期1'][1][0:4]
#      = "zz"

     df['日期1']=df['日期'].str[0:7]
     df1=df.groupby(df['日期1'])
#     df2 = pd.DataFrame([1], columns=['date'])
#     df = pd.DataFrame({'open': [1, 2.1, np.nan, 4.7, 5.6, 6.8],
#                   'close': [0, 1, np.nan, 0, 0, 0],
#                   'high': [0, 0, 0, 0, 0, 1],
#                   'low': [5, 5, 6, 5, 5.6, 6.8],
#                   'foo.fox': [2, 4, 1, 0, 0, 5],
#                   'nas.foo': ['NA', 0, 1, 0, 0, 0],
#                   'foo.manchu': ['NA', 0, 0, 0, 0, 0],})
#     
#     
#     print(type(df1['开盘价'].mean()))
     df2 = df1['开盘价'].last().reset_index()
     df3 = df1['收盘价'].first().reset_index()
     df4 = df1['最高价'].max().reset_index()
     df5 = df1['最低价'].min().reset_index()
     df6 = df1['成交量'].sum().reset_index()
     
     dfx = pd.merge(pd.merge(
             pd.merge(pd.merge(df2, df3, on = '日期1'),df4,on = '日期1'),
             df5,on = '日期1'),
             df6,on = '日期1')
     
     dfx.columns = ['date','Open', 'Close', 'High', 'Low', 'Volume'] ;
     
     
     print(dfx)
     
     
     df9=df['日期'].str[0:10].prod()
     print()
#     df9 = datetime.datetime.strptime(df['日期'].str[0:10],’%Y-%m-%d')
#     print(df9.weekday())
     
#     print(df1['开盘价'].last())
#     
#    quotes = pr[0:80]
#
#    print(quotes)
#    
#    fig,ax = plt.subplots(figsize=(30,6))
#    fig.subplots_adjust(bottom=0.2)
#    mpf.candlestick_ohlc(ax,quotes,width=0.4,colorup='r',colordown='g')
#    plt.grid(False)
#    ax.xaxis_date()
#    ax.autoscale_view()
#    plt.setp(plt.gca().get_xticklabels(), rotation=30) 
#    plt.show()
#         
         
         
         
         