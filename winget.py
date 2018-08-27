# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:24:18 2018

@author: Administrator
"""
from WindPy import *
def myCallback(indata):
    if indata.ErrorCode!=0:
        print('error code:'+str(indata.ErrorCode)+'\n');
        return();

    global begintime
    lastvalue ="";
    print(indata)
#    for k in range(0,len(indata.Fields)):
#         if(indata.Fields[k] == "rt_low"):
#            lastvalue = str(indata.Data[k][0]);
#
#    string =  lastvalue +"\n";
#    print(string);
w.start()
#        w.wsq("170210.IB","rt_time,rt_last",func=myCallback)
w.wsq("600030.SH,000001.SZ","rt_last,rt_last_vol",func=myCallback)
