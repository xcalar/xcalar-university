def bid_ask_spread(bid, ask):
    try:
        spread = float(ask) - float(bid) * 100 / float(ask)
        return str(spread)
    except ZeroDivisionError:
        return "Error: Ask is 0" # Now we dont flood the logger and observe the errors in the end table
    except Exception as e:
        return "Error: " + str(e)
