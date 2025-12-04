
import time
def portfolio_add_cash(self, amount: float):
    """TODO:
    - Reject negative amounts
    - Otherwise add to self.cash
    - Print message showing how much cash added and what you new cash balance is
    - return not needed
    """
#need to check to make sure positive first, otherwise whole thing crash
    if amount <= 0:
        print("Invalid amount")
        return
#add amnt to self.cash
    self.cash += amount
#print amnt of cash added and new balance 
    print(f"Added ${amount}. New balance: ${self.cash}")