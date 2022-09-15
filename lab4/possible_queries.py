read_queries = ["SELECT * FROM board_game",
                "SELECT * FROM commerce",
                "SELECT * FROM feedback",
                "SELECT email FROM \"user\"",
                "SELECT name FROM sale",
                "SELECT status FROM \"order\"",
                "SELECT * FROM sale WHERE name LIKE 'c%' AND discount >= 50",
                "SELECT * FROM \"order\" WHERE status IN ('ready', 'in progress') AND order_price > 5000",
                "SELECT name FROM board_game WHERE release BETWEEN '2010-01-01' AND'2020-01-01' AND age_limit >= 5",
                "SELECT * FROM sale ORDER BY discount DESC, start",
                "SELECT MAX(price) FROM commerce",
                "SELECT MIN(price) FROM commerce",
                "SELECT floor(AVG(price)) FROM commerce",
                "SELECT \"order\".id as ORDER_ID, \"user\".username FROM \"order\" "
                "RIGHT JOIN \"user\" ON \"order\".user_id=\"user\".id"]

change_queries = ["UPDATE \"order\" SET status = 'delivered' WHERE \"order\".status = 'ready'",
                  "UPDATE sale SET discount = 80 WHERE sale.name LIKE 'c%'",
                  "INSERT INTO collection (name) VALUES ('newName')"]

delete_queries = [
    "DELETE FROM \"order\" WHERE date_of_order = (SELECT MIN(date_of_order) FROM \"order\" WHERE status='delivered')",
    "DELETE FROM sale WHERE id NOT IN (SELECT sale_id FROM sale_intersection)",
    "DELETE FROM feedback WHERE feedback.review = null"]
