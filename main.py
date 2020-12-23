#write a simple python script for doing a specific job, write a python script at specific times

import datetime, schedule, requests
import time

def output():
    r = requests.get("https://shapeshed.com/unix-cal/")
    # json decode r.text
#print the name for today in the list

def job():
    date = datetime.datetime.now().strftime("%H")
    runTime = "00"
    if date != runTime:
        return
    output()
#automate the task of printing name so that it prints the name once a day
while True:
    job()
    time.sleep(3600)

#run it in the background in Linux


