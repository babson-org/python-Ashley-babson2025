

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
    #Validate sym
    if sym not in _prices.DOW30:
        print("TICKER INVALID")
        return
    
    # Validate shares >0
    if shares <= 0:
        print("Enter number greater than 0")
        return

    #Get last close price
    price_map = _prices.get_last_close_map([sym])
    buy_price = price_map[sym]

    total_cost = buy_price * shares

    #Check cash
    if total_cost > self.cash:
        print("Insufficient Funds")
        return

    #Look for existing position
    p = _find_position(self, sym)
#for it it doesn't already exist, must make new and add
    if p is None:
        self.positions.append({
            "sym": sym,
            "name": sym,    
            "shares": shares,
            "cost": total_cost
        })
    else:
        p["shares"] += shares
        p["cost"] += total_cost

    # Subtract cash!!!!!
    self.cash -= total_cost

    return