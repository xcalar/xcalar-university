def sqlite3_import_udf (fullPath, inStream): #<== First param of the UDF is giving us the config file
    import sqlite3
    import codecs 
    import datetime
    from ast import literal_eval             #to deserialize dictionary in config file
    Utf8Reader = codecs.getreader("utf-8")   #  Xcalar opens and streams files in binary mode,
    utf8Stream = Utf8Reader(inStream)        #  We need a codec to convert it to UTF-8
    #Read config Param
    config = utf8Stream.read()               #  Read content of the config file to a python string
    #load the config file into a dictionary
    dict = literal_eval(config)              # convert the string to a dictionary   
    conn = sqlite3.connect(dict ["database file"])
    where_clause = " WHERE "
    index = 0
    for stock in dict["stocks"]:             # build WHERE CLAUSE
        where_clause += "security ='" + stock + "'"
        if index < len(dict["stocks"]) - 1:
            where_clause +=" OR "
        index += 1
    cursor = conn.execute("select * from stocks" + where_clause)
    headers = [description[0] for description in cursor.description]
    for row in cursor:
        column_indx = 0;
        record = {}
        for val in row:
            record[headers[column_indx]] = val
            column_indx += 1
        yield (record)
