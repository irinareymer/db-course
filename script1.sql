DROP DATABASE if exists lab1_reymer;
CREATE DATABASE lab1_reymer;

\c lab1_reymer

CREATE TABLE "user" 
(id serial PRIMARY KEY,
email text NOT NULL UNIQUE,
password text NOT NULL,
username text NOT NULL UNIQUE,
date_of_birth date NOT NULL);

CREATE TABLE "order"
(id serial PRIMARY KEY,
date_of_order date NOT NULL,
order_price integer NOT NULL,
CONSTRAINT valid_order_price CHECK (order_price > 0),
status text NOT NULL,
CONSTRAINT valid_status CHECK (status IN ('in progress', 'ready', 'delivered')),
user_id integer NOT NULL,
FOREIGN KEY (user_id)
REFERENCES "user" (id)
ON DELETE CASCADE);

CREATE TABLE board_game
(id serial PRIMARY KEY,
name text UNIQUE NOT NULL,
description text NOT NULL,
rules text,
players text,
duration text,
age_limit integer DEFAULT 0,
release text,
author text);

CREATE TABLE cart_intersection
(order_id integer,
FOREIGN KEY (order_id)
REFERENCES "order" (id)
ON DELETE CASCADE,
game_id integer,
FOREIGN KEY (game_id)
REFERENCES board_game (id)
ON DELETE CASCADE,
CONSTRAINT cart_intersection_pkey PRIMARY KEY (order_id, game_id));

CREATE TABLE feedback
(id serial PRIMARY KEY,
review text,
questions text,
date_of_publication date NOT NULL,
user_id integer NOT NULL,
FOREIGN KEY (user_id)
REFERENCES "user" (id)
ON DELETE CASCADE,
game_id integer NOT NULL,
FOREIGN KEY (game_id)
REFERENCES board_game (id)
ON DELETE CASCADE);

CREATE TABLE commerce
(id serial PRIMARY KEY,
price integer NOT NULL,
CONSTRAINT valid_price CHECK (price >= 0),
availability text NOT NULL,
CONSTRAINT valid_availability CHECK (availability IN ('in stock', 'out of stock', 'no longer produced')),
arrive date,
game_id integer UNIQUE,
FOREIGN KEY (game_id)
REFERENCES board_game (id)
ON DELETE CASCADE);

CREATE TABLE category
(id serial PRIMARY KEY,
name text NOT NULL);

CREATE TABLE category_intersection
(category_id integer,
FOREIGN KEY (category_id)
REFERENCES category (id)
ON DELETE CASCADE,
game_id integer,
FOREIGN KEY (game_id)
REFERENCES board_game (id)
ON DELETE CASCADE,
CONSTRAINT category_intersection_pkey PRIMARY KEY (category_id, game_id));

CREATE TABLE collection
(id serial PRIMARY KEY,
name text NOT NULL);

CREATE TABLE collection_intersection
(collection_id integer,
FOREIGN KEY (collection_id)
REFERENCES collection (id)
ON DELETE CASCADE,
game_id integer,
FOREIGN KEY (game_id)
REFERENCES board_game (id)
ON DELETE CASCADE,
CONSTRAINT collection_intersection_pkey PRIMARY KEY (collection_id, game_id));
