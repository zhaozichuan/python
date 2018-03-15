# -*- coding:utf-8 -*-
import datetime

#print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
# 格式化成Sat Mar 28 22:24:24 2016形式
day=(datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y%m%d')

data_url = "http://quotes.money.163.com/service/chddata.html?code=&start=19990101&end=" + day + "&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
   
print(data_url)
# 将格式字符串转换为时间戳
#a = "Sat Mar 28 22:24:24 2016"
#print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))