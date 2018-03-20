
"""
Created on Thu Mar 15 08:29:02 2018

@author: Administrator
"""
import os
import pandas as pd
path = 'D:\\zzc\\Kfile\\'
name = '600011.csv'

df2 = pd.DataFrame([1], columns=['date'])

df = pd.DataFrame({'open': [1, 2,3, 4, 5, 6],
                   'close': [0, 1, 0, 0, 0, 0],
                   'high': [0, 0, 0, 0, 0, 1],
                   'low': [5, 5, 6, 5, 5.6, 6.8],
                   'foo.fox': [2, 4, 1, 0, 0, 5],
                   'nas.foo': ['NA', 0, 1, 0, 0, 0],
                   'foo.manchu': ['NA', 0, 0, 0, 0, 0],})






def a(x):
    print((x).prod())    
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
    
#     nf = df.loc[:,'日期1']=
#     nf=df['日期1'][1][0:4]
#      = "zz"
    a(df['open'])
     
    
         
         
         
         
         