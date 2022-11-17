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
    """
    creates tables
    :return: None
    """
    Watchlist.createTable(ifNotExists=True)
    return None


def get_all_movies_data(sort_rating=False, sort_status=False, reverse=False):
    """
    Gets all Watchlist Entries attributes
    :return: dict with id as key and list of attributes as values
    """
    mv = list(Watchlist.select())
    p = [{x.movie_id: [x.rating, x.status, x.progress, x.comment]} for x in mv]
    new = {}
    newnew = {}
    for x in p:
        new.update(x)
    for y in new:
        for x in new:
            if not reverse and new[x][0] < new[y][0]:
                newnew[x] = new[x]
            elif new[x][0] > new[y][0]:
                newnew[x] = new[x]
    for x in new:
        if x not in newnew:
            newnew[x] = new[x]
    return new



def get_all_movie_ids():
    """
    Gets all Watchlist Entries IDs
    :return: list of ids
    """
    mv = list(Watchlist.select())
    return [[x.movie_id] for x in mv][0]


def get_movie_data_by_id(movie_id: int):
    """
    Gets all attributes of Watchlist Entry
    :param movie_id: id
    :return: list of Entry attributes
    """
    movie = list(Watchlist.select(Watchlist.q.movie_id == movie_id))
    return [[mv.movie_id, mv.rating, mv.status, mv.progress, mv.comment] for mv in movie][0]


def insert_data(movie_id: int, rating: float, status: str, progress: int, comment: str):
    """
    Create new Watchlist Entry
    :param movie_id: int
    :param rating: float between 0.0 - 10.0
    :param status: string (Plan, Watching, Done)
    :param progress: int
    :param comment: str
    :return: Watchlist Object
    """
    mv = Watchlist(movie_id=movie_id, rating=rating, status=status, progress=progress,
                   comment=comment)
    return mv


def update_data(movie_id: int, rating: float = None, status: str = None, progress: int = None, comment: str = None):
    """
    Updates Watchlist Entries
    :param movie_id: int
    :param rating: float between 0.0 - 10.0
    :param status: string (Plan, Watching, Done)
    :param progress: int
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
            if progress:
                mv.progress = progress
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
    Watchlist.delete(id_)


createTables()
#update_data(475557, rating=9.8)
print(get_all_movies_data(sort_rating=True, reverse=False))
