
import time
import prices as _prices

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_sell_stock(self, sym: str, shares: float, price: float):
    """TODO:
    - Ensure symbol exists (use _find_position())
    - Ensure shares <= owned
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to sell shares)
    - Reduce position shares; adjust  'cost' proportionally by shares. (assumes average cost accounting)
    - Remove the position if shares drop to 0
    - Increase self.cash by proceeds
    - Hint: the amount you reduce cost is NOT the same as the amount you increase cash
    """
    #check is sym is real
    position = _find_position(self, sym)
    if not position:
        print("Ticker symbol not in portfolio")
        return
#make sure shares <= owned
    if shares <= 0 or shares > position["shares"]:
        print("Invalid number of shares")
        return
# get last close price
    price_map = _prices.get_last_close_map([sym])
    last_close = price_map[sym]
#reduce pos shs
    proceeds = last_close * shares
    position["shares"] -= shares
    avg_cost_per_share = position["cost"] / (position["shares"] + shares)
    position["cost"] -= avg_cost_per_share * shares
#remove pos is shs drop to 0 
    if position["shares"] == 0:
        self.positions.remove(position)

#increase self.cash --> DNE reduce cost
    self.cash += proceeds

    return
       
