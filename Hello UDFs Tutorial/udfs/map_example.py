def bid_ask_spread (bid, ask):
    spread = float(ask) - float(bid) * 100 / float(ask)
    return str(spread)
