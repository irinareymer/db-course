class FeedbackQuery:

    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self, review, questions, date_of_publication, user_id, game_id):
        self.cursor.execute("INSERT INTO feedback (review, questions, date_of_publication, user_id, game_id) " +
                            "VALUES (%s, %s, %s, %s, %s)", (review, questions, date_of_publication, user_id, game_id))
