class OrderQuery:

    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self, date_of_order, order_price, status, user_id):
        self.cursor.execute("INSERT INTO \"order\" (date_of_order, order_price, status, user_id) " +
                            "VALUES (%s, %s, %s, %s)", (date_of_order, order_price, status, user_id))

    def select_max_id(self):
        self.cursor.execute("SELECT max(id) FROM \"order\"")
        order_id = self.cursor.fetchone()
        return order_id
