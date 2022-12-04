from dataclasses import dataclass
from dataclasses import field
# from functools import total_ordering
from typing import List
# from typing import Any

# @total_ordering
@dataclass (frozen=True)
class Stock:
    ticker: str = field (compare = False)
    price: float = field (compare = True)
    dividend: float = field (default=0, compare=False)
    dividend_frequency: float = field (default=4, compare=False)

    @property    
    def annual_dividend(self):
        _AD = self.dividend * 12
        return _AD

@dataclass (order=True)
class Position:    
    stock: Stock
    shares: int
    # position: float = field (default = 0, compare=True)

    # def __init__(self, position):
    #     self.position = position

    # @property
    # def position(self):
    #     return self.position
    
    # @position.setter
    # def position(self, p: float):
    #     p ==  self.shares * self.stock.price
    #     self.position = p
    
    def __eq__(self,other):
        if not type(other)==type(self):
            return False
        
        self.position = self.shares*self.stock.price
        print  (self.price == other.price,"\n" ,self.position == other.position)

@dataclass
class Portfolio:
    obj : Position
    port = []

    def portfolio(self):
        for x in self.obj.stock:
            port = port.append(x)
        print (port, "\n")

s1 = Stock("MSFT", 200, 0.6, 4)
s2 = Position(s1,100)
s3 = Position(s1,120)
s4 = Position(s1,150)
p_l = [s2,s3,s4]

prtf_list = Portfolio(p_l)


print ("\n",s1, "\n", "\n", s2, "\n","\n", s1==s2, "\n","\n", prtf_list, "\n")
