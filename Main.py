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
    return input("\nSelect: ")

def action(id_):
    id_ = int(id_)
    if id_ == 1:
        data = API.search_by_name(input("Name: "), enable_all=True)
        for e in data:
            print("-"*20)
            print("ID: " + str(e))
            print("Name: "+str(data[e][0]))
            print("Poster: "+str(data[e][1]))
            print("Date: "+str(data[e][2]))
            print("Rating: "+str(data[e][3]))
            print("Description: "+str(data[e][4]))
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
        data = API.get_trending(input("Week, Day: ").lower(), enable_all=True)
        for e in data:
            print("-"*20)
            print("Name: "+str(data[e][0]))
            print("Poster: "+str(data[e][1]))
            print("Date: "+str(data[e][2]))
            print("Rating: "+str(data[e][3]))
            print("Description: "+str(data[e][4]))
            print("-"*20)
            re = input("Next or End: ")
            if re.lower() == "end":
                break
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






def main():
    print("\n"*20)
    print("Loading FEA v0.36 CLI Successful")
    while True:
        action(menu())


if __name__ == "__main__":
    main()
    input("Press to Close")
