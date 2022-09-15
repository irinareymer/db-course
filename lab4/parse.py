def parse_query(query):
    split_query = query.split(" ")
    operation = split_query[0]
    return operation


def parse_table(query, operation):
    if operation == "INSERT":
        index = 12
    elif operation == "UPDATE":
        index = 7
    else:
        index = query.find(" FROM ") + 6
    table = ''
    length = len(query) - index
    while query[index] != ' ':
        table = table + query[index]
        index += 1
        length -= 1
        if length == 0:
            break
    return table


def parse_join_table(query, list_of_tables):
    index = query.find(" JOIN ") + 6
    if index != 5:
        table = ''
        length = len(query) - index
        while query[index] != ' ':
            table = table + query[index]
            index += 1
            length -= 1
            if length == 0:
                break
        list_of_tables.append(table)
        if length != 0:
            query = query[index:]
            parse_join_table(query, list_of_tables)
    return list_of_tables
