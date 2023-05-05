# Name: Shiwen An 
# Date: 2023/05/03 
# Purpose: Trying to taste some flavors for HFT trading
# Market Making

import random

# Initialize bid-ask prices and quantities
bid_price = 100
ask_price = 101
bid_qty = 10
ask_qty = 10

# Define a function to generate orders
def generate_order():
    global bid_price, ask_price, bid_qty, ask_qty
    
    # Randomly adjust bid and ask prices
    bid_price += random.randint(-1, 1)
    ask_price += random.randint(-1, 1)
    
    # Randomly adjust bid and ask quantities
    bid_qty += random.randint(-2, 2)
    ask_qty += random.randint(-2, 2)
    
    # Generate orders based on bid-ask spread
    if bid_qty > 0:
        # Generate bid order if there is available bid quantity
        bid_order = {'price': bid_price, 'quantity': bid_qty, 'side': 'buy'}
    else:
        bid_order = None
    
    if ask_qty > 0:
        # Generate ask order if there is available ask quantity
        ask_order = {'price': ask_price, 'quantity': ask_qty, 'side': 'sell'}
    else:
        ask_order = None
    
    return bid_order, ask_order

# Generate 10 orders
for i in range(10):
    bid_order, ask_order = generate_order()
    print(f"Bid order: {bid_order}, Ask order: {ask_order}")