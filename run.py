import threading
import os
import time


def GO():
    os.system("echo \"1\" >> 1.txt")
    os.system("git add .")
    os.system("git commit -m \"init commit\"")
    os.system("git push origin master")

while 1:
    GO()
    #i = 1
    time.sleep(2)
