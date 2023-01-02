import subprocess as sub
try:
    sub.run("pip install -r requirements.txt")
    sub.run("python Main.py")
except Exception as ERR:
    print(ERR)
    with open("Last_SetupError.txt", "w+") as f:
        f.write(str(ERR))
