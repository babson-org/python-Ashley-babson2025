
def portfolio_str(self):
    """TODO: return a readable summary string. self is a Portfolio
    Example (format is flexible):
        "Bob has 2 positions and $1,234.56"
        - refer to client name
        - refer to positions --> need to get count
        - refer to the cash
    """
    pos_cnt = len(self.positions)
    return f"{self.client} has {pos_cnt} and {self.cash}"
