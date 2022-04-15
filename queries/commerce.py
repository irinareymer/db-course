class CommerceQuery:

    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self, price, availability, arrive, game_id):
        self.cursor.execute("INSERT INTO commerce (price, availability, arrive, game_id) " +
                            "VALUES (%s, %s, %s, %s)", (price, availability, arrive, game_id))

    def select_id(self):
        self.cursor.execute("SELECT id FROM commerce")
        commerce_ids = self.cursor.fetchall()
        return commerce_ids
