

import prices as _prices
import time

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_buy_stock(self, sym: str, shares: float, price: float):
    """TODO:    
    - Validate sym in DOW30
         In the lab4 folder is a file prices.py.  Look at the file and find out what DOW30 is
         You can access DOW30 with _prices.DOW30 (see how we import prices above)
    - Validate shares > 0
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to buy shares)
    - Make sure the client has enough cash to make the purchase (price * shares)

    - IMPORTANT: in self.positions there should only be one dictionary per symbol

    - Add the purchase to an existing position or create a new position in self.positions 
    - Be sure to decrease the client cash attribute
    NOTE: UI prompts are handled in main.py: this method only prints for invalid ticker and insufficient funds. The rest are handled in main.py
    """
    #validate sym in Dow30 to make sure that it exists
    if sym not in _prices.DOW30:
        print("TICKER INVALID")
        return
    #make sure shares is >0 
    if shares <= 0:
            return
    #get last close price
    price_map = _prices.get_last_close_map([sym])
    price = price_map[sym]

    #make sure cash >= purchase --> (price*shares)
    tot_cost = price * share
    if self.cash < tot_cost:
        print("Insufficient funds")
        return
    #add purchase to position ormake new
    position = _find_position(self, sym)
    if position:
        position["shares"] += shares
        position["cost"] += tot_cost
    else:
        new_position = {
            "sym": sym,
            "shares": shares,
            "cost": tot_cost
        }
        self.positions.append(new_position)
    # - (price*shares) from cash 
    self.cash -= tot_cost
    
    
    return



