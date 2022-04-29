import psycopg2


def db_query(r, cur, query):
    cur.execute(query)
    try:
        cur.fetchall()
    except psycopg2.ProgrammingError:
        return
