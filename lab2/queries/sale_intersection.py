class SaleIntersectionQuery:

    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self, sale_id, commerce_id):
        self.cursor.execute("INSERT INTO sale_intersection (sale_id, commerce_id) " +
                            "VALUES (%s, %s)", (sale_id, commerce_id))
