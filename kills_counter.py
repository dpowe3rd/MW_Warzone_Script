from bs4 import BeautifulSoup
import requests
import selenium
import json
import pprint

pp = pprint.PrettyPrinter(width=4000)  # Pretty Print to make Console text Easy to read

url = 'https://cod.tracker.gg/warzone/leaderboards/stats/all/Kills?page=1'
res = requests.get(url)
html_soup = BeautifulSoup(res.text, 'html.parser')

stats = html_soup.find_all('td', class_='stat')

# pp.pprint(str(stats[67])[55:].split('<')[0])
for i in range(len(stats)-1):
    kills = str(stats[i])[50:].split('>')[1].split('<')[0]
    matches = str(stats[i+1])[50:].split('>')[1].split('<')[0]

    if kills > matches:
        temp0 = [kills, matches]
        print(temp0)
    else:
        pass

# TODO Fix list out of bounds error
