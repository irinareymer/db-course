import json

from db import db_query
from parse import parse_query, parse_table, parse_join_table


def get_cache(r, query):
    return r.get(query)


def set_cache(r, query, tables, data):
    value = {"tables": tables, "data": data}
    r.mset({query: json.dumps(value, default=str)})


def get_cache_value(cache, val):
    cache_data = json.loads(cache.decode())
    value = cache_data[val]
    return value


def get_db_data(cursor, query):
    cursor.execute(query)
    data = cursor.fetchall()
    return data


def cache_query(r, cur, query):
    list_of_tables = []
    operation = parse_query(query)
    if operation == "SELECT":
        cache = get_cache(r, query)
        if cache:
            get_cache_value(cache, "data")
        else:
            data = get_db_data(cur, query)
            from_table = parse_table(query, operation)
            join_tables = parse_join_table(query, list_of_tables)
            if join_tables is not None:
                tables = [from_table, *join_tables]
            else:
                tables = [from_table, ]
            set_cache(r, query, tables, data)
    else:
        db_query(r, cur, query)
        table = parse_table(query, operation)
        for q in r.scan_iter():
            q = q.decode()
            cache = get_cache(r, q)
            cache_tables = get_cache_value(cache, "tables")
            for cache_table in cache_tables:
                if table == cache_table:
                    r.delete(q)
