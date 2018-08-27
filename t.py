
"""
Created on Thu Mar 15 08:29:02 2018

@author: Administrator
"""
import pymysql
import pandas as pd
import datetime
import time
from time import strftime, localtime
"""
path = r'D:\zzc\HQ_ALL\hq\fileKLine\600030.csv'
f = open(path,'r') #mac不用这行，直接pd.read_csv(path)
df = pd.read_csv(f)
print(df)
print(df.index)
df.to_csv("c://data3out.csv")
#print(data.describe())
"""


def datetime1():
    '''''
    get datetime,format="YYYY-MM-DD HH:MM:SS"
    '''
    return strftime("%Y-%m-%d %H:%M:%S", localtime())


def downk():
    conn.close() 
    

if __name__ == "__main__":
    while(1): 
      downk()
      print('down is ok!')
      time.sleep(60*60*24)    