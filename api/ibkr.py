from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.common import BarData

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        
    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)
        self.start()
        
    def start(self):
        contract = Contract()
        contract.symbol = "AAPL"
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"

        self.reqRealTimeBars(1, contract, 5, "MIDPOINT", True, [])
        
    def historicalData(self, reqId, bar):
        print("HistoricalData. Ticker Id:", reqId, "BarData:", bar)
        
    def realTimeBar(self, reqId: int, time: int, open_: float, high: float, low: float, close: float, volume: int, wap: float, count: int):
        print("RealTimeBar. Ticker Id:", reqId, "Time:", time, "Open:", open_, "High:", high, "Low:", low, "Close:", close, "Volume:", volume, "WAP:", wap, "Count:", count)
        

