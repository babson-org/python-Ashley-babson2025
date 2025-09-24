def _update_position(active_client, transaction):
    # helper function to only be used inside create_transaction    

    if transaction['type'] == 'CONTRIBUTION':
        if active_client['positions']:
            for position in active_client['positions']:                
                if position['symbol'] == transaction['symbol']:
                    position['shares'] += transaction['shares']
        else: 
            position = {'id': transaction['id'],            
            'shares': round(transaction['shares'], 2),
            'symbol': transaction['symbol'],
            'name': transaction['name'],
            'avg_cost': transaction['trn_price']}

            active_client['positions'].append(position)    # or client['positions].append(position)
    elif transaction['type'] == 'BUY':
        #get ticker
        stock = input("Please enter ticker symbol of stock you would like to buy:")

        #get share number
        while True:
            try:  
                share = int(input("Enter how many share you would like to buy:"))
                if share > 0:
                    break
                else:
                    print("please enter positive number.")          
            except ValueError:
            print("Please enter a numeric value: ")
            pass

        #import ticker data and get price per share - make sure positive 
        price = 5.00
        cost = share * price

        #check if cash is enough - using shares and price, all positive 
        #if enough, then deduct purhcase from cash
        if cash >= cost:
            #CHANGE CASH POSITION BY SUBTRACTING COST 
            # ADD TRANSACTION STOCKS TO PORTFOLIO 
            #Position in active client positions 
        else:
            print("Not enough cash. Please make a contribution.")


   
    elif transaction['type'] == 'SELL':
        pass
    elif transaction['type'] == 'WITHDRAWAL':
        pass
    else:
        print('FATAL ERROR: we should never get here _update_postion')
        exit()
    return