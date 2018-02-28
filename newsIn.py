import tushare as ts
import time  
import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy import create_engine
engine = create_engine('mysql://root:Zzc7382788@rm-uf65wbvomnp2mufa6o.mysql.rds.aliyuncs.com:3306/playebean?charset=utf8')   
  
def getNews():
    df = ts.get_latest_news()
    df1 = df[['title','url','classify','time']]
    # print df1
    #insert()
    #存入数据库
    #df1.to_sql('news',engine, if_exists='append',index_label='url')
    #df1.to_sql('news',engine, if_exists='append',index_label='title,url,classify,time',index=False)
   
    print(engine.execute('delete from news'))
    df1.to_sql('news',engine,if_exists='append', index_label='title,url,classify,time',index=False)
    
    print('---ok---') 
#for i in range(5):  
while 1 : 
#   print time.time()  
#   df= ts.get_latest_news(top=5,show_content=True) #显示最新5条新闻，并打印出新闻内容
#    print time.time()  
    getNews() 
    time.sleep(60)  
   
   
   
   
   
   
