
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
    p = _find_position(self, sym)
    if not p:
        print("Ticker symbol not in portfolio")
        return
#make sure shares <= owned
    if shares <= 0 or shares > p["shares"]:
        print("Invalid number of shares")
        return
# get last close price
    price_map = _prices.get_last_close_map([sym])
    last_close = price_map[sym]
#reduce pos shs
    proceeds = last_close * shares
    p["shares"] -= shares
    avg_cost_per_share = p["cost"] / (p["shares"] + shares)
    p["cost"] -= avg_cost_per_share * shares
#remove pos is shs drop to 0 
    if p["shares"] == 0:
        self.positions.remove(p)

#increase self.cash --> DNE reduce cost
    self.cash += proceeds

    return
       
