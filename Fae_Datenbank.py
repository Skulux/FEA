import os
import sqlobject

db_filename = os.path.abspath('Faedatenbank.db')
connection_string = 'sqlite:' + db_filename
connection = sqlobject.connectionForURI(connection_string)
sqlobject.sqlhub.processConnection = connection


class Watchlist(sqlobject.SQLObject):
    movie_id = sqlobject.IntCol()
    rating = sqlobject.FloatCol()
    status = sqlobject.StringCol()
    progress = sqlobject.IntCol(default=0)
    comment = sqlobject.StringCol(length=250)


def createTables():
    Watchlist.createTable(ifNotExists=True)


def get_all_movies_data():
    mv = list(Watchlist.select())
    return [{x.movie_id: [x.rating, x.status, x.progress, x.comment]} for x in mv]


def get_all_movie_ids():
    mv = list(Watchlist.select())
    return [[x.movie_id] for x in mv][0]


def get_movie_data_by_id(id_: int):
    movie = list(Watchlist.select(Watchlist.q.movie_id == id_))
    return [[mv.movie_id, mv.rating, mv.status, mv.progress, mv.comment] for mv in movie][0]


def insert_data(movie_id: int, rating: float, status: str, progress: int, comment: str):
    mv = Watchlist(movie_id=movie_id, rating=rating, status=status, progress=progress,
                   comment=comment)
    return mv


createTables()
#insert_data(475557, 8.8, "Watching", 0, "")