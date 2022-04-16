/*1*/
SELECT * FROM board_game;
SELECT * FROM cart_intersection;
SELECT * FROM category;
SELECT * FROM category_intersection;
SELECT * FROM collection;
SELECT * FROM collection_intersection;
SELECT * FROM commerce;
SELECT * FROM feedback;
SELECT * FROM "order";
SELECT * FROM sale;
SELECT * FROM sale_intersection;
SELECT * FROM "user";
/*2*/
SELECT * FROM sale
WHERE name LIKE 'c%' AND discount >= 50;
SELECT * FROM "order"
WHERE status IN ('ready', 'in progress') AND order_price > 5000;
SELECT name FROM board_game
WHERE release BETWEEN '2010-01-01' AND'2020-01-01' AND age_limit >= 5;
/*3*/
SELECT name, start || '  -  ' || finish as PERIOD FROM sale
WHERE start BETWEEN '2010-01-01' AND'2022-01-01' AND discount >= 50;
/*4*/
SELECT * FROM sale
ORDER BY discount DESC, start;
/*5*/
SELECT MAX(price) FROM commerce;
SELECT MIN(price) FROM commerce;
SELECT floor(AVG(price)) FROM commerce;
/*6*/
SELECT "order".id, "order".date_of_order, "order".status, "user".username, board_game.name as BOARD_GAME 
FROM "order"
INNER JOIN cart_intersection ON cart_intersection.order_id="order".id
INNER JOIN board_game ON cart_intersection.game_id=board_game.id
INNER JOIN "user" ON "order".user_id="user".id;

SELECT "order".id as ORDER_ID, "user".username
FROM "order"
RIGHT JOIN "user" ON "order".user_id="user".id;
/*7,8*/
SELECT game, age_limit, game_count FROM (
	SELECT board_game.name as game, board_game.age_limit as age_limit, count(game_id) as game_count
	FROM cart_intersection
	INNER JOIN board_game ON cart_intersection.game_id=board_game.id
	GROUP BY game,age_limit
) AS foo
WHERE age_limit <= 16
ORDER BY game_count DESC;
/*9*/
INSERT INTO "user" (email, password, username, date_of_birth )
VALUES 
('rinirey@yandex.ru', 'b0bda564df1a5aea0011aae040799dc2f1cdbc4f623e8e320efc90374eaa730e', 'rinirey', '2001-03-04');

INSERT INTO "order" (date_of_order, order_price, status, user_id)
VALUES ('2022-04-01', 1300, 'in progress', 11);

INSERT INTO board_game (name, description, rules, players, duration, age_limit, release, author)
VALUES 
('Carcassonne', 'This game is known as one of the best board games in the world. What is the superiority of "Carcassonne"? In simple rules, in the variety of games, in their short duration, in the absence of open confrontation between the players, this is a classic example of a German-style game.', '' , '2-5', '35+ minutes', 7, '2000', 'Klaus-Jürgen Wrede');

INSERT INTO commerce (price, availability, arrive, game_id)
VALUES(2500, 'in stock', null, 11);

INSERT INTO feedback (review, questions, date_of_publication, user_id, game_id)
VALUES ('I love this game!', null, '2022-03-10', 11, 11);

INSERT INTO cart_intersection (order_id, game_id)
VALUES (1, 11);

INSERT INTO collection (name)
VALUES ('Carcassonne');

INSERT INTO collection_intersection (collection_id, game_id)
VALUES (1, 11);

INSERT INTO category (name)
VALUES ('unknown');

INSERT INTO category_intersection (category_id, game_id)
VALUES (1, 11);

INSERT INTO sale (name, discount, start, finish)
VALUES ('Carcassonne30', 30, '2022-04-01', '2022-04-30');

INSERT INTO sale_intersection (sale_id, commerce_id)
VALUES (1, 11);
/*10*/
UPDATE "order" 
SET status = 'delivered'
WHERE "order".status = 'ready';
/*11*/
DELETE FROM "order"
WHERE date_of_order = (SELECT MIN(date_of_order) FROM "order" WHERE status='delivered');
/*12*/
DELETE FROM sale WHERE id NOT IN (SELECT sale_id FROM sale_intersection);