import time
import random
import requests
KEY = "e93c3350ce19973913e4baf37a49a213"
lang = "de-DE"


def search_by_name(term, title=False, poster=False, date=False, rating=False, overview=False, enable_all=False):
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
        response = requests.get(query)
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


def search_by_id(movie_id, title=False, poster=False, date=False, rating=False, overview=False, enable_all=False):
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
    res = requests.get(query).json()
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
    response = requests.get(query)
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
    genre_ranking = {}
    ids = []
    for movie_id in movie_list:
        ids += [get_genres(movie_id)]
    for id_sets in ids:
        for id_ in id_sets:
            if id_ not in genre_ranking:
                genre_ranking[id_] = 1
            else:
                genre_ranking[id_] += 1
    genre_ranking = {k: v for k, v in sorted(genre_ranking.items(), key=lambda item: item[1], reverse=True)}
    if return_dict:
        return genre_ranking
    return list(genre_ranking)[0], list(genre_ranking)[1], list(genre_ranking)[2]


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
    for page in range(1, 100):
        query = f"https://api.themoviedb.org/3/trending/all/{time_span}?api_key={KEY}&page={page}"
        response = requests.get(query)
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


def compare_genres(movie_list: list, offset: int = 0):
    """
    algorithm to find matching movies based on watched genres
    :param movie_list: list of movie ids
    :param offset: int how many fewer genres need to be matched (3-n)
    :return: int movie id
    """
    fav_genres = get_genre_list(movie_list)
    trending_genres = {}
    for id_ in list(get_trending("week").keys()):
        trending_genres[id_] = get_genres(id_)
    movies = []
    for movie in trending_genres:
        temp_score = 0
        for genre in trending_genres[movie]:
            for genre_ in fav_genres:
                if genre_ == genre:
                    temp_score += 1
        if temp_score == len(fav_genres) - offset and movie not in movie_list:
            movies += [movie]
    if not movies and offset < 3:
        compare_genres(movie_list, offset + 1)
    return random.choice(movies)
    # TODO: Add Multiprocessing?



if __name__ == "__main__":
    #print("Welcome To FEA v0.1")
    #print("Loading...")
    #term = input("Title: ")
    #sus = search_by_name(term, enable_all=True)
    #print(len(sus))
    #print(sus)
    #print(get_genres(808))
    #print(search_by_id(808, enable_all=True))
    #print(get_genre_list([810, 505, 808, 809, 505], return_dict=True))
    start = time.time()
    print(get_trending(enable_all=True))
    print(time.time() - start)
    #print(compare_genres([664469, 808, 809, 810, 505]))