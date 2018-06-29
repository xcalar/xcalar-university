def parse_and_log(inFile, inStream):
    import logging                                  # importing logging module 
    import datetime                                 # to get current date-time for our error logs
    import codecs 
    logging.basicConfig(level=logging.INFO)         # setting logging 
    firstRow = True
    Utf8Reader = codecs.getreader("utf-8")          #  Xcalar opens and streams files in binary mode,
    utf8Stream = Utf8Reader(inStream)               #  We need a codec to convert it to UTF-8
    for line in utf8Stream:                                  
        fields = line.split(",")                    # split comma separated fields
        if firstRow:                                # skip first row (headers)
            headers = fields                              
            firstRow = False
            continue
        try:
            record = {}                                                       # record dictionary
            record["security"] = fields[0]                                      # Asked Price 
            record["Date"] = fields[1]                                        # Date
            record["Ask"] = float(fields[3])                                  # Asked Price
            record["Bid"] = float(fields[2])                                  # Bid Price
            record["Avg"] = (float(fields[2]) + float(fields[3])) / 2.0       # New Field , (Ask + Bid) / 2.0
            record["Sale"] = float(fields[6])                                 # Handshake price
            record["Volume"] = float(fields [8])                              # Number of stocks
            record["Total"] = float(fields[8]) * float (fields[6])            # New Field , Total Price 
            yield record;
        except Exception as e:
            #add error logging. These logs will appear in file xpu.out
            log_dict = {}
            log_dict ["Time Stamp"] = datetime.datetime.utcnow().strftime("%I:%M%p on %B %d, %Y")
            log_dict ["Source UDF"] = "parse_stocks_file"
            log_dict ["Description"] = "Parser Error " + str(e)
            log_dict ["File"] = inFile
            logging.error(log_dict)
            yield {"Bad Record":line, "Exception": str(e)}
