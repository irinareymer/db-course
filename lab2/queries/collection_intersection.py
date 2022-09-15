class CollectionIntersectionQuery:

    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self, collection_id, game_id):
        self.cursor.execute("INSERT INTO collection_intersection (collection_id, game_id) " +
                            "VALUES (%s, %s)", (collection_id, game_id))
