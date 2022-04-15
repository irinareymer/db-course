class BoardGameQuery:

    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self, name, description, rules, players, duration, age_limit, release, author):
        self.cursor.execute("INSERT INTO board_game (name, description, rules, players, duration, age_limit, release, "
                            "author) " +
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (name, description, rules, players,
                                                                        duration, age_limit, release, author))

    def select_max_id(self):
        self.cursor.execute("SELECT max(id) FROM board_game")
        game_id = self.cursor.fetchone()
        return game_id

    def select_id(self):
        self.cursor.execute("SELECT id FROM board_game")
        game_id = self.cursor.fetchone()
        return game_id

    def select_age_limit(self, game_id):
        self.cursor.execute("SELECT age_limit FROM board_game WHERE id = %s", (game_id,))
        age_lim = self.cursor.fetchone()
        return age_lim
