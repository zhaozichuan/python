# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 09:28:06 2017

@author: zzc
"""
import requests
import json
import pandas as pd
from lxml import etree
import xlwt
import urllib.request
import re
import pandas as pd
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey
import pandas as pd
import pymysql
#pymysql.install_as_MySQLdb()
#import tushare as ts
##def downback(a,b,c):

##    ''''

##    a:已经下载的数据块

##    b:数据块的大小

##    c:远程文件的大小

##   '''

##    per = 100.0 * a * b / c

##    if per > 100 :

##        per = 100

#    print('%.2f%%' % per)
code1 = 'JM1809'
stock_CodeUrl = 'http://hq.sinajs.cn/list=' + code1 
#stock_CodeUrl = 'http://fund.eastmoney.com/HBJJ_dwsy.html'
#stock_CodeUrl = 'http://quote.eastmoney.com/stocklist.html'

title=[]

#获取股票代码列表

def urlTolist(url):

    allCodeList = []

    html = urllib.request.urlopen(url).read()

    html = html.decode('gbk')
    
    print(html)

    s = r'[(.*?)]'

    pat = re.compile(s)

    code = pat.findall(html)
    
    print(code[0][1])
#    conn = pymysql.connect(user='root', passwd='Zzc7382788',  
#                     host='rm-uf65wbvomnp2mufa6o.mysql.rds.aliyuncs.com', db='playebean',charset='utf8')
#    for item in code:
#           print(item[0],item[1])
#           insert(conn,item[0],item[1],"")
#           
#    conn.close() 
    
    
    
    
    
    
#    conn = pymysql.connect(user='root', passwd='Zzc7382788',  
#                     host='rm-uf65wbvomnp2mufa6o.mysql.rds.aliyuncs.com', db='playebean',charset='utf8') 

     
#    engine=create_engine('mysql://root:Zzc7382788@rm-uf65wbvomnp2mufa6o.mysql.rds.aliyuncs.com/playebean?charset=utf8')
##        
#    data= pd.DataFrame(code)
##    print(data)
#    data.to_sql('stock1',engine) 
##    data.to_excel('c:/000875.xlsx')
#    return allCodeList    
   
   
    # stockname = pat.findall(html)
#    for item in code:
#
#        if item[0]=='6' or item[0]=='3' or item[0]=='0':
#
#            allCodeList.append(item)
#
#    return allCodeList


##插入  
def insert(conn,code,name,simple_name):  
#    conn = pymysql.connect(user='root', passwd='Zzc7382788',  
#                     host='rm-uf65wbvomnp2mufa6o.mysql.rds.aliyuncs.com', db='playebean',charset='utf8')  
    cur = conn.cursor()  
    sql= "INSERT INTO stock (code,name,simple_name) VALUES ('"+code+"','"+name+"','"+simple_name+"')"  
    print(sql)  
    sta=cur.execute(sql)  
    if sta==1:  
        print('Done')  
    else:  
        print('Failed')     
    conn.commit()  
    cur.close()      
#    conn.close()  


    

#allCodelist = urlTolist(stock_CodeUrl)

#html = urllib.request.urlopen(stock_CodeUrl, 'r',encoding='utf-8').read()
#html=html.decode('gbk')
#print(type(html))
    
# encoding=utf-8


url = 'https://api.github.com/repos/pydata/pandas/milestones/28/labels'
resp = requests.get(stock_CodeUrl)

#strHq = resp.content[19:len(resp.content)-3] 
strHq = resp.content
print(strHq)

strHq = strHq.decode('gbk')
arrHq = strHq.split(",")
#print (arrHq.decode('gbk') )
print (arrHq[20])


#data = json.loads(resp.text)
#issus_labels = pd.DataFrame(data)
#print ('issus_labels:=\n', issus_labels)    
    

#html = urllib.request.urlopen(stock_CodeUrl)


#html = html.decode('gbk')
    
#print(html)
#
#s = r'[(.*?)]'

#pat = re.compile(s)
#
#code = pat.findall(html)
#    
#print(code[0][1])

    


#myxls=xlwt.Workbook()
#sheet1=myxls.add_sheet(u'top250',cell_overwrite_ok=True)
#for i in range(0,100):
#    sheet1.write(i,0,i+1)
#    sheet1.write(i,1,str1[i])
#    myxls.save('c:\\top250.xls')
#f = open('tieba.html','w',encoding='utf-8')
#f.write(content)
#f.close()
#



#
#print(allCodelist)

#for code in allCodelist:
#
#    print('正在获取%s股票数据...'%code)
#
#    if code[0]=='6':
#
#        url = 'http://quotes.money.163.com/service/chddata.html?code=0'+code+\
#        '&end=20161231&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
#
#    else:
#
#        url = 'http://quotes.money.163.com/service/chddata.html?code=1'+code+\ '&end=20161231&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
#
#        urllib.request.urlretrieve(url,'d:\\all_stock_data\\'+code+'.csv')#可以加一个参数dowmback显示下载进度


##!/usr/bin/env pytho
## -*- coding:utf-8 -*-
##jdbc:mysql://rm-uf65wbvomnp2mufa6o.mysql.rds.aliyuncs.com:3306/playebean  
## 创建连接
#conn = pymysql.connect(host='rm-uf65wbvomnp2mufa6o.mysql.rds.aliyuncs.com', port=3306, user='root', passwd='Zzc7382788', db='playebean', charset='utf8')
### 创建游标
#cursor = conn.cursor()
#  
## 执行SQL，并返回收影响行数
#effect_row = cursor.execute("select * from stock")
#  # 获取剩余结果的第一行数据
#row_1 = cursor.fetchone()
#
#print(row_1)
## 获取剩余结果前n行数据
## row_2 = cursor.fetchmany(3)
# 
## 获取剩余结果所有数据
## row_3 = cursor.fetchall()
#
#
## 执行SQL，并返回受影响行数
##effect_row = cursor.execute("update tb7 set pass = '123' where nid = %s", (11,))
#  
## 执行SQL，并返回受影响行数,执行多次
##effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])
#  
#  
## 提交，不然无法保存新建或者修改的数据
#conn.commit()
#  
## 关闭游标
#cursor.close()
## 关闭连接
#conn.close()