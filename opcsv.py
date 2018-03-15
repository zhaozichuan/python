
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
#    path = 'data/k/'
    path = 'D:\\zzc\Kfile'
#    day=(datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y%m%d')
    day=(datetime.date.today()).strftime('%Y%m%d')
      
    print (datetime1()+"start")
    
    conn = pymysql.connect(user='root', passwd='Zzc7382788',  
             host='rm-uf65wbvomnp2mufa6o.mysql.rds.aliyuncs.com', db='playebean',charset='utf8')
    cur = conn.cursor()  
    cur.execute("SELECT * FROM stock")
    for r in cur:  
      print("row_number:" , (cur.rownumber) )          
    #  print("id:"+str(r[0])+" code:"+str(r[1])+" name:"+str(r[2]))
      
      if str(r[1]).startswith('6'):
        code = "0" + str(r[1])
      elif str(r[1]).startswith('0'):
        code = "1" + str(r[1])
      else:
        continue
      
      data_url = "http://quotes.money.163.com/service/chddata.html?code="+code+"&start=19990101&end="+day+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP" 
    #  data_url = "http://quotes.money.163.com/service/chddata.html?code="+str(r[1]+"&start=19990101&end="+day+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
      df = pd.read_csv(data_url,encoding="gbk")
    #  print(data_url)
    #print(df.describe())
      df.to_csv(path+str(r[1])+'.csv',encoding="gbk")
    cur.close() 
    print (datetime1()+"end")
    conn.close() 
    

if __name__ == "__main__":
    while(1): 
      downk()
      print('down is ok!')
      time.sleep(60*60*24)    