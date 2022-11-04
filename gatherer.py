import requests
KEY = "e93c3350ce19973913e4baf37a49a213"
lang = "de-DE"


def search_by_name(term, title=False, poster=False, date=False, rating=False, overview=False, *args, **kwargs):
    settings = [title, poster, date, rating, overview]
    try:
        if kwargs["enable_all"]:
            title = True
            poster = True
            date = True
            rating = True
            overview = True
    except:
        pass

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
        f"&include_adult=true" \
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


print(search_by_name("Shrek", enable_all=True))

