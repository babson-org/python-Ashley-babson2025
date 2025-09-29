def _update_position(active_client, transaction):
    # helper function to only be used inside create_transaction    
'''  
For contribution: 
- no positions exist (first contribution)
- add to existing cash balance
'''
    if transaction['type'] == 'CONTRIBUTION':
        cash = none #first cash position, nothing there 
        if active_client['positions']:
            for position in active_client['positions']:                
                if position['symbol'] == transaction['symbol']:
                    position['shares'] += transaction['shares']
                    cash = position #making new position cash?
                    break
        else:
            position = {'id': transaction['id'],            
            'shares': round(transaction['shares'], 2),
            'symbol': transaction['symbol'],
            'name': transaction['name'],
            'avg_cost': transaction['trn_price']}

            active_client['positions'].append(position)    # or client['positions].append(position)
    elif transaction['type'] == 'BUY':
        return NONE
    elif transaction['type'] == 'SELL':
        return NONE
''' 
For withdrawal:
   - Check available cash balance.
   - Reduce the cash position accordingly.
'''
    elif transaction['type'] == 'WITHDRAWAL':
        if active_client['positions']:
                    for position in active_client['positions']:                
                        if position['symbol'] >= transaction['symbol']:
                            position['shares'] -= transaction['shares']
                            cash = position #making new position cash?
                            break
        pass
    else:
        print('FATAL ERROR: we should never get here _update_postion')
        exit()
    return