import datetime
import random
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from generators import User, Order, Feedback, BoardGame, Category, Collection, Commerce, Sale
from queries import UserQuery, OrderQuery, FeedbackQuery, BoardGameQuery, CategoryQuery, CollectionQuery, CommerceQuery, \
    SaleQuery, SaleIntersectionQuery, CategoryIntersectionQuery, CartIntersectionQuery, CollectionIntersectionQuery
import psycopg2
import argparse
from psycopg2 import errors

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--clear', type=bool, default=False,
                        help='A bool argument to create and clear tables')
    parser.add_argument('--users', type=int, default=1,
                        help='An integer argument to define users')
    parser.add_argument('--games', type=int, default=1,
                        help='An integer argument to define board games')
    parser.add_argument('--feedback', type=int, default=1,
                        help='An integer argument to define feedback')
    parser.add_argument('--collections', type=int, default=1,
                        help='An integer argument to define collections')
    parser.add_argument('--sales', type=int, default=1,
                        help='An integer argument to define sales')
    args = parser.parse_args()

    conn = psycopg2.connect(database="board_game_reymer", user="username",
                            password="password", host="localhost", port=5432)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    try:
        with conn:
            with conn.cursor() as cur:
                if args.clear:
                    cur.execute("TRUNCATE board_game, \"user\", \"order\", feedback, commerce, sale, category, "
                                "collection, cart_intersection, collection_intersection, "
                                "category_intersection, sale_intersection" + " RESTART IDENTITY CASCADE ")
                    print("Completed. All tables are empty.")

                category = Category()
                categories = CategoryQuery(cur).select_name()
                if len(categories) != len(category.category):
                    for i in range(len(category.category)):
                        if (category.category[i],) not in categories:
                            CategoryQuery(cur).insert(category.category[i])

                category_ids = CategoryQuery(cur).select_id()

                for i in range(args.games):
                    board_game = BoardGame()
                    try:
                        BoardGameQuery(cur).insert(board_game.name, board_game.description, board_game.rules,
                                                   board_game.players, board_game.duration,
                                                   str(board_game.age_limit),
                                                   board_game.release, board_game.author)
                        gen = True
                    except psycopg2.errors.UniqueViolation:
                        print("Board Game with same name exists")
                        gen = False
                        conn.rollback()

                    if gen:
                        game_id = BoardGameQuery(cur).select_max_id()
                        category_id = random.choice(category_ids)
                        CategoryIntersectionQuery(cur).insert(category_id, game_id)

                        commerce = Commerce()
                        CommerceQuery(cur).insert(commerce.price, commerce.availability, commerce.arrive, game_id)

                commerce_ids = CommerceQuery(cur).select_id()

                for i in range(args.sales):
                    sale = Sale()
                    SaleQuery(cur).insert(sale.name, sale.discount, sale.start, sale.finish)

                    sale_id = SaleQuery(cur).select_max_id()
                    commerce_id = random.choice(commerce_ids)
                    SaleIntersectionQuery(cur).insert(sale_id, commerce_id)

                game_ids = BoardGameQuery(cur).select_id()

                for i in range(args.collections):
                    collection = Collection()
                    CollectionQuery(cur).insert(collection.name)

                    collection_id = CollectionQuery(cur).select_max_id()
                    game_id = random.choice(game_ids)
                    CollectionIntersectionQuery(cur).insert(collection_id, game_id)

                for i in range(args.users):
                    user = User()
                    try:
                        UserQuery(cur).insert(user.email, user.password, user.username, user.date_of_birth)
                    except psycopg2.errors.UniqueViolation:
                        print("User with same info exists")
                        conn.rollback()

                user_ids = UserQuery(cur).select_id()

                for i in range(args.users):
                    order = Order()
                    user_id = random.choice(user_ids)
                    user_birth = UserQuery(cur).select_user_birth(user_id)
                    age = (datetime.date.today().year - user_birth[0].year)
                    game_id = random.choice(game_ids)
                    age_lim = BoardGameQuery(cur).select_age_limit(game_id)
                    if age_lim[0] <= age:
                        OrderQuery(cur).insert(order.date_of_order, order.order_price, order.status, user_id)
                        order_id = OrderQuery(cur).select_max_id()
                        CartIntersectionQuery(cur).insert(order_id, game_id)

                for i in range(args.feedback):
                    user_id = random.choice(user_ids)
                    game_id = random.choice(game_ids)
                    feedback = Feedback()
                    if feedback.review or feedback.questions:
                        FeedbackQuery(cur).insert(feedback.review, feedback.questions,
                                                  feedback.date_of_publication, user_id, game_id)
                print('Data generated')
    finally:
        conn.close()
