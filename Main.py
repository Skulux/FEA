from FEA_G import config, gatherer as API, Fae_Datenbank as DB
import time as t
import subprocess as sub
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

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
    print("[7] Time Test (iterations)")
    print("[8] Config")
    print("[9] START GUI")
    return input("\nSelect: ")

def action(id_, re="", time="", name=""):
    id_ = int(id_) if id_.isnumeric() else action(menu())
    if id_ == 1:
        name = input("Name: ") if not name else name
        data = API.search_by_name(name, enable_all=True)
        for i, e in enumerate(data):
            if re.isnumeric():
                if int(re) < i + 1:
                    action(id_, re=re, time=time, name=name)
                if int(re) != i + 1:
                    continue
            print("-"*20)
            print("ID: " + str(e))
            print("Name: "+str(data[e][0]))
            print("Poster: "+str(data[e][1]))
            print("Date: "+str(data[e][2]))
            print("Rating: "+str(data[e][3]))
            print("Description: "+str(data[e][4]))
            print("["+str(i+1) + "/" + str(len(data))+"]")
            print("-"*20)
            re = input("Next, Page or End: ")
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
                    action(id_, re=re, time=time)
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
        b = API.compare_genres(a)
        data = API.search_by_id(b, enable_all=True)
        print("ID: "+str(b))
        print("Name: "+str(data[0]))
        print("Poster: "+str(data[1]))
        print("Date: "+str(data[2]))
        print("Rating: "+str(data[3]))
        print("Description: "+str(data[4]))
        print("-"*20)
        re = input("Save or End: ")
        if re.lower() == "save":
            save(b)

    elif id_ == 6:
        print("-" * 20)
        data = DB.get_all_movies_data()
        for i, e in enumerate(data):
            if re.isnumeric():
                if int(re) < i + 1:
                    action(id_, re=re)
                if int(re) != i + 1:
                    continue
            print("ID: "+str(e))
            print("Rating: "+str(data[e][0]))
            print("Status: "+str(data[e][1]))
            print("Comment: "+str(data[e][2]))
            print("[" + str(i + 1) + "/" + str(len(data)) + "]")
            re = input("Next, Alter, Remove, Page or End: ")
            if re.lower() == "end":
                break
            if re.lower() == "alter":
                alter(e)
            if re.lower() == "remove":
                remove(e)
            print("-" * 20)

    elif id_ == 7:
        print("-" * 20)
        db_type = int(input("1 (Load Set from DB), 2(Standard Set)"))
        re = int(input("Iterations: "))
        start = t.time()
        for x in range(re):
            API.compare_genres([808, 809, 810] if db_type == 2 else DB.get_all_movie_ids())
            print("Iteration: " + str(x+1))
        print("Iterations Done in: " + str(round(t.time() - start, 2)))
        print("Time per Iteration: " + str(round((t.time() - start)/re, 2)))

    elif id_ == 9:
        sub.run(f"python {os.path.dirname(os.path.realpath(__file__))}/FEA_G/main.py")





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

def alter(movie_id):
    try:
        print("-"*20)
        rating = int(input("Rating: "))
        status = int(input("Status (1,2,3): "))
        comment = input("Comment: ")
        DB.update_data(movie_id, rating=rating, status=status, comment=comment)
        print("-"*20)
    except:
        print("could not alter data.")


def remove(movie_id):
    try:
        print("-"*20)
        DB.delete_entry(movie_id)
        print("Removed Entry.")
        print("-"*20)
    except:
        print("could not remove Entry.")

def main():
    try:
        print("\n"*20)
        print("Loading FEA v0.61 CLI Successful")
        while True:
            action(menu())
    except Exception as ERR:
        with open("Last_SetupError.txt", "w+") as f:
            f.write(str(ERR))

if __name__ == "__main__":
    config.setup()
    main()
    input("Press to Close")
