import argparse
import redis
import psycopg2
from progress.bar import IncrementalBar

from cache import cache_query
from db import db_query
from queries import get_query
from time_characteristics import get_time_characteristics
from times import get_time


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--read', type=int, default=1,
                        help='An integer argument to define read queries')
    parser.add_argument('--change', type=int, default=1,
                        help='An integer argument to define change queries')
    parser.add_argument('--delete', type=int, default=1,
                        help='An integer argument to define delete queries')
    parser.add_argument('--total', type=int, default=10000,
                        help='An integer argument to define total number of queries')
    args = parser.parse_args()

    r = redis.Redis()
    conn = psycopg2.connect(database="board_game_reymer", user="username",
                            password="password", host="localhost", port=5432)

    query, total_q = get_query(args.read, args.change, args.delete, args.total)

    cache_times = []
    db_times = []
    max_query_delta = float('-inf')

    bar = IncrementalBar('Progress', max=total_q)

    try:
        with conn:
            with conn.cursor() as cur:
                for i in range(total_q):
                    q = query[i]
                    cache_time_delta, cache_times = get_time(r, cache_query, cur, q, cache_times)
                    db_time_delta, db_times = get_time(r, db_query, cur, q, db_times)

                    delta = db_time_delta - cache_time_delta
                    if delta > max_query_delta:
                        max_query_delta = delta

                    bar.next()

                get_time_characteristics(cache_times, "with")
                get_time_characteristics(db_times, "without")
                print("\nAt best, with cache faster on: ", max_query_delta)
    finally:
        conn.close()
        bar.finish()
