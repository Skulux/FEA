import subprocess as sub

try:
    sub.run("pip install -r requirements.txt")
except Exception as ERR:
    print(ERR)
