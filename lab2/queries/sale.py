class SaleQuery:

    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self, name, discount, start, finish):
        self.cursor.execute("INSERT INTO sale (name, discount, start, finish) " +
                            "VALUES (%s, %s, %s, %s)", (name, discount, start, finish))

    def select_max_id(self):
        self.cursor.execute("SELECT max(id) FROM sale")
        sale_id = self.cursor.fetchone()
        return sale_id
