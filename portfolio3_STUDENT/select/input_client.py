from portfolio3_STUDENT.transactions.contribution_input import contribution_input
from portfolio3_STUDENT.x_other.get_next_id import get_next_id

def input_client(clients):
    """Gather client input (name + cash) and add to clients list."""
    fname = input('Please enter your first name: ')
    lname = input('Please enter your last name: ')

    if not fname or not lname:
        return None  # go back to menu    
    

    next_id = get_next_id(clients)

    active_client = { #this is the client that I am working with right now 
        'id': next_id,
        'fname': fname,
        'lname': lname,
        'positions': [],
        'transactions': []
    }

    clients.append(active_client) #by appending, in the list of clients have a dictionary of this active client 
    contribution_input(active_client, clients) #take care of getting first contribution 

    return 