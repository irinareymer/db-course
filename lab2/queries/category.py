class CategoryQuery:

    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self, name):
        self.cursor.execute("INSERT INTO category (name) " + "VALUES (%s)", (name,))

    def select_name(self):
        self.cursor.execute("SELECT name FROM category")
        categories = self.cursor.fetchall()
        return categories

    def select_id(self):
        self.cursor.execute("SELECT id FROM category")
        category_ids = self.cursor.fetchall()
        return category_ids
