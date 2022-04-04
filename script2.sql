INSERT INTO "user" (id, email, password, username, date_of_birth )
VALUES (1, 'rinirey@yandex.ru', 'strongPassword', 'rinirey', '2001-03-04'),
(2, 'masha@yandex.ru', 'mashaPassword', 'masha', '2000-03-08'),
(3, 'vera@gmail.com', 'veraPass', 'verra', '1998-05-25'),
(4, 'marry2@gmail.com', 'mySecretPassword2', 'marry', '1989-04-04');

INSERT INTO "order" (id, date_of_order, order_price, status, user_id)
VALUES (1, '2022-04-01', 1300, 'in progress', 1),
(2, '2022-03-28', 1500, 'ready', 1),
(3, '2022-03-08', 2500, 'delivered', 4),
(4, '2021-01-31', 500, 'delivered', 2);

INSERT INTO board_game (id, name, description, rules, players, duration, age_limit, release, author)
VALUES (1, 'Carcassonne', 'This game is known as one of the best board games in the world. What is the superiority of "Carcassonne"? In simple rules, in the variety of games, in their short duration, in the absence of open confrontation between the players, this is a classic example of a German-style game.', '' , '2-5', '35+ minutes', 7, '2000', 'Klaus-Jürgen Wrede'),
(2, 'Carcassonne: Expansion 1 — Inns & Cathedrals', 'Now you can play with six players thanks to a whole set of meeples. Scoring will be greatly facilitated with special scoring squares of 50 points. A new large meeple is worth two small ones! Taverns have appeared along the roads, and cathedrals have appeared in the cities, which increase the number of points for completed objects, but if they fail to complete, then they will not bring points at all.', ' ', '2-6', '40+ minutes', 7, '2002', 'Klaus-Jürgen Wrede'),
(3, 'Ghost Letters', 'You are Detectives trying to solve a crime. You found 12 clues on the crime scene, but only 3 of these are True Clues. One of you is the Ghost of the victim, who helps to solve the crime. Detectives choose and send Clues to the Ghost. The Ghost chooses and opens the best as the Hints. One of you is the Murderer, who misleads investigation – in discussion and also bluffing about cards, that were sent to the Ghost and were not opened. In 3 rounds the Detectives need to guess all the 3 True Clues OR any 2 True Clues + the Murderer.', ' ', '2-12', '30+ minutes', 8, '2020', 'Nikita Kuznetsov'),
(4, 'Citadels', 'In Citadels, players take on new roles each round to represent characters they hire in order to help them acquire gold and erect buildings. The game ends at the close of a round in which a player erects his/her eighth building. Players then tally their points, and the player with the highest score wins.', ' ', '2-7', '30-60 minutes', 10, '2000', 'Bruno Faidutti');

INSERT INTO commerce (id, price, availability, arrive, game_id)
VALUES(1, 2500, 'in stock', null, 1),
(2, 1500, 'in stock', null, 2),
(3, 1300, 'in stock', null, 3),
(4, 500, 'out of stock', '2022-05-01', 4);

INSERT INTO feedback (id, review, questions, date_of_publication, user_id, game_id)
VALUES (1, 'I love this game!', null, '2022-03-10', 4, 1),
(2, 'I don`t get it...', 'Can anybody help me with rules?', '2021-02-02', 2, 4);

INSERT INTO cart_intersection (order_id, game_id)
VALUES (1, 3),
(2, 2),
(3, 1),
(4, 4);

INSERT INTO collection (id, name)
VALUES (1, 'Carcassonne');

INSERT INTO collection_intersection (collection_id, game_id)
VALUES (1, 1),
(1, 2);

INSERT INTO category (id, name)
VALUES (1, 'family'),
(2, 'strategy'),
(3, 'detective'),
(4, 'party');

INSERT INTO category_intersection (category_id, game_id)
VALUES (1, 4),
(1, 1),
(1, 2),
(2, 4),
(3, 3);