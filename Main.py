import gatherer as API
import Fae_Datenbank as DB


def println(text: str = ""):
    print("\n"+text)

def menu():
    print("-"*20)
    print("[1] Suche (name)")
    print("[2] Suche (id)")
    print("[3] Genres (id)")
    print("[4] Trends (time)")
    print("[5] Vorschlag (list: ids)")
    print("[6] Watchlist ()")
    return input("\nSelect: ")

def action(id_, re="", time=""):
    id_ = int(id_)
    if id_ == 1:
        data = API.search_by_name(input("Name: "), enable_all=True)
        for i, e in enumerate(data):
            print("-"*20)
            print("ID: " + str(e))
            print("Name: "+str(data[e][0]))
            print("Poster: "+str(data[e][1]))
            print("Date: "+str(data[e][2]))
            print("Rating: "+str(data[e][3]))
            print("Description: "+str(data[e][4]))
            print("["+str(i+1) + "/" + str(len(data))+"]")
            print("-"*20)
            re = input("Next or End: ")
            if re.lower() == "end":
                break
    elif id_ == 2:
        data = API.search_by_id(int(input("ID: ")), enable_all=True)
        print("-"*20)
        print("Name: "+str(data[0]))
        print("Poster: "+str(data[1]))
        print("Date: "+str(data[2]))
        print("Rating: "+str(data[3]))
        print("Description: "+str(data[4]))
        print("-"*20)
    elif id_ == 3:
        data = API.get_genres(int(input("ID: ")))
        for num, e in enumerate(data):
            print("["+str(num)+"]" + str(e))
    elif id_ == 4:
        print("-" * 20)
        time = input("Week, Day: ").lower() if not time else time
        data = API.get_trending(time, enable_all=True)
        for i, e in enumerate(data):
            if re.isnumeric():
                if int(re) < i + 1:
                    action(4, re=re, time=time)
                if int(re) != i + 1:
                    continue
            print("-"*20)
            print("Name: "+str(data[e][0]))
            print("Poster: "+str(data[e][1]))
            print("Date: "+str(data[e][2]))
            print("Rating: "+str(data[e][3]))
            print("Description: "+str(data[e][4]))
            print("[" + str(i + 1) + "/" + str(len(data)) + "]")
            print("-"*20)
            re = input("Next, Page, Save or End: ")
            if re.lower() == "end":
                break
            if re.lower() == "save":
                save(e)

    elif id_ == 5:
        print("-"*20)
        a = input("IDs 'a, b': ").split(", ")
        data = API.search_by_id(API.compare_genres(a), enable_all=True)
        print("Name: "+str(data[0]))
        print("Poster: "+str(data[1]))
        print("Date: "+str(data[2]))
        print("Rating: "+str(data[3]))
        print("Description: "+str(data[4]))
        print("-"*20)

    elif id_ == 6:
        print("-" * 20)
        data = DB.get_all_movies_data()
        for i, e in enumerate(data):
            if re.isnumeric():
                if int(re) < i + 1:
                    action(6, re=re)
                if int(re) != i + 1:
                    continue
            print("ID: "+str(e))
            print("Rating: "+str(data[e][0]))
            print("Status: "+str(data[e][1]))
            print("Comment: "+str(data[e][2]))
            print("[" + str(i + 1) + "/" + str(len(data)) + "]")
            re = input("Next, Page or End: ")
            if re.lower() == "end":
                break
            print("-" * 20)




def save(movie_id):
    try:
        print("-"*20)
        rating = int(input("Rating: "))
        status = int(input("Status (1,2,3): "))
        comment = input("Comment: ")
        DB.insert_data(movie_id, rating, status, comment)
        print("-" * 20)
    except:
        print("could not save data.")


def main():
    print("\n"*20)
    print("Loading FEA v0.37 CLI Successful")
    while True:
        action(menu())


if __name__ == "__main__":
    main()
    input("Press to Close")