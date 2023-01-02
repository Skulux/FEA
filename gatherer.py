from random import choice
import requests
from collections import Counter
import multiprocessing
KEY = "e93c3350ce19973913e4baf37a49a213"
lang = "de-DE"


def search_by_name(term: str, title=False, poster=False, date=False, rating=False, overview=False, enable_all=False):
    """
    Gets all Movies and attributes by search term, all attributes are deactivated by default
    :param term: str
    :param title: bool
    :param poster: bool
    :param date: bool
    :param rating: bool
    :param overview: bool
    :param enable_all: bool enables all attributes
    :return: dict with id as key and attributes as list
    """
    if enable_all:
        title = True
        poster = True
        date = True
        rating = True
        overview = True

    page = 1
    query = f"https://api.themoviedb.org/3/search/" \
     f"multi?api_key={KEY}&" \
     f"language={lang}" \
     f"&page={page}" \
     f"&include_adult=true" \
     f"&query={term}"
    response = requests.get(query)
    titles = {}
    for cpage in range(1, int(response.json()["total_pages"]) + 1):
        page = str(cpage)
        query = f"https://api.themoviedb.org/3/search/" \
        f"multi?api_key={KEY}&" \
        f"language={lang}" \
        f"&page={page}" \
        f"&include_adult=True" \
        f"&query={term}"
        response = s.get(query)
        for x in response.json()["results"]:
            try:
                titles[x["id"]] = [x["original_title"] if title else None,
                                               "https://image.tmdb.org/t/p/w600_and_h900_bestv2" + str(x["poster_path"]) if poster else None,
                                               x["release_date"] if date else None,
                                               x["vote_average"] if rating else None,
                                               x["overview"] if overview else None]
            except:
                pass
    return titles


def search_by_id(movie_id: int, title=False, poster=False, date=False, rating=False, overview=False, enable_all=False):
    """
    Gets one Movie and its attributes by id, all attributes are deactivated by default
    :param movie_id: int
    :param title: bool
    :param poster: bool
    :param date: bool
    :param rating: bool
    :param overview: bool
    :param enable_all: bool enables all attributes
    :return: list with attributes
    """
    if enable_all:
        title = True
        poster = True
        date = True
        rating = True
        overview = True
    query = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={KEY}"
    res = s.get(query).json()
    return [res["original_title"] if title else None,
            "https://image.tmdb.org/t/p/w600_and_h900_bestv2" + str(res["poster_path"]) if poster else None,
            res["release_date"] if date else None,
            res["vote_average"] if rating else None,
            res["overview"] if overview else None]


def get_genres(movie_id: int):
    """
    Gets all genres of a movie
    :param movie_id: int
    :return: list of genre ids
    """
    query = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={KEY}"
    response = s.get(query)
    ids = []
    try:
        for x in response.json()["genres"]:
            try:
                ids += [x["id"]]
            except:
                pass
    except:
        pass
    return ids


def get_genre_list(movie_list: list, return_dict=False):
    """
    Gets top 3 genres filtered from the movies or all genres ranked
    :param movie_list: list of movie ids
    :param return_dict: bool return all genres ranked as dict
    :return: list of top 3 genres or dict of all genres ranked
    """
    ids = []
    for movie_id in movie_list:
        ids += [genre for genre in get_genres(movie_id)]
    if return_dict:
        return Counter(ids)
    genre_ranking = list(Counter(ids))
    return genre_ranking[0: len(genre_ranking) if len(genre_ranking) <= 3 else 3]


def get_trending(time_span: str="week", title=False, poster=False, date=False, rating=False, overview=False,
                 enable_all=False):
    """
    Gets all Trending Movies and attributes by timespan, all attributes are deactivated by default
    :param time_span: str ("day" or "week")
    :param title: bool
    :param poster: bool
    :param date: bool
    :param rating: bool
    :param overview: bool
    :param enable_all: bool enables all attributes
    :return: dict with id as key and attributes as list
    """
    if enable_all:
        title = True
        poster = True
        date = True
        rating = True
        overview = True
    titles = {}
    for page in range(1, 6):
        query = f"https://api.themoviedb.org/3/trending/all/{time_span}?api_key={KEY}&page={page}"
        response = s.get(url=query)
        for x in response.json()["results"]:
            try:
                titles[x["id"]] = [x["original_title"] if title else None,
                                   "https://image.tmdb.org/t/p/w600_and_h900_bestv2" + str(
                                       x["poster_path"]) if poster else None,
                                   x["release_date"] if date else None,
                                   x["vote_average"] if rating else None,
                                   x["overview"] if overview else None]
            except:
                pass
    return titles


def compare_genres_helper(id_, fav_genres, offset):
    if len(set(get_genres(id_)) & set(fav_genres)) >= len(fav_genres) - offset:
        return id_
    return None

def compare_genres(movie_list: list, offset: int = 0):
    fav_genres = get_genre_list(movie_list)
    movies = []
    with multiprocessing.Pool() as p:
        movies = [id_ for id_ in p.starmap(compare_genres_helper, [(id_, fav_genres, offset) for id_ in list(get_trending("week").keys())]) if id_ is not None]
    return choice(movies) if movies and offset <= 2 else compare_genres(movie_list, offset + 1)


s = requests.session()
