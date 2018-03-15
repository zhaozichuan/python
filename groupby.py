
"""
Created on Thu Mar 15 08:29:02 2018

@author: Administrator
"""
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

     df['日期1']=df['日期'].str[0:4]
     df1=df.groupby(df['日期1'])
     print(df1['开盘价'].mean())
     
     
    
         
         
         
         
         