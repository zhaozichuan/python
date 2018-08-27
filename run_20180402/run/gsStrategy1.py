# encoding: UTF-8


import gsTemplate

import datetime


########################################################################
class TradingStrategy(gsTemplate.StrategyTemplate):
    """策略模板"""
    
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(TradingStrategy, self).__init__()
        
        self.vtSymbol = '000001.SZSE'
        self.vtOrderID = None
        
    #----------------------------------------------------------------------
    def onInit(self):
        """初始化策略（必须由用户继承实现）"""
        self.writeLog(u'onInit调用')
        
        data = {
            'inited': self.inited,
            'trading': self.trading
            }
        self.putEvent(data)
        
        self.subscribe(self.vtSymbol)
    
    #----------------------------------------------------------------------
    def onStart(self):
        """启动策略（必须由用户继承实现）"""
        self.writeLog(u'onStart调用')
        
        data = {
            'inited': self.inited,
            'trading': self.trading
            }
        self.putEvent(data)
        
    #----------------------------------------------------------------------
    def onStop(self):
        """停止策略（必须由用户继承实现）"""
        self.writeLog(u'onStop调用')
        
        data = {
            'inited': self.inited,
            'trading': self.trading
            }
        self.putEvent(data)
        
    #----------------------------------------------------------------------
    def onTick(self, tick):
        """收到行情TICK推送（必须由用户继承实现）"""
        self.writeLog(u'onTick调用')
        
        # 过滤没有昨收数据的情况
        if not tick.preClosePrice:
            self.writeLog(u'昨收数据为0，不进行操作')
            return
        
        # 过滤委托尚未完成的情况
        if self.vtOrderID:
            self.writeLog(u'委托尚未完成，不进行操作')
            return
        
        # 计算今日涨跌
        todayChange = tick.lastPrice / tick.preClosePrice - 1
        
        # 获取持仓数据
        pos = self.getPosition(self.vtSymbol)
        
        # 上涨超过5%
        if todayChange >= 0.01:    
            # 若持仓返回为None或者仓位为0，则发单买入
            if not pos or pos.position == 0:
                # 以涨停价发单买入100股，并记录委托号
                self.vtOrderID = self.buy(self.vtSymbol, tick.upperLimit, 100)
                self.writeLog(u'涨幅为%s%%，买入挂单%s股于%s，委托号%s' %(todayChange*100, 100, 
                                                                       tick.upperLimit, self.vtOrderID))
                
        # 推送数据
        data = {
            'vtSymbol': self.vtSymbol,
            'lastPrice': tick.lastPrice,
            'pos': pos.position,
            'todayChange': '%.1f%%' %(todayChange * 100),
            'vtOrderID': self.vtOrderID
        }
        
        self.putEvent(data)

    #----------------------------------------------------------------------
    def onOrder(self, order):
        """收到委托变化推送（必须由用户继承实现）"""
        self.writeLog(u'onOrder调用')
        
        # 若是由策略发出的委托
        if order.vtOrderID == self.vtOrderID:
            # 且状态为已完成（全部成交、撤单、拒单）
            if order.status in [gsTemplate.ALLTRADED, gsTemplate.CANCELLED, gsTemplate.REJECTED]:
                # 则清空委托号缓存
                self.vtOrderID = ''
                
                data = {
                    'vtOrderID': self.vtOrderID
                }         
                self.putEvent(data)
    
    #----------------------------------------------------------------------
    def onTrade(self, trade):
        """收到成交推送（必须由用户继承实现）"""
        self.writeLog(u'onTrade调用')
        
        pos = self.getPosition(self.vtSymbol)
        data = {
            'pos': pos.position
        }        
        self.putEvent(data)
    
    #----------------------------------------------------------------------
    def onTimer(self):
        """收到定时推送（必须由用户继承实现）"""
        #self.writeLog(u'onTimer调用')  
        
        t = datetime.datetime.now().time()
        data = {'time': str(t)}
        self.putEvent(data)
