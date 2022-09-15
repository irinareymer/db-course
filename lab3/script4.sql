/*1*/
CREATE OR REPLACE VIEW top_5_collections AS 
SELECT DISTINCT collection.name as collection, floor(AVG(commerce.price) OVER (PARTITION BY collection.name)) as avg_price
FROM collection_intersection
INNER JOIN board_game ON collection_intersection.game_id=board_game.id
INNER JOIN commerce ON commerce.game_id=board_game.id
INNER JOIN collection ON collection_intersection.collection_id=collection.id
ORDER BY avg_price DESC
LIMIT 5;

SELECT * FROM top_5_collections;

/*2*/
CREATE OR REPLACE VIEW sale_stats AS
SELECT DISTINCT sale.name AS sale, sale.discount, sale.start, sale.finish, 
COUNT(case when "order".date_of_order BETWEEN sale.start AND sale.finish then 1 else null end) OVER (PARTITION BY sale.name) AS sold_games,
SUM(case when "order".date_of_order BETWEEN sale.start AND sale.finish then "order".order_price else 0 end) OVER (PARTITION BY sale.name, board_game.id) AS sum,
COUNT(case when "order".date_of_order BETWEEN sale.start AND sale.finish AND "order".status IN ('delivered') then 1 else null end) OVER (PARTITION BY sale.name) AS delivered,
COUNT(case when "order".date_of_order BETWEEN sale.start AND sale.finish then 1 else null end) OVER (PARTITION BY sale.name, board_game.id) AS customers
FROM cart_intersection
INNER JOIN board_game ON cart_intersection.game_id=board_game.id
INNER JOIN "order" ON cart_intersection.order_id="order".id
INNER JOIN commerce ON board_game.id=commerce.game_id
INNER JOIN sale_intersection ON commerce.id=sale_intersection.commerce_id
INNER JOIN sale ON sale_intersection.sale_id=sale.id
ORDER BY sum DESC;

SELECT * FROM sale_stats;

/*3*/
CREATE OR REPLACE PROCEDURE CategoryUpdate(categ text, collect text) AS $$
    DECLARE
    categ_id INT;
    collect_id INT;
    t_row category_intersection%rowtype;
    BEGIN
    SELECT id INTO categ_id FROM category WHERE name = categ;
    SELECT id INTO collect_id FROM collection WHERE name = collect;
    CREATE TEMP TABLE game_ids ON COMMIT DROP AS SELECT game_id FROM collection_intersection WHERE collection_id = collect_id;
    FOR t_row in SELECT * FROM category_intersection LOOP
        if (SELECT category_id = categ_id FROM category_intersection 
            WHERE game_id IN (SELECT game_id FROM game_ids) AND category_id = t_row.category_id AND game_id = t_row.game_id) then
            RAISE NOTICE 'Game is already in the category!';
        else
            UPDATE category_intersection SET category_id = categ_id 
            WHERE game_id IN (SELECT game_id FROM game_ids) AND category_id = t_row.category_id AND game_id = t_row.game_id;
        end if;
    end LOOP;
    END $$ LANGUAGE plpgsql;
