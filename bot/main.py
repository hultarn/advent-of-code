import advent_of_code as aoc

import requests
import os.path
import os
import sys
import time
import datetime
import random

def printWithTime(*arg):
    print(datetime.datetime.today().replace(microsecond=0), *arg)

printWithTime("started program...")
year = str(datetime.date.today().year)

try: 
    day = datetime.date.today().day
    printWithTime("starting day", day)
    if day > 25:
        sys.exit()

    day = str(day)
    filepath = day + ".in"

    if not os.path.isfile(filepath): 
        printWithTime("creating file...")
        with open(filepath, "w") as f:
            aoc = aoc.aoc(year, day)
            f.write(aoc.data + "\n")
    else:
        printWithTime("file already exists.")

    # Don't print anything in here...
    startTime = time.time()
    stdout = sys.stdout
    with open('tmp.txt', 'w') as sys.stdout:
        while True:
            r = requests.get("https://raw.githubusercontent.com/user/repo/master/" + year + "/" + day + ".py")
            if r.status_code == 200:
                break
            time.sleep(1)
        exec(r.text)
    sys.stdout = stdout

    printWithTime("solution found.")
    endTime = time.time()
    time.sleep((endTime - startTime) * 3)

    with open('tmp.txt', "r") as f:
        aoc = aoc.aoc(year, day)  
        a1 = f.readline()
        a2 = f.readline()

        printWithTime(a1.rstrip(), aoc.post(a1, 1))
        time.sleep((endTime - startTime) * random.uniform(0.2, 0.5))
        printWithTime(a2.rstrip(), aoc.post(a2, 2))

    printWithTime("deleting tmp.txt")
    os.remove("tmp.txt")

    printWithTime("exiting.")
except Exception as e:
    printWithTime(e)