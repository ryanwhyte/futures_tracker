import requests
from bs4 import BeautifulSoup
from time import sleep
from playsound import playsound
from datetime import datetime

today = datetime.today()
current_year = today.year
current_month = today.month
current_day = today.day
hour = today.hour

tracker = []
while datetime(current_year, current_month, current_day, 14) < datetime.now() < datetime(current_year, current_month, current_day, 23):
    base_url = r"https://www.investing.com/"

    r = requests.get(base_url, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c = r.content
    soup = BeautifulSoup(c, "html.parser")

    file = r"C:\Users\Ryan Whyte\programming\my_projects\index_tracker_venv\You_suffer.mp3"

    spfutures = soup.find("td", {"id":"sb_changepc_8839"}).text.replace("+","").replace("-","").replace("%","")
    spfutures = float(spfutures)
    tracker.append(spfutures)
    if len(tracker) > 2:
        tracker.pop(0)
    if len(tracker) == 2: 
        if tracker[-2] < 1.00 and tracker[-1] >= 1.00:
            playsound(file, True)
    sleep(5)
