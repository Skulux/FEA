import subprocess as sub

try:
    sub.run("pip install -r requirements.txt")
except Exception as ERR:
    print(ERR)
    with open("Last_SetupError", "w+") as f:
        f.write(str(ERR))
