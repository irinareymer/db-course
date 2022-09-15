import time


def get_time(r, cache_or_db_query, cur, query, times):
    time_start = time.time()
    cache_or_db_query(r, cur, query)
    time_finish = time.time()
    time_delta = time_finish - time_start
    times.append(time_delta)
    return time_delta, times
