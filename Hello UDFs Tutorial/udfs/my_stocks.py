def parse_stocks_file(inFile, inStream):
    firstRow = True
    import codecs 
    Utf8Reader = codecs.getreader("utf-8") #  Xcalar opens and streams files in binary mode,
    utf8Stream = Utf8Reader(inStream)     #  We need a codec to convert it to UTF-8
    for line in utf8Stream:                                  
        fields = line[:-1].split(",")                           # split comma separated fields
        if firstRow:                                       # skip first row (headers)
            headers = fields                              
            firstRow = False
            continue
        record = {}                                                        # record dictionary
        for i,field in enumerate(fields):
            record[headers[i]] = field
        record["Total Sale"] = (float(record["Last Sale"]) * float(record["Volume"])) 
        yield (record)        # returns a single row to Xcalar to be inserted
