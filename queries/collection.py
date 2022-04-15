class CollectionQuery:

    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self, name):
        self.cursor.execute("INSERT INTO collection (name) " + "VALUES (%s)", (name, ))

    def select_max_id(self):
        self.cursor.execute("SELECT max(id) FROM collection")
        collection_id = self.cursor.fetchone()
        return collection_id
