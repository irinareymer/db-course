class UserQuery:

    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self, email, password, username, date_of_birth):
        self.cursor.execute("INSERT INTO \"user\" (email, password, username, date_of_birth) " +
                            "VALUES (%s, %s, %s, %s)", (email, password, username, date_of_birth))

    def select_id(self):
        self.cursor.execute("SELECT id FROM \"user\"")
        user_ids = self.cursor.fetchall()
        return user_ids

    def select_user_birth(self, user_id):
        self.cursor.execute("SELECT date_of_birth FROM \"user\" WHERE id = %s", (user_id,))
        user_birth = self.cursor.fetchone()
        return user_birth
