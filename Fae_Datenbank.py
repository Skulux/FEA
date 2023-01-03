import os
import sqlobject

directory = os.path.dirname(os.path.realpath(__file__))
# Database connection
sqlobject.sqlhub.processConnection = sqlobject.connectionForURI(f'sqlite:{directory}/FEA.db')


class Watchlist(sqlobject.SQLObject):
    movie_id = sqlobject.IntCol()
    rating = sqlobject.FloatCol()
    status = sqlobject.IntCol()
    comment = sqlobject.StringCol(length=250)


def createTables():
    """
    creates tables
    :return: None
    """
    Watchlist.createTable(ifNotExists=True)
    return None


def get_all_movies_data():
    """
    Gets all Watchlist Entries attributes
    :return: dict with id as key and list of attributes as values
    """
    mv = list(Watchlist.select())
    p = [{x.movie_id: [x.rating, x.status, x.comment]} for x in mv]
    new = {}
    for x in p:
        new.update(x)
    return new



def get_all_movie_ids():
    """
    Gets all Watchlist Entries IDs
    :return: list of ids
    """
    mv = list(Watchlist.select())
    return [x.movie_id for x in mv]


def get_movie_data_by_id(movie_id: int):
    """
    Gets all attributes of Watchlist Entry
    :param movie_id: id
    :return: list of Entry attributes
    """
    movie = list(Watchlist.select(Watchlist.q.movie_id == movie_id))
    return [[mv.movie_id, mv.rating, mv.status, mv.comment] for mv in movie][0]


def insert_data(movie_id: int, rating: float, status: int, comment: str):
    """
    Create new Watchlist Entry
    :param movie_id: int
    :param rating: float between 0.0 - 10.0
    :param status: int (1: Planned, 2: Watching, 3: Done)
    :param comment: str
    :return: Watchlist Object
    """
    return Watchlist(movie_id=movie_id, rating=rating, status=status, comment=comment)


def update_data(movie_id: int, rating: float = None, status: int = None, comment: str = None):
    """
    Updates Watchlist Entries
    :param movie_id: int
    :param rating: float between 0.0 - 10.0
    :param status: int (1: Planned, 2: Watching, 3: Done)
    :param comment: str
    :return: None
    """
    try:
        mv = list(Watchlist.select(Watchlist.q.movie_id == movie_id))[0]
        try:
            if rating and 10.0 >= rating >= 0.0:
                mv.rating = rating
            if status:
                mv.status = status
            if comment:
                mv.comment = comment
        except Exception as ER:
            print(ER)
            pass
    except Exception as ERR:
        print(ERR)
        pass
    return None


def delete_entry(id_):
    """
    Deletes an Entry
    :param id_: int
    :return:
    """
    cnvrt_id = [int(x.id) for x in list(Watchlist.select(Watchlist.q.movie_id == id_).limit(1))]
    Watchlist.delete(cnvrt_id[0])


createTables()
#for x in range(800, 900):
#    insert_data(x, 9, 3, "")
#delete_entry(810)
#insert_data(809, 8, 2, "")
#insert_data(810, 0, 1, "")
#update_data(475557, rating=9.8)
#print(get_all_movies_data(sort_status=True))