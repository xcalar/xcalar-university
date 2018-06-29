def bid_ask_spread (bid, ask, last_sale):
    ask = float(ask)
    bid = max(0,float(bid))
    if ask < 0:
        ask = last_sale
    if ask > 0:
        spread = (ask - bid) * 100 / ask
    else:
        spread = 1
    return str(spread)   
