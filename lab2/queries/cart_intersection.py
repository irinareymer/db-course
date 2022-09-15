class CartIntersectionQuery:

    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self, order_id, game_id):
        self.cursor.execute("INSERT INTO cart_intersection (order_id, game_id) " +
                            "VALUES (%s, %s)", (order_id, game_id))
