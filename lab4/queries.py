import random
from math import floor

from possible_queries import read_queries, change_queries, delete_queries


def get_query(read, change, delete, total):
    queries_sum = read + change + delete
    x = floor(total / queries_sum)

    read_q = read * x
    change_q = change * x
    delete_q = delete * x

    total_q = read_q + change_q + delete_q

    query = []

    for i in range(read_q):
        query.append(random.choice(read_queries))

    for i in range(change_q):
        query.append(random.choice(change_queries))

    for i in range(delete_q):
        query.append(random.choice(delete_queries))

    random.shuffle(query)

    return query, total_q
