class CategoryIntersectionQuery:

    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self, category_id, game_id):
        self.cursor.execute("INSERT INTO category_intersection (category_id, game_id) " +
                            "VALUES (%s, %s)", (category_id, game_id))
